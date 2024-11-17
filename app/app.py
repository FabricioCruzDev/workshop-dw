import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis do arquivo .env
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Criar a URL de conexão do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# query para consultar o banco

def get_data():
    query = f"""
            SELECT * FROM public.dm_commodities;"""
    df = pd.read_sql(query, engine)
    return df

df = get_data()

# configurar streamlit
# página
st.set_page_config(page_title= 'Dashboard desempenho das commodities', layout='wide')

#Título do Dashboard
st.time_input('Últimas movimentações')

#Descrição]
st.write("""Dashboard com o dados sobre as operações realizadas""")
         
# Obter dados
st.dataframe(df)