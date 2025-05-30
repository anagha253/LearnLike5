import streamlit as st
from main import generate_response, prompt_ans, simplify_for_kids

st.title("🧠 Explain Like I'm 5 – AI Agent")

concept = st.text_input("Enter a concept you want explained:")

if st.button("Explain It!"):
    with st.spinner("Thinking..."):
        step1 = generate_response(prompt_ans(concept))
        st.subheader("🤔 Thought + Observation")
        st.write(step1)

        step2 = generate_response(simplify_for_kids(concept, step1))
        st.subheader("🎉 Final Answer")
        st.write(step2)