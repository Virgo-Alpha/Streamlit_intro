import streamlit as st

st.set_page_config(page_title="Portfolio Page",
                   page_icon=":tada:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# --- CONTACT ME ---
with st.container():
    # st.write("---")
    st.title("Contact Me: :email:")
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