import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

hit = list(pd.read_csv('Hit_If.csv')['Hit If'])
double = list(pd.read_csv('Double_If.csv')['Double If'])

## teste
st.set_page_config(page_title="BJ Houdini", 
                    page_icon=":🧠:",
                    layout="wide")

st.title('Blackjack Houdini')
your_sum = st.text_input('What is the sum of your cards?:')
dealers_card = st.text_input('Whats the dealers card?:')
has_a= st.toggle('Do you have an A?')
if has_a:
    has_a = 'with A'
else:
    has_a = 'without A'

state = f'{your_sum} {has_a} + {dealers_card}' 
dub = "Just "
if state in double:
  dub = "Double it and "
if state in hit:
    st.header(f"{dub}Hit it!")
else:
    st.header("Dont Hit!") 




