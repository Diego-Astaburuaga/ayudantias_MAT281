import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir(r'C:\Users\diego\OneDrive - Universidad Técnica Federico Santa María\(01)-University\(10)_X_Semestre\(01)-Ayud. Aplicaciones\ayudantias_MAT281\Streamlit')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

st.title('Ayudantía 1: Probando Streamlit')
st.write('La ayudantía "oficial" es la realizada en el Jupyter Notebook, la cual fue una introducción al ecosistema de Python. Esté último documento es amor al arte.')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#


st.header('Ejemplo de caso de modelo de clasificación')
st.write('Un problema puede ser abordado mediantes *problemas de clasificación* cuando este se centra en poder indentificar una carácteristica binaria (o discreta) mediante conocer otras variables.')

st.markdown('Para este ejemplo, cargaremos un conjunto de datos de `Kaggle`. El conjunto de datos entrega información sobre distintos tipos de hongos, así como si estos son venenosos o no. El objetivo es tener un modelo que sea capaz de determinar si un hongo en venenoso o no en función de sus carácteristicas.')
st.markdown('[Pincha aquí para ver más información.](https://www.kaggle.com/datasets/uciml/mushroom-classification?select=mushrooms.csv)')

mushrooms_df = pd.read_csv('../datasets/mushrooms.csv')
st.dataframe(mushrooms_df)

st.markdown('Más información en la próxima ayudantía.')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#


st.header('Ejemplo de caso de series temporales')
st.write('El análisis de series temporales puede ser realizados en datos que se encuentran indexados por una variable temporal. Las aplicaciones pueden ser comprender la serie temporal o bien buscar predecirla.')

st.markdown('Para este ejemplo, usaremos el valor del precio del dolar respecto a nuestra moneda (CLP). Estos datos son extraidos de `yfinance`.')

ticker = 'USDCLP=X'
dolar_df = yf.download(ticker, period='1mo', interval='1d')
dolar_close_price = pd.Series(dolar_df["Close"])

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dolar_close_price.index, dolar_close_price, marker='o', linestyle='-')
ax.set_title('Evolución del precio de cierre del dólar en los últimos 30 días')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio de Cierre (CLP)')
ax.grid(True)
st.pyplot(fig)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

st.header('Ejemplo de caso de geoestadística')
st.write('Para este enfoque de estadística espacial, se busca estudiar el comportamiento de una variable indexada en el espacio en base a conocer ciertas localizaciones especificas.')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#