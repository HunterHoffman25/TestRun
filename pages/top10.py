import streamlit as s
import numpy as n
import pandas as p
import matplotlib.pyplot as pl

s.title("Top 10 Smallest Countries")
uf = r'C:/Users/hhoffman25\Documents/HOPES/Population/pages/wp.csv'

if uf is not None:
    df = p.read_csv(uf)
    sc = ['Rank','Country', '2022 Population']
    top5 = df.nsmallest(10, '2022 Population')

    fig, ax = pl.subplots()
    ax.plot(top5['Country'], top5['2022 Population'], marker='o', linestyle='-')
    ax.set_xlabel('Country')
    ax.set_ylabel('2022 Population')
    ax.set_title('Top 10 Smallest Countries')
    ax.set_ylim(500, 15000)
    y_ticks = [500, 1500, 2500, 5000, 7500, 10000, 15000]
    ax.set_yticks(y_ticks)
    ax.tick_params(axis='x', rotation=45)

    s.pyplot(fig)