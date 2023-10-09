import streamlit as st
import smtplib
import ssl
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="Olamide Olajide",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(
    f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Olamide Olajide"}</h1>',
    unsafe_allow_html=True)
st.markdown(
    f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Data Analyst | AI Engineer"}</h1>',
    unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

text_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">I am a skilled data analyst with expertise in Natural Language Processing (NLP) and Python development. I\'ve made meaningful contributions to organizations like the Ethereum Foundation, Lilnouns.eth, Flipside Crypto. I\'m currently contributing my data analysis skills to Metricsdao.<br><br>My passion lies in transforming data into actionable insights. With a strong track record of leveraging NLP to extract valuable information from unstructured text, I\'m dedicated to helping organizations harness the power of data for strategic decision-making and innovation. Explore my portfolio to see how I can bring data-driven success to your organization.</p>'

st.markdown(text_1, unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.empty()

with col2:
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.markdown("[![](https://api.iconify.design/fa6-brands/github.svg?download=1&width=50&height=50)](https://github.com/oolajide/)")
    with col2:
        st.markdown("[![](https://api.iconify.design/fa6-brands/linkedin.svg?download=1&width=50&height=50)](https://www.linkedin.com/in/olamide-olajide-2b913b1b4/)")
    with col3:
        st.markdown("[![](https://api.iconify.design/fa6-brands/square-twitter.svg?download=1&width=50&height=50)](https://twitter.com/sageOlamide)")
with col3:
    st.empty()

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(
    f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"My Projects 💼"}</h1>',
    unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

# project 1
st.markdown(
    f'<h1 style="font-size:30px;text-align:left;"><a href="https://huggingface.co/spaces/OOlajide/common-nlp-tasks">Common NLP Tasks</a></h1>',
    unsafe_allow_html=True)

st.markdown("""
    - Perform common natural language processing tasks like extractive question answering, text summarization and text generation using [huggingface transformers](https://huggingface.co/docs/transformers/index).
    - Featured in the top 8 machine learning apps of the week on [huggingface spaces](https://huggingface.co/spaces) upon release.
    """)


st.markdown(
    f'<h1 style="color:#434346;font-size:30px;text-align:center;">{"CONTACT ME"}</h1>',
    unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.empty()

with col2:

    with st.form("contact_me", clear_on_submit=True):
        name = st.text_input("Name:")
        email = st.text_input("Email Address:")
        message = st.text_area("Message:")
        if st.form_submit_button("Send 📨"):
            email_from = 'oladaniel19@gmail.com'
            password = st.secrets["gmail_app_password"]
            email_to = 'oladaniel19@gmail.com'
            email_string = f'''Subject: OOlajide - Contact Me
{name}\n\n{email}\n\n{message}
            '''
            # Connect to the Gmail SMTP server and Send Email
            # Create a secure default settings context
            context = ssl.create_default_context()
            # Connect to Gmail's SMTP Outgoing Mail server with such context
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                # Provide Gmail's login information
                server.login(email_from, password)
                # Send mail with from_addr, to_addrs, msg, which were set up as variables above
                server.sendmail(email_from, email_to, email_string)
            st.success('Sent', icon="✅")

with col3:
    st.empty()