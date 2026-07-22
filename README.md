# 🎬 Pipeline ETL - Filmes em Cartaz (TMDB API)

## 📌 Sobre o Projeto
Este é um projeto prático desenvolvido durante a minha graduação em Engenharia de Dados pela faculdade Infnet, com foco prático em Banco de Dados. 

O objetivo principal foi construir um pipeline ETL (Extract, Transform, Load) completo, consumindo dados em tempo real da API do The Movie Database (TMDB). A ideia surgiu não apenas como um exercício acadêmico, mas também para automatizar a escolha do que assistir nas minhas idas ao cinema aos domingos, criando um banco de dados próprio com as opções em cartaz.

## ⚙️ Arquitetura e Tecnologias
O fluxo dos dados foi estruturado em três etapas fundamentais usando **Python**:

* **Extract (E):** Utilização da biblioteca `requests` para consumir a API REST do TMDB, com implementação de paginação para extrair uma amostra maior de filmes (100 registros).
* **Transform (T):** Uso da biblioteca `pandas` para converter o retorno JSON em um DataFrame estruturado, filtrando apenas as colunas relevantes (título, data de lançamento, popularidade e nota) e padronizando os nomes dos campos.
* **Load (L):** Persistência dos dados processados em um banco de dados relacional **SQLite** (`cinema.db`), utilizando a funcionalidade nativa do Pandas para inserção SQL.

## 🚀 Como Executar
1. Clone este repositório.
2. Instale as dependências executando: `pip install requests pandas`.
3. Crie uma conta no [TMDB](https://www.themoviedb.org/) e gere sua própria API Key.
4. Substitua o valor `SUA_CHAVE_AQUI` no código pela sua chave real.
5. Execute o script principal: `python Projeto_cinema.py`.
6. O arquivo `cinema.db` será gerado automaticamente na raiz do projeto com os dados prontos para consultas SQL.
