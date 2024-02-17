import streamlit as st

st.set_page_config(page_title="Github Wrapped Page",
                   page_icon=":tada:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")


# Display a video from a local file
st.title("My 2023 Github Unwrapped: :octopus:")
st.write("##")
video_file = open('images/unwrapped-Virgo-Alpha.mp4', 'rb')
video_bytes = video_file.read()
st.write("Please view in full screen mode for a better experience.")
st.video(video_bytes)

# # Display a video from a URL
# st.title('Video from URL')
# video_url = 'https://www.example.com/example_video.mp4'
# st.video(video_url)


# st.title('YouTube Video Example')
# # Embed a YouTube video
# st.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
