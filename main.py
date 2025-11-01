import pandas as pd
import plotly.express as px
from solana.rpc.api import Client

def get_solana_performance():
    """
    Busca os dados de performance recentes da rede Solana e os retorna em um DataFrame.
    (VERSÃO CORRIGIDA para a biblioteca solders)
    """
    print("Conectando à rede Solana (mainnet)...")
    
    solana_client = Client("https://api.mainnet-beta.solana.com")

    try:
        # 1. A resposta é um objeto, não uma lista. Vamos chamá-la de 'response'.
        response = solana_client.get_recent_performance_samples(limit=60)
        
        # 2. A lista de amostras real está dentro de 'response.value'
        samples_list = response.value
        
        if not samples_list:
            print("Nenhuma amostra de performance foi retornada.")
            return None

        print(f"Sucesso! {len(samples_list)} amostras de performance recebidas.")

        # 3. Precisamos extrair os dados dos objetos 'solders' manualmente
        #    Os nomes dos atributos também mudaram (ex: num_transactions)
        data_for_df = []
        for sample in samples_list:
            data_for_df.append({
                'slot': sample.slot,
                'numTransactions': sample.num_transactions,  # Nome do atributo mudou
                'samplePeriodSecs': sample.sample_period_secs # Nome do atributo mudou
            })

        # Agora criamos o DataFrame a partir da nossa lista de dicionários
        df = pd.DataFrame(data_for_df)

        # O resto do código funciona como antes, pois
        # criamos as colunas com os nomes que o script já esperava
        
        df['tps'] = df['numTransactions'] / df['samplePeriodSecs']
        
        df = df.iloc[::-1].reset_index(drop=True)
        df['tempo_amostra'] = df.index * (df['samplePeriodSecs'].mean() / 60) 

        return df

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return None

def create_performance_chart(df):
    """
    Cria um gráfico de linha interativo com o Plotly e o salva em HTML.
    (Esta função não precisa de mudanças)
    """
    if df is None:
        print("Não há dados para gerar o gráfico.")
        return

    print("Gerando gráfico de performance...")
    
    fig = px.line(df, 
                  x='tempo_amostra', 
                  y='tps', 
                  title='Performance da Rede Solana (TPS)',
                  labels={'tempo_amostra': 'Tempo (Minutos aproximados)', 'tps': 'Transações por Segundo (TPS)'},
                  markers=True) 

    fig.write_html("solana_tps_chart.html")
    print("Sucesso! Gráfico salvo como 'solana_tps_chart.html'")

# --- Função Principal ---
if __name__ == "__main__":
    performance_data = get_solana_performance()
    
    if performance_data is not None:
        print("\n--- Últimas 5 Amostras de Dados ---")
        print(performance_data.tail())
        print("----------------------------------\n")
        
        create_performance_chart(performance_data)
