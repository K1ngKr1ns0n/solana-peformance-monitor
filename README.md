# solana-peformance-monitor
# 📈 Monitor de Performance da Rede Solana

Este projeto é um script em Python que monitora a performance (Transações Por Segundo - TPS) da rede Solana. Ele utiliza a API RPC pública, processa os dados com Pandas e gera um gráfico interativo com Plotly.

Este projeto foi criado como parte do meu portfólio de Engenharia de Software e Análise de Dados.

## 🚀 Resultado

Aqui está um exemplo do gráfico interativo (salvo como HTML) gerado pelo script:
<img width="1820" height="919" alt="image" src="https://github.com/user-attachments/assets/990caf47-82b9-4af2-b80c-5c46fb4e3bf1" />


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
