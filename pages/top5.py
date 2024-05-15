import streamlit as s
import numpy as n
import pandas as p
import matplotlib.pyplot as pl

s.title("Top 5 Largest Countries")
uf = r'C:/Users/hhoffman25\Documents/HOPES/Population/pages/wp.csv'

if uf is not None:
    df = p.read_csv(uf)
    sc = ['Rank','Country', '2022 Population']
    top5 = df.nlargest(5, '2022 Population')

    fig, ax = pl.subplots()
    ax.bar(top5['Country'], top5['2022 Population'])
    ax.set_xlabel('Country')
    ax.set_ylabel('2022 Population in Billions')
    ax.set_title('Top 5 Largest Country')
    ax.set_ylim(100000000, 2000000000)
    y_ticks = [100000000, 500000000, 1000000000, 1500000000, 2000000000]
    ax.set_yticks(y_ticks)
    ax.tick_params(axis='x', rotation=45)

    s.pyplot(fig)