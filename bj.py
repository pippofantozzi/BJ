import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu



## teste
st.set_page_config(page_title="TCS DeepConsultant", 
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


df = pd.read_csv('Odds.csv')

state = f'{your_sum} {has_a} + {dealers_card}' 
prob_not_loss = df.loc[df['State'] == state, 'Not Losing Chance']
st.title(f'Probability of Not Losing: {str(prob_not_loss)}')


