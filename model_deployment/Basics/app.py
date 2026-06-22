import streamlit as st
st.write('This is my first Streamlit app!')
st.title('Hello Streamlit👋')
# name=st.text_input("Enter your name:")
# if name:
#     st.success(f"Hello {name},welcome to Streamlit!")
# else:
#     st.error("Enter a valid name")
st.title('This is title')
st.header('This is header')
st.subheader('This is subheader')
st.text('This is Simple text')
st.markdown("**Bold text**,*Italics* and `code-style text`")

####Widgets#####

#button
if st.button('Click Me!'):
    st.write('Button Clicked!')

#checkbox
agree=st.checkbox("I agree to Terms and Conditions")
if  agree:
    st.write('You agreed☑️')

#radio buttons
choice=st.radio('Choose any one:',["Option A","Option B","Option C"])
st.write("You selected:",choice)

#selectbox
option=st.selectbox("Pick a number:",[1,2,3,4,5])
st.write("Your number is:",option)

#slider
value=st.slider("Select a range",0,100,25) #min,max,defualt
st.write("Slider value:",value)

#Data Display(Dataa Frame)
import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.randn(10,3),columns=["A","B","C"])
st.write('Random Data Frame:',df)
st.line_chart(df)
st.bar_chart(df)

#Upload&display file
file=st.file_uploader("Upload a CSV file",type=["csv"])
if file:
    data=pd.read_csv(file)
    st.write(data.head())

#Layouts&Sidebar
st.sidebar.title('Sidebar Menu')
user=st.sidebar.text_input("Enter your username")
st.sidebar.text(f"Welcome {user}")

#columns
col1,col2=st.sidebar.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")