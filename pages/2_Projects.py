import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# TODO: Sub-divide the projects into categories - SWE & Web Development, Data Science & ML, GenAI.
# TODO: Add downloadable resume that can be previewed on the website.

st.set_page_config(page_title="Projects' Page",
                   page_icon=":tada:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

img_menta = Image.open("images/Menta.png")
img_refacer = Image.open("images/refacer.png")
img_dashboard = Image.open("images/dashboard.png")
img_profile = Image.open("images/ben.jpeg")
img_fake_news = Image.open("images/fake_news.png")
img_job_data = Image.open("images/job_data.png")
img_tembea_kenya = Image.open("images/tembea_kenya.png")
img_opus_futura = Image.open("images/Opus_Futura.png")
img_sustravels = Image.open("images/sustravels.png")
img_linkedin_resume_builder = Image.open("images/linkedin_resume_builder.png")
img_CarbonCalc = Image.open("images/CarbonCalc.png")
img_Story_gen = Image.open("images/Story-gen.png")

with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            # insert image here
            st.image(img_Story_gen, width=300)
        with text_column:
            st.subheader("Gen Ai + Web App: Story Generator")
            st.write(
                """
                - This Streamlit app uses the Google Generative AI API to generate stories based on user prompts.
                - Users can input a prompt, generate a story, and clear the response.
                - Tech stack: Streamlit, Google Generative AI API, and Python. 
                - You can find the code [here](https://github.com/Virgo-Alpha/Story_generator).
                    """)
            st.markdown("[View Project >](https://story-generator2.streamlit.app/)")

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
            - You can find the project code [here](https://github.com/Virgo-Alpha/Menta)
                """)
        st.markdown("[View Project >](https://menta.onrender.com/)")

with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_CarbonCalc, width=300)
        with text_column:
            st.subheader("Website: Carbon emission calculator")
            st.write(
                """
                - This Streamlit app allows users to estimate their carbon footprint based on the distance traveled between two cities.
                - Additionally, it provides information on the environmental impact by calculating the potential harm to wildlife in terms of the number of animals that would be affected.
                - I used haversine, pandas, openpyxl and streamlit to build it.
                - Project code can be found [here](https://github.com/Virgo-Alpha/CarbonCalc)
                    """)
            st.markdown("[View Project >](https://carbon-calc.streamlit.app)")

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

with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_linkedin_resume_builder, width=300)
        with text_column:
            st.subheader("Website: LinkedIn Resume Builder")
            st.write(
                """
                - I developed a website that allows one to scrap their LinkedIn profile and generate a resume from it.
                - I used selenium, beautiful soup, and streamlit to build it.
                - Project code can be found [here](https://github.com/Virgo-Alpha/linkedin_resume_builder)
                    """)
            st.markdown("[View Project >](https://linkedin-resume-builder.streamlit.app/)")
