import pandas as pd
import plotly.express as px
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Price Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
)

df = pd.read_excel(
    io = 'pricelist.xlsx',
    engine='openpyxl',
    # sheet_name='Price'
    # skiprows=3,
    # usecols='B:R'
    nrows=100,
)

with st.container():

    st.header("**明的作品")

    st.title("A boss that say nothing")
    st.subheader("Hi, I am Eric")
    st.write("There's no need to spend days or weeks building a website anymore. ")
    st.write("[Learn More >](https://www.baidu.com)")

    # st.sidebar.header("Please Filter Here:")
    # industry = st.sidebar.multiselect(
    #     "Select the industry:",
    #     options=df["INDUSTRY"].unique(),
    #     default=df["INDUSTRY"].unique()
    #
    # )

    # size = st.sidebar.multiselect(
    #     "Select the size:",
    #     options=df["SIZE"].unique(),
    #     default=df["SIZE"].unique()

    # )

    company = st.sidebar.multiselect(
        "Select the company:",
        options=df["COMPANY"].unique(),
        default=df["COMPANY"].unique()

    )



    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
    """

    st.markdown(hide_st_style, unsafe_allow_html=True)

    df_selection = df.query(
        "COMPANY ==@company"
    )

    st.dataframe(df_selection)

    st.markdown("---")

    size_by_industry = (
        df_selection.groupby(by=["COMPANY"]).sum()[["SIZE"]].sort_values(by="SIZE")
    )
    # st.dataframe(size_by_industry)

    fig_industry_size = px.bar(
        size_by_industry,
        x="SIZE",
        y=size_by_industry.index,
        orientation ="h",
        title ="<b>Size by Industry</b>",
        color_discrete_sequence=["#0083B8"]*len(size_by_industry),
        template="plotly_white",
    )


    # st.plotly_chart(fig_industry_size)


    fig_industry_size1 = px.bar(
        size_by_industry,
        y="SIZE",
        x=size_by_industry.index,
        # orientation ="h",
        title ="<b>Size by Industry</b>",
        color_discrete_sequence=["#0083B8"]*len(size_by_industry),
        template="plotly_white",
    )
    # st.markdown("---")

    left_column,right_column = st.columns(2)
    left_column.plotly_chart(fig_industry_size, use_container_width=True)
    right_column.plotly_chart(fig_industry_size1, use_container_width=True)

# st.plotly_chart(fig_industry_size1)

lottie_coding = "https://assets2.lottiefiles.com/packages/lf20_q4KeH0MSPB.json"


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_8udmnhsx.json")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
⭐ 𝗧𝗮𝗯𝗹𝗲 𝗼𝗳 𝗖𝗼𝗻𝘁𝗲𝗻𝘁𝘀
00:00 – Introduction 
00:25 – Basic Page Configuration 
01:16 – Header Section
02:55 – About Me Section
03:51 – Insert Animations
06:07 – Project Section
07:58 – Contact Form 
11:04 – Change Streamlit Theme
12:08 – Outro
            """
        )
    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")

image1 = Image.open("images/1.png")
image2 = Image.open("images/2.png")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(image1)

    with text_column:
        st.subheader("Integrate Lottie Animations Inside")
        st.write(
            """
            There's no need to spend days or weeks building a website anymore. .

🌎 𝗥𝗘𝗦𝗢𝗨𝗥𝗖𝗘𝗦:
Check out the website here: 
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com)")

with st.container():

    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(image2)

    with text_column:
        st.subheader("Integrate Lottie Animations Inside")
        st.write(
            """
            There's no need to spend days or weeks building a website anymore. 
            
🌎 𝗥𝗘𝗦𝗢𝗨𝗥𝗖𝗘𝗦:
Check out the website here: 
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/540309694@qq.com" method="POST">
     <input type="hidden" name="_captcha"value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
with st.container():
    st.write("")
    st.write("---")
    st.subheader(":raising_hand: FAQ")
    faq = {
        "Question 1": "Some text goes here to answer question1",
        "Question 2": "Some text goes here to answer question2",
        "Question 3": "Some text goes here to answer question3",
        "Question 4": "Some text goes here to answer question4",
        "Question 5": "Some text goes here to answer question5",
        "Question 6": "Some text goes here to answer question6",
        "Question 7": "Some text goes here to answer question7",
    }
    for question, answer in faq.items():
        with st.expander(question):
            st.write(answer)