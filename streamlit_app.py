import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDw02JFnQlIcU5T6qVXj3zj8YhSQ3Och5U")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response = model.generate_content([input_text, image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data= uploaded_file.getvalue()
        image_parts=[
                {
                    "mime_type":uploaded_file.type,
                    "data":bytes_data
                }
                    ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded.")
    
st.set_page_config(page_title="Khushi's Invoice generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Khushi")
st.sidebar.write("Powered by google gemini ai")
st.header("ROBOBILL")
st.subheader("Made by Khushi")
st.subheader("Manage Your Expenses with RoboBill")
input= st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image", type = ["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption = "Uploaded Image", use_column_width=True)

submit = st.button("Lets Go")

input_prompt = """
You are an expert in calculus. 
We are going to upload an image of a question and you are going to solve the question step wise.
You have to greet the user first. 
Make sure to keep the fonts uniform and give the steps in bullet points format
At the end, make sure to repeat the name of the app RoboBill and ask the user to use it again
"""
if submit:
     image_data= input_image_details(uploaded_file)
     response = get_gemini_response(input_prompt, image_data,input)
     st.subheader("Here's what you need to know!")
     st.write(response)

