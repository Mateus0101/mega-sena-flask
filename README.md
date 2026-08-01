# Simulador Mega-Sena IA
🍀Simulador de números da Mega-Sena utilizando um modelo de IA (Random Forest) para prever os próximos números mais prováveis com base nos últimos concursos. O sistema também exibe os 10 números mais prováveis em um gráfico interativo.

## Estrutura do Projeto
mega-sena-flask/ <br>
│ <br>
├── static/ <br>
│ ├── css/ <br>
│ │ ├── style.css # Estilos customizados <br>
│ │ └── bootstrap.min.css <br>
│ ├── js/ <br>
│ │ ├── chart.min.js # Biblioteca Chart.js <br>
│ │ └── main.js # Scripts da aplicação <br>
│ └── img/ <br>
│ └── trevo.png # Ícone favicon 🍀 <br>
│ <br>
├── templates/ <br>
│ └── index.html # Página principal <br>
│ <br>
├── app.py # Aplicação Flask <br>
├── requirements.txt # Dependências do projeto <br>
├── README.md # Documentação do projeto <br>
│ <br>
└── venv/ # Ambiente virtual (não versionado) <br>

## Requisitos
  * Python 3.10 ou superior
  * pip
  * Virtualenv - recomendado

## Dependências principais
  * Flask
  * pandas
  * numpy
  * scikit-learn
  * requests
  
Instalação rápida:
  pip install -r requirements.txt

## Como rodar o projeto
  1. Clone ou baixe o repositório.
  2.  Crie e ative um ambiente virtual (opcional, mas recomendado):
    python -m venv venv  <br>
   * Windows: venv\Scripts\activate  <br>
   * Linux / Mac: source venv/bin/activate
  4. Instale as dependências:
    pip install -r requirements.txt
  5. Execute o servidor Flask:
    python app.py
  6. Abra no navegador:
    http://127.0.0.1:5000

## Como funciona
  1. Atualização automática: O backend agora consulta a API da Caixa para obter os resultados mais recentes da Mega-Sena e salva localmente em resultados.csv.
  2. O backend lê os dados do CSV atualizado.
  3. Treina um modelo de Random Forest com os últimos N concursos para prever os próximos números.
  4. Exibe na tela os 6 números sugeridos e o Top 10 de números mais prováveis em um gráfico.
  5. Um loader animado indica que o sistema está processando os dados enquanto a IA calcula as probabilidades.
  6. Se quiser mudar quantos concursos recentes são usados como base para a previsão, altere a constante JANELA no início do arquivo "app.py" (por padrão, 15 concursos).

## Aviso
  A Mega-Sena é um sorteio aleatório e independente: nenhum modelo estatístico ou de IA consegue prever seus resultados de fato. Este projeto é um estudo/experimento com Machine Learning, não um preditor confiável de números.
    

## UI
  * Tela limpa e responsiva usando Bootstrap.
  * Loader animado enquanto os cálculos são feitos.
  * Gráfico interativo usando Chart.js.

## Licença
  MIT License
