import streamlit as s
import numpy as n
import pandas as p
import matplotlib.pyplot as pl

s.title("Top 10 Countries From 70s till Now")
uf = r'C:/Users/hhoffman25\Documents/HOPES/Population/pages/wp.csv'

if uf is not None:
    sc = [
    'Country',
    '2022 Population', 
    '1970 Population', 
    '1980 Population', 
    '1990 Population', 
    '2000 Population', 
    '2010 Population', 
    '2015 Population', 
    '2020 Population'
    ]
    df = p.read_csv(uf, names=sc)

    df_sorted = df.sort_values(by='2022 Population', ascending=False)
    top_10_countries = df_sorted.head(10)
    print(top_10_countries)
    s.line_chart(top_10_countries.set_index('Country'))