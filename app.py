import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My First Web Page", page_icon=":tada:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://lottie.host/b8347808-b365-493c-8e68-680ef844d61c/NbyJ92QuTQ.json")

# --- HEADER ---
with st.container():
    st.subheader("Hi, I am Ben :wave:")
    st.title("A software engineer who loves to code :computer:")
    st.write("I am a software engineer who loves to code and build things. I am passionate about learning new technologies and applying them to solve real-world problems.")
    st.write("[Learn More >](https://www.linkedin.com/in/benson-mugure-017153196/)")

# --- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do: :hammer_and_wrench:")
        st.write("##")
        st.write("I am a full-stack software engineer who loves to build things. I have experience building web applications using Python, Django, Flask, and React. :snake: :atom_symbol:")
        st.write("I am also a data science enthusiast. I have experience building machine learning models using Python and Scikit-learn library. :snake: :bar_chart:")
        st.write("I am currently learning Data Engineering at Cloud Academy. :cloud:")

    with right_column:
        st_lottie(lottie_coding, speed=1, height=300, key="coding")