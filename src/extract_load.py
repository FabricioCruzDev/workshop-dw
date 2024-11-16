# import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# import das variáveis de ambiente

# pegar a cotação dos meus ativos

commodities = ['CL=F', 'GC=F', 'SI=F']

def buscar_dados_commodities(ticker_id, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker('CL=F')
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['ticker_id'] = ticker_id
    return dados

def buscar_todos_dados_commodities(commodities):
    df = []
    for c in commodities:
        dados = buscar_dados_commodities(c)
        df.append(dados)
    return pd.concat(df)

# concatenar os meus ativos (1..2...3) -> (1)

# salvar no banco de dados

if __name__ == "__main__":
    df_final = buscar_todos_dados_commodities(commodities)
    print(df_final)
