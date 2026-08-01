window.addEventListener("DOMContentLoaded", () => {
    fetch("/gerar_numeros")
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro na resposta do servidor: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Esconde loader
            document.getElementById("loader-container").style.display = "none";

            // Mostra números previstos dentro de círculos
            const container = document.getElementById("numeros-previstos");
            container.innerHTML = ""; // limpa caso haja conteúdo anterior
            container.style.display = "flex";
            container.style.justifyContent = "center";
            container.style.flexWrap = "wrap";

            data.numeros_previstos.forEach(num => {
                const div = document.createElement("div");
                div.className = "numero-circulo"; // classe do CSS
                div.textContent = num;
                container.appendChild(div);
            });

            // Mostra quantos concursos foram usados no treino
            const infoConcursos = document.getElementById("info-concursos");
            infoConcursos.textContent = `Baseado em ${data.concursos_usados} concursos históricos.`;
            infoConcursos.style.display = "block";

            // Mostra o gráfico
            const ctx = document.getElementById("grafico").getContext("2d");
            document.getElementById("grafico").style.display = "block";

            new Chart(ctx, {
                type: "bar",
                data: {
                    labels: data.top10.map(t => t[0]),
                    datasets: [{
                        label: "Probabilidade",
                        data: data.top10.map(t => t[1]),
                        backgroundColor: "#198754",
                        borderColor: "#146c43",
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: { y: { beginAtZero: true } }
                }
            });
        })
        .catch(() => {
            document.getElementById("loader-container").style.display = "none";
            document.getElementById("erro-container").style.display = "block";
        });
});
