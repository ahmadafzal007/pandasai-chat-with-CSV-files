from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe

# Initialize the model
try:
    model = LocalLLM(api_base="http://localhost:11434/v1", model="llama3")
    st.success("Model loaded successfully.")
except Exception as e:
    st.error(f"Failed to load model: {e}")

st.title("Data analysis with PandaAI")

uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(3))

    try:
        df = SmartDataframe(data, config={"llm": model})
        st.success("Dataframe initialized with the model.")
    except Exception as e:
        st.error(f"Failed to initialize SmartDataframe: {e}")

    prompt = st.text_area("Enter your prompt: ")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                try:
                    response = df.chat(prompt)
                    st.write(response)
                except Exception as e:
                    st.error(f"Error during generation: {e}")
