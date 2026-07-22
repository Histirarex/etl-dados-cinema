import requests
import pandas as pd
import sqlite3

# 1. Configurações da API
API_KEY = "SUA_CHAVE_AQUI"

def extrair_filmes():
    print("Conectando ao TMDB para buscar filmes em cartaz...")
    todos_os_filmes = []
    
    for pagina in range(1, 6):
        url_paginada = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=pt-BR&page={pagina}"
        resposta = requests.get(url_paginada)

        if resposta.status_code == 200:
            dados = resposta.json()
            lista_filmes = dados['results']
            todos_os_filmes.extend(lista_filmes)
        else:
            print(f"❌ Erro na página {pagina}. Código HTTP: {resposta.status_code}")
            
    print(f"✅ Sucesso! Encontramos {len(todos_os_filmes)} filmes.")
    return todos_os_filmes

def transformar_dados(lista_filmes):
    print("Transformando os dados com Pandas...")
    df = pd.DataFrame(lista_filmes)
    
    colunas_selecionadas = ['title', 'release_date', 'popularity', 'vote_average']
    df_limpo = df[colunas_selecionadas]
    df_limpo = df_limpo.rename(columns={
        'title': 'titulo',
        'release_date': 'data_lancamento',
        'popularity': 'popularidade',
        'vote_average': 'nota_media'
    })
    
    return df_limpo

def carregar_dados(df):
    print("Iniciando a carga no Banco de Dados...")
    # Cria a conexão (se o arquivo não existir, o Python cria pra você na mesma pasta)
    conexao = sqlite3.connect("cinema.db")
    
    # O Pandas cria a tabela 'filmes_cartaz' e insere os dados automaticamente
    df.to_sql(name="filmes_cartaz", con=conexao, if_exists="replace", index=False)
    
    print("✅ Pipeline ETL concluído! Dados salvos no banco 'cinema.db'.")
    conexao.close()

# ==========================================
# BLOCO DE EXECUÇÃO
# ==========================================
if __name__ == "__main__":
    # E - Extração
    filmes_brutos = extrair_filmes()
    
    if filmes_brutos:
        # T - Transformação
        filmes_transformados = transformar_dados(filmes_brutos)
        
        # L - Carga
        carregar_dados(filmes_transformados)