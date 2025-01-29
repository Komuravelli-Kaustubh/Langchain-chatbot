import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community import chain 

import os
from dotenv import load_dotenv
load_dotenv()


os.environ['GOOGLE_API_KEY']=os.getenv('GEMINI_API_KEY')
#Langsmith
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a very intelligent and helpful assistant . Please respond to user queries"),
         ("user","Question:{question}")
    ]
)

st.title("Langchain chatbot with GEMINI")
input_txt=st.text_input("Enter your question: ")

#Gemini LLm Instance
llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.7)
output_parser = StrOutputParser()

chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'question':input_txt}))