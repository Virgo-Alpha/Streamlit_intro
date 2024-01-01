import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
# from streamlit_option_menu import option_menu


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio Page",
                   page_icon=":tada:",
                   layout="wide",
                   initial_sidebar_state="collapsed"
                   )

# ! Makes all pictures circular
# st.markdown("""
#   <style>
#     // st-emotion-cache-0 e1f1d6gn0
#     .st-emotion-cache-1v0mbdj::first-child {
#       border-radius: 50%;
#     }
#   </style>
# """, unsafe_allow_html=True)

# # ! 1. Nav bar as sidebar
# with st.sidebar:
#     selected = option_menu(
#         menu_title=None,
#         options=["Home", "Projects", "Contact Me"],
#         icons=["🏠", "💻", "📧"],
#         menu_icon="cast",
#         default_index=0,
#     )

# # ! 2. Nav bar as horizontal menu
# selected = option_menu(
#         menu_title=None,
#         options=["Home", "Projects", "Contact Me"],
#         icons=["🏠", "💻", "📧"],
#         menu_icon="cast",
#         default_index=0,
#         orientation="horizontal",
#         styles={
#                 "container": {"padding": "0!important", "background-color": "black"},
#                 "icon": {"color": "orange", "font-size": "25px"},
#                 "nav-link": {
#                     "font-size": "25px",
#                     "text-align": "left",
#                     "margin": "0px",
#                     "--hover-color": "#eee",
#                 },
#                 "nav-link-selected": {"background-color": "green"},
#             },
#     )

# st.title(f"You are on the {selected} page")
# st.sidebar.success("Selecet a page from the above")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# --- LOAD ASSETS ---
# Find the animation at lottiefiles.com and copy the url here
lottie_coding = load_lottieurl("https://lottie.host/b8347808-b365-493c-8e68-680ef844d61c/NbyJ92QuTQ.json")
img_menta = Image.open("images/Menta.png")
img_refacer = Image.open("images/refacer.png")
img_dashboard = Image.open("images/dashboard.png")
img_profile = Image.open("images/ben.jpeg")
img_fake_news = Image.open("images/fake_news.png")
img_job_data = Image.open("images/job_data.png")
img_tembea_kenya = Image.open("images/tembea_kenya.png")
img_opus_futura = Image.open("images/Opus_Futura.png")
img_sustravels = Image.open("images/sustravels.png")

# --- HEADER ---
with st.container():
    col1, col2 = st.columns([2, 1])
    col1.subheader("Hi, I am Ben :wave:")
    col1.title("A software engineer who loves to code :computer:")
    col1.write("I am passionate about learning new technologies and applying them to solve real-world problems.")
    col1.write("In particular, I am interested in DARQ [Distributed Ledgers, AI, Extended Realities and Quantum Computing] or ABCD [AI, Blockchain, Cloud and Data] technologies.")
    col1.write("I am also passionate about entrepreneurship and Sustainability, especially through Circular Economy.")
    col1.write("I am a cinephile and I play chess in my free time.")
    col1.write("I also read books and write creative articles on [manenoz.com](https://sarunisays.wordpress.com/virgo-alpha/) and technical ones on [Medium](https://medium.com/@b.mugure).")
    col1.write("I have also written poems at [AllPoetry](https://allpoetry.com/Virgo_Alpha).")
    col1.write("[Learn More >](https://www.linkedin.com/in/benson-mugure-017153196/)")
    # ? Make only the profile picture below circular
    col2.image(img_profile, width=300, output_format='PNG', caption='Me')

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


# --- PROJECTS ---
with st.container():
    st.write("---")
    st.header("Projects: :computer:")
    st.write("##")

with st.expander("Click to view projects"):
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            # insert image here
            st.image(img_refacer, width=300)
        with text_column:
            st.subheader("Deep Fake: The Harder They Fall")
            st.write(
                """
                - I replaced Cherokee Bill's face with mine in this scene in The Harder they Fall movie. 
                - I used Refacer to do this. Refacer is a web app that allows you to replace faces in videos. 
                - You can find it [here](https://github.com/xaviviro/refacer?ref=alxappliedai.com).
                    """)
            st.markdown("[View Project >](https://www.linkedin.com/posts/benson-mugure-017153196_alxabrai-deepfake-appliedai-activity-7142568176705347584-PVdY?utm_source=share&utm_medium=member_desktop)")
            
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_menta, width=300)
        with text_column:
            st.subheader("Web App: Mentorship")
            st.write(
                """
                - This is a web app that connects mentors and mentees. 
                - It is built using Nodejs, Express-js, Mustache, nedb, and Bootstrap.
                    """)
            st.markdown("[View Project >](https://menta-b-mugure-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_dashboard, width=300)
        with text_column:
            st.subheader("Streamlit Dashboard: Data Visualization")
            st.write(
                """
                - A sample dashboard built using Streamlit, Plotly, and duckdb.
                - Allows you to visualize data from a data file that you upload.
                - Automated visualizations are generated using python functions and plotly.
                - Initialized with a placeholder xlsx data file.
                    """)
            st.markdown("[View Project >](https://prototype-dashboard.streamlit.app/)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_fake_news, width=300)
        with text_column:
            st.subheader("Web App: Fake News Detection")
            st.write(
                """
                - A simple web app built with Flask to detect fake news.
                - Powered by TfidfVectorizer and PassiveAggressiveClassifier from sklearn to classify news as fake or real upon request from a user
                - Find the code on Github [here](https://github.com/Virgo-Alpha/Fake_News_Detection)
                    """)
            st.markdown("[View Project >](https://benson.pythonanywhere.com/)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_opus_futura, width=300)
        with text_column:
            st.subheader("Web App: Opus Futura")
            st.write(
                """
                - A simple web app built with friends to demonstrate the future of work for the 2023 SD Worx Hackathon (Sparkathon).
                - Opus AI is a software that allows employees to manage their tasks, get support from AI to optimize their workflows and generates reports that offer insights on performance and career development opportunities.
                - Tech stack: React, React, web forms, and UI components for the FE, Flask, OpenAI, TextBlob, and RESTful APIs for the BE
                - View the project [here](https://docs.google.com/presentation/d/13boiVSN6j1A9mFH0a7dphd8rL5EixLTk/edit?usp=sharing&ouid=102435224940560953120&rtpof=true&sd=true) and the demo [here](https://drive.google.com/file/d/1nqAEdfJOi5pMPPBkOesndzoLsoxVcnK0/view?usp=sharing) and the code on Github [here](https://github.com/Stoichiometrical/sdWorx)
                    """)
            st.markdown("[View Project >](https://velvety-pudding-c3b592.netlify.app/)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_sustravels, width=300)
        with text_column:
            st.subheader("Web App: Sustravels")
            st.write(
                """
                - Sustravels is a website that allows travelers to check how much damage their travel is doing to the environment.
                - It is implemented as a django web application with an embedded carbon calculator that enables the user (e.g., a tourist) to gauge their carbon emissions as well as how many animals, particularly the big 5: Leopard, Lion, Buffalo, Rhino & Elephant, they will be killing.
                - View the code on Github [here](https://github.com/Virgo-Alpha/Sustravels)
                    """)

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_job_data, width=300)
        with text_column:
            st.subheader("Web App: Data on Jobs Available")
            st.write(
                """
                - A simple web app built with friends
                - The project involved finding sources of interesting data related to jobs worldwide including two dissimilar sources then selecting and applying suitable visualisations to represent the data.
                - The data was sourced live via APIs, rather than being previously downloaded.
                - Find the code on Github [here](https://github.com/Emmastro/ip-project-2)
                    """)
            st.markdown("[View Project >](https://ip-project-2.vercel.app/)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_tembea_kenya, width=300)
        with text_column:
            st.subheader("Website: Concierge and travel Services")
            st.write(
                """
                - I developed a concierge website that would enable locals, expats, and tourists to look for different services available in my country of origin based on their needs.
                - Project code can be found [here](https://github.com/Virgo-Alpha/Tembea-Kenya)
                    """)
            st.markdown("[View Project >](https://tembeakenya1.netlify.app/)")

# --- CONTACT ME ---
with st.container():
    st.write("---")
    st.header("Contact Me: :email:")
    st.write("##")
    
    # used the free service at formsubmit.co to send the form data to my email
    contact_form = """
<form action="https://formsubmit.co/b.mugure@alustudent.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
     <button type="submit">Send</button>
</form>

"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        