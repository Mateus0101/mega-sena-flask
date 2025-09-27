from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

app = Flask(__name__)

@app.route("/")
def index():
    # Apenas renderiza o template, sem processar a IA ainda
    return render_template("index.html")


@app.route("/gerar_numeros")
def gerar_numeros():
    # -----------------------------
    # 1. Ler Excel
    # -----------------------------
    arquivo = "mega_sena_asloterias_ate_concurso_2919_sorteio.xlsx"
    df = pd.read_excel(arquivo)

    # Detectar linha do cabeçalho correto
    for i, row in df.iterrows():
        if "Concurso" in row.values:
            df.columns = row
            df = df[i+1:]
            break

    # Padronizar nomes das colunas
    df.columns = [str(c).strip().replace(" ", "").capitalize() for c in df.columns]
    df = df[["Bola1","Bola2","Bola3","Bola4","Bola5","Bola6"]]

    # Converter para inteiros
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna().astype(int)

    # -----------------------------
    # 2. Preparar dados para IA
    # -----------------------------
    sorteios = df.values.tolist()
    mlb = MultiLabelBinarizer(classes=range(1, 61))
    y = mlb.fit_transform(sorteios)

    N = 5  # últimos concursos
    X, Y = [], []
    for i in range(N, len(y)):
        X.append(y[i-N:i].flatten())
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
    prob_array = np.array([p[:,1] for p in probabilidades]).flatten()

    # Ranking dos números mais prováveis
    ranking = np.argsort(prob_array)[::-1] + 1
    top10 = [(int(num), float(prob_array[num-1])) for num in ranking[:10]]

    # 6 números sugeridos
    numeros_previstos = [int(n) for n in ranking[:6]]

    return jsonify({
        "numeros_previstos": sorted(numeros_previstos),
        "top10": top10
    })


if __name__ == "__main__":
    app.run(debug=True)
