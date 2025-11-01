# solana-peformance-monitor
Um script Python que monitora a peformance (TPS) da rede solana e gera um gráfico interativo usando Plotly
# 📈 Monitor de Performance da Rede Solana

Este projeto é um script em Python que monitora a performance (Transações Por Segundo - TPS) da rede Solana. Ele utiliza a API RPC pública, processa os dados com Pandas e gera um gráfico interativo com Plotly.

Este projeto foi criado como parte do meu portfólio de Engenharia de Software e Análise de Dados.

## 🚀 Resultado

Aqui está um exemplo do gráfico interativo (salvo como HTML) gerado pelo script:

*(Aqui você deve tirar um print screen do seu `solana_tps_chart.html` e colar a imagem aqui. O GitHub permite colar imagens direto no editor.)*

![Exemplo do Gráfico de TPS](caminho/para/sua/imagem.png)

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **solana-py:** Biblioteca cliente oficial para interagir com a API RPC da Solana.
* **Pandas:** Para manipulação e estruturação dos dados de performance.
* **Plotly:** Para a criação do gráfico de linha interativo.

## 🏁 Como Executar

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/solana-performance-monitor.git](https://github.com/SEU_USUARIO/solana-performance-monitor.git)
    cd solana-performance-monitor
    ```

2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Você deve criar um arquivo `requirements.txt` com o comando: `pip freeze > requirements.txt` e adicioná-lo ao GitHub)*

4.  Execute o script:
    ```bash
    python main.py
    ```

5.  Abra o arquivo `solana_tps_chart.html` no seu navegador.
