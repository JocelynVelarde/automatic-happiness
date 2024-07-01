import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
        page_title="Boopie",
        page_icon="🐝",
)

st.title("Boopie")

st.divider()

st.write("Una paginita para un boopie muy bonito.")
st.write("Okei la idea es que aqui puedo agregar cosas lindas para que tu las veas en momentos random del dia, yyyy lo mejor es que siempre pondre cosas distintas para que digas omg ahora que sera.")
st.write("Un update jijiss para revivir la apps")
st.divider()

st.subheader("Primero la musiquita chida del momento")

st.write("Miraa esta es una muy chida que honestamente yo la habia escuchado en algun lado y resulto que me encanto")

components.html(
    """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/1b6F3QgBBg7HND2hfY6Tav?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""",
height=365
)

st.divider()

st.write("Okeeei esta es porque me recuerda demasiado a ti, la verdad es que la mayoria de las canciones que escucho me recuerdan a ti pero pues sippp")

components.html(
    """
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6v5J4UE21xOjnQ4N9H5jur?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""",
height=365
)   
