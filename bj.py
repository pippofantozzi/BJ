import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

hit = list(pd.read_csv('Hit.csv')['State'])
double = list(pd.read_csv('Double.csv')['State'])
#split = list(pd.read_csv('Correct_Splits.csv')['Split'])

## teste
st.set_page_config(page_title="BJ Houdini", 
                    page_icon=":🧠:",
                    layout="wide")

st.title('Blackjack Houdini')
your_sum = st.text_input('What is the sum of your cards?:')
dealers_card = st.text_input('Whats the dealers card?:')
has_a= st.toggle('Do you have a flexible A?')
if has_a:
    has_a = 'with flexible A'
else:
    has_a = 'without flexible A'

state = f'{your_sum} {has_a} + {dealers_card}' 
dub = "Just "
split_it = ""
if state in double:
  dub = "Double it and "


if (state != " without flexible A + ") and  (state != " with flexible A + "):
  if state in hit:
    st.header(f"{split_it}{dub} Hit It!") 
  else:
    st.header(f"{split_it}Dont Hit!") 


st.markdown("---")
st.title("Some Rules:")
st.markdown("---")
st.text("- This method assumes you always play the same initial bet in each hand")
st.text("- This method assumes you should prioritize splitting over hitting when prompted to do so")
st.text("- This method assumes that you should only split or double if you have sufficient capital")
st.text("- This method assumes that if your initial bet is always $10, and you have $6 remaining, you bet $6 (whatever is left)") 
st.text("Keep in mind: Still not 100% sure about splitting method, but try it for now, except just ignore when it says to split and do whatever is next to it")






