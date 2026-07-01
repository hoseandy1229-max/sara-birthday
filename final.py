import streamlit as st

st.set_page_config(page_title = "Sara" , page_icon = "✨")

st.markdown("""
    <style>
    .stAPP {
        background_color: #ffe4e6;
    }
    div.stButton > button {
        background_color: #00bfff;
        color: white;
        border_radius: 20px;
        border: none;
    }
    div.stButton > button: hover {
        background_color: #009acd;
    }
    h1 , h2 , h3 , p , div {
        color: #00bfff !important;
    }
    </style>
""", unsafe_allow_html = True)


st.title("تولدت مبارک سارا")
st.write("شاید یکم برای تبریک دیر شده باشه ولش به هر حال گفته بودم یه کادو بهت میدم امیدوارم خوشت بیاد تولدت مبارک")

audio_file = open('music.mp3.mp3' , 'rb')
audio_bytes = audio_file.read()
if st.button("دکمه شروع"):
    st.audio(audio_bytes , format = 'audio/mp3')
    st.balloons()
    from streamlit_extras.let_it_rain import rain

    rain(
        emoji = "💐",
        font_size = 54,
        falling_speed = 5,
        animation_length = "infinite"
    )