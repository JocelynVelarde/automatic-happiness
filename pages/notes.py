import streamlit as st

st.set_page_config(
        page_title="Boopie",
        page_icon="🐝",
)

st.title("Para escribir mensajitos")

st.divider()

def load_messages():
    try:
        with open("messages.txt", "r") as file:
            messages = file.readlines()
        messages = [message.strip() for message in messages]
    except FileNotFoundError:
        messages = []
    return messages

def save_message(message):
    with open("messages.txt", "a") as file:
        file.write(message + "\n")

if 'messages' not in st.session_state:
    st.session_state['messages'] = load_messages()

with st.form("form"):
    st.write("Aqui para dejar notitas jiji")

    text_input = st.text_input(label="Escribe el mensajito")

    submitted = st.form_submit_button("Submit")
    if submitted:

        st.session_state['messages'].append(text_input)
        save_message(text_input)
        st.success("Ya se agrego wiii")

for message in st.session_state['messages']:
    st.subheader(message)