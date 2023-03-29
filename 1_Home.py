import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json
import pandas as pd


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Matthew Kimmell", page_icon="chart_with_upwards_trend", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding_whatido = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


with open("images/new-bitcoin-touch.json", 'r') as json_f:
    header_json = json.load(json_f)
lottie_coding_header = header_json

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Matthew Kimmell :wave:")
        st.title("Your Friendly Neighborhood Bitcoin Pal")
        st.write(
            "Welcome to my humble abode, it's a simple space, but if you stick around long enough, I promise to teach you something new :bulb:"
        )
        st.write("[Twitter](https://twitter.com/MatthewKimmell)")
        #st.write("[YouTube](https://www.youtube.com/channel/UCV00jVwqZ_cyP-yygLtWFjA)")
        st.write("[Linkedin](https://www.linkedin.com/in/matthew-kimmell-780554121/)")
    with right_column:
        st_lottie(lottie_coding_header, height=350, key="bitcoin")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I visualize data and write for people that:
            - are interested in learning about Bitcoin
            - enjoy storytelling through charts and graphs
            - want to perform meaningful and impactful analyses by themselves
            - don't have time for the deeper research

            If this sounds interesting to you, please be in touch, I'd be happy to chat with you.
            """
        )
    with right_column:
        st_lottie(lottie_coding_whatido, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ 
    contact_form = """
    <form action="https://formsubmit.co/mattkimmellyt@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
