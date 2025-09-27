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
└── venv/ # Ambiente virtual (não versionar) <br>

## Requisitos
  * Python 3.10 ou superior
  * pip
  * Virtualenv - recomendado

## Dependências principais
  * Flask
  * pandas
  * numpy
  * scikit-learn
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
  1. O backend lê os dados do arquivo Excel com os resultados da Mega-Sena.
  2.  Treina um modelo de Random Forest com os últimos N concursos para prever os próximos números.
  3. Exibe na tela os 6 números sugeridos e o Top 10 de números mais prováveis em um gráfico.
  4. Um loader animado mostra que o sistema está processando os dados enquanto a IA calcula as probabilidades.

## UI
  * Tela limpa e responsiva usando Bootstrap.
  * Loader animado enquanto os cálculos são feitos.
  * Gráfico interativo usando Chart.js.

## Como adicionar novos dados
  Substitua ou atualize o arquivo Excel (mega_sena_asloterias_ate_concurso_XXXX_sorteio.xlsx) mantendo a mesma estrutura:
  * Concurso	Data	bola 1	bola 2	bola 3	bola 4	bola 5	bola 6
  * Para baixar um arquivo atualizado, acesse o site: https://asloterias.com.br/todos-resultados-mega-sena#google_vignette 
     <img width="287" height="335" alt="image" src="https://github.com/user-attachments/assets/1560335a-1fc1-46cf-8577-a9790d5f9e61" />
  * Substitua dentro do diretório do projeto o arquivo que era o último concurso até o momento desse projeto: mega_sena_asloterias_ate_concurso_2919_sorteio.xlsx
  * Altere dentro do arquivo "app.py" na linha número 20 o nome do arquvio atualizado.
  * Observação: Será feita uma pesquisa para possibilidade de integrar esse projeto a uma API para facilitar esse processo de não precisar de atualizar os dados manualmente.

## Licença
  MIT License
