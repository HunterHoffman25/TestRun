import streamlit as s
import numpy as n
import pandas as p
import matplotlib.pyplot as pl

s.title("Salary Database")
uf = 'Jimmeh.csv'

if uf is not None:
    df = p.read_csv(uf)
    sc = ['Employer','Job Title', 'Annual Base Pay']
    top5 = df.nlargest(5, 'Annual Base Pay')


    jon, ax = pl.subplots()
    ax.pie(top5['Annual Base Pay'], labels=top5['Employer'], autopct='%1.1f%%')
    ax.axis('equal')


    fig, ax = pl.subplots()
    ax.bar(top5['Employer'], top5['Annual Base Pay'])
    ax.set_xlabel('Employer')
    ax.set_ylabel('Annual Base Pay')
    ax.set_title('Top 5 Best Annual Base Pays')
    ax.tick_params(axis='x', rotation=45)


    dfs = df[sc]
    s.write(dfs.head(100))
    s.pyplot(fig)
    s.pyplot(jon)

