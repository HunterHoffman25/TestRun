import pandas as pd
import matplotlib.pyplot as plt
import streamlit as s

s.title("Top 10 Countries From 70s till Now")
uf = r'C:/Users/hhoffman25\Documents/HOPES/Population/pages/wp.csv'

if uf is not None:
    sc = ['Country', '1970 Population']
    df = pd.read_csv(uf, names=sc)


    df.set_index('Country', inplace=True)  

    df.plot(kind='pie', y='1970 Population', figsize=(8, 8), autopct='%1.1f%%', startangle=140)
    plt.title('Population Distribution in 1970')
    plt.ylabel('')  
    plt.show()
