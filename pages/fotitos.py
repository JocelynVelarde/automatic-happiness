import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
        page_title="Boopie",
        page_icon="🐝",
)

st.title("Fotitos de la semanita")

st.divider()

st.write("Okei las pondría todas en la main page pero mi spotify anda muriendo no se porqueee, tengo que esperar como 5 minutos a que deje de ponerse en negro la pantalla del monitor, pero hummmmm sussss.")
st.write("Aqui unas fotitos de la semana tan bonita (todas son bonitas a tu lado)")

st.image('assets/image1.jpg', caption='Unos patitos paseando en la nochecita')

st.divider()

st.image('assets/image2.jpg', caption='Borbs muy felices')

st.divider()

sorpresa = st.button("Click Click Click quack")
not_sorpresa = st.button("Buzzyyyy buzzy bee")

if(sorpresa):
    st.balloons()

if(not_sorpresa):
    st.toast("Bee boopie borb", icon="🐝")