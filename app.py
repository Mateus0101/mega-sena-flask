from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import requests
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

app = Flask(__name__)

# -----------------------------
# Configurações globais
# -----------------------------
API_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"
ARQUIVO = "resultados.csv"

# -----------------------------
# Função para atualizar resultados
# -----------------------------
def atualizar_resultados():
    colunas_esperadas = ["Concurso", "Data", "Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]

    if os.path.exists(ARQUIVO):
        df = pd.read_csv(ARQUIVO, sep=";")
        df.columns = [
            c.strip().replace(" ", "").capitalize() if "bola" in c.lower() else c.strip().capitalize()
            for c in df.columns
        ]
        for col in colunas_esperadas:
            if col not in df.columns:
                df[col] = np.nan
        ultimo_concurso = df["Concurso"].max() if not df.empty else 0
    else:
        df = pd.DataFrame(columns=colunas_esperadas)
        ultimo_concurso = 0

    novos = []
    concurso = int(ultimo_concurso) + 1

    while True:
        resp = requests.get(f"{API_URL}/{concurso}")
        if resp.status_code != 200:
            break
        dados = resp.json()
        bolas = [int(b) for b in dados["dezenasSorteadasOrdemSorteio"]]
        data_apuracao = dados.get("dataApuracao", "")
        novos.append([dados["numero"], data_apuracao] + bolas)
        concurso += 1

    if novos:
        novos_df = pd.DataFrame(novos, columns=colunas_esperadas)
        df = pd.concat([novos_df, df], ignore_index=True)

        # Ordena todos os concursos do maior (mais recente) para o menor
        df = df.sort_values(by="Concurso", ascending=False).reset_index(drop=True)

        df.to_csv(ARQUIVO, index=False, sep=";")

    return df

# -----------------------------
# Rotas Flask
# -----------------------------
@app.route("/")
def index():
    # Apenas renderiza o template, sem processar a IA ainda
    return render_template("index.html")


@app.route("/gerar_numeros")
def gerar_numeros():
    # -----------------------------
    # 1. Atualizar resultados
    # -----------------------------
    df = atualizar_resultados()

    # -----------------------------
    # 2. Preparar dados para IA
    # -----------------------------
    sorteios = df[["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]].values.tolist()
    mlb = MultiLabelBinarizer(classes=range(1, 61))
    y = mlb.fit_transform(sorteios)

    # 70% dos concursos para treino
    N = int(len(y) * 0.7)

    X, Y = [], []
    for i in range(N, len(y)):
        X.append(y[i - N:i].flatten())
        Y.append(y[i])
    X = np.array(X)
    Y = np.array(Y)

    # -----------------------------
    # 3. Treinar Random Forest
    # -----------------------------
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X, Y)

    # -----------------------------
    # 4. Prever próximo concurso
    # -----------------------------
    ultimos_n = y[-N:].flatten().reshape(1, -1)
    probabilidades = clf.predict_proba(ultimos_n)
    prob_array = np.array([p[:, 1] for p in probabilidades]).flatten()

    # -----------------------------
    # 5. Ranking dos números mais prováveis
    # -----------------------------
    ranking = np.argsort(prob_array)[::-1] + 1
    top10 = [(int(num), float(prob_array[num - 1])) for num in ranking[:10]]

    # -----------------------------
    # 6. números sugeridos
    # -----------------------------
    numeros_previstos = [int(n) for n in ranking[:6]]

    return jsonify({
        "numeros_previstos": sorted(numeros_previstos),
        "top10": top10,
        "concursos_usados": len(df)
    })

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
