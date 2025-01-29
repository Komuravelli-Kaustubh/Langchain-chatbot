import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
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

st.title("Langchain chatbot with Ollama")
input_txt=st.text_input("Enter your question: ")

#Ollama local LLm Instance
llm=Ollama(model="llama2",temperature=0.7)
output_parser = StrOutputParser()

chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'question':input_txt}))