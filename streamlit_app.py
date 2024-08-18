import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# st.write('Hello world')
st.header('Header for buttons')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')    


st.header('day 5')

# display tesxt nd markdown
st.write('Hello, *World!* :sunglasses:')

# display number
st.write(1234)

# display dataFrames
df = pd.DataFrame({'first_column': [1,2,3,4], 
                  'second_column': [10,20,30,40],
                  'third_column': ['a', 'b', 'c', 'd']
             }
             )

st.write(df)

# pass in multiple arguments
st.write('Below is a df',df, 'Above is a df')

df2 = pd.DataFrame(
                   np.random.randn(200,3),
                   columns = ['a', 'b', 'c']
                   )
st.write(df2)

c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)




