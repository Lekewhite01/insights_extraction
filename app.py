import streamlit as st
import openai
import re
import nltk
nltk.download('punkt')
from nltk import tokenize
from gensim.summarization import summarize

# nltk.download('omw-1.4')

api_key = st.text_input(label='Enter your API Key',)

@st.cache
def second_grade(text,userPrompt="Summarize this for a second-grade student:"):
    openai.api_key = api_key
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=userPrompt + "\n\n" + text,
    temperature=0.7,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    for r in response['choices']:
        print(r['text'])
    return response

@st.cache
def second_grade_mod(text,userPrompt="Summarize this for a second-grade student:"):
    openai.api_key = api_key
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=userPrompt + "\n\n" + text,
    temperature=0.8,
    max_tokens=1350,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    for r in response['choices']:
        print(r['text'])
    return response

@st.cache
def tldr(text,userPrompt="\n\nTl;dr"):
    openai.api_key = api_key
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt= text + userPrompt,
      temperature=0.7,
      max_tokens=1550,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    for r in response['choices']:
        print(r['text'])
    return response

def display_app_header(main_txt, sub_txt, is_sidebar=False):
    """
    Code Credit: https://github.com/soft-nougat/dqw-ivves
    function to display major headers at user interface
    :param main_txt: the major text to be displayed
    :param sub_txt: the minor text to be displayed
    :param is_sidebar: check if its side panel or major panel
    :return:
    """
    html_temp = f"""
    <h2 style = "text_align:center; font-weight: bold;"> {main_txt} </h2>
    <p style = "text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html=True)
    else:
        st.markdown(html_temp, unsafe_allow_html=True)

def divider():
    """
    Sub-routine to create a divider for webpage contents
    """
    st.markdown("""---""")

@st.cache
def second(text,userPrompt="Summarize this for a second-grade student:"):
    return second_grade(text,userPrompt="Summarize this for a second-grade student:")

@st.cache
def tldr_summary(text,userPrompt="\n\nTl;dr"):
    return tldr(text,userPrompt="\n\nTl;dr")

def main():
    st.write("""
    # GPT-3 Text Processing Demo
    """)
    input_help_text = """
    Enter Text
    """
    final_message = """
    The data was successfully analyzed
    """
    text1 = st.text_area(label='INPUT TEXT',placeholder="Enter First Text")
    text2 = st.text_area(label='INPUT TEXT',placeholder="Enter Second Text")
    text3 = st.text_area(label='INPUT TEXT',placeholder="Enter Third Text")

    with st.sidebar:
        # st.markdown("**Processing**")
        # summary1 = st.button(
        #     label="Concise",
        #     help=""
        # )
        summary2 = st.button(
            label="Summarize",
            help=""
        )
    if summary2:
        st.markdown("#### Detailed summary")
        with st.spinner('Wait for it...'):
            # output1 = second_grade(text).get("choices")[0]['text']
            output_first = tldr(text1).get("choices")[0]['text']
            output_second = tldr(text2).get("choices")[0]['text']
            output_third = tldr(text3).get("choices")[0]['text']
            # output = tldr(output1 + output2).get("choices")[0]['text']
            # output = output1 + output2
            output_total = output_first + output_second + output_third
            text_sentences = tokenize.sent_tokenize(output_total)
            for sentence in text_sentences:
                st.write('•',sentence)
    # if summary1:
    #     st.markdown("#### Concise summary")
    #     with st.spinner('Wait for it...'):
    #         output_first = second_grade_mod(text1).get("choices")[0]['text']
    #         output_second = second_grade_mod(text2).get("choices")[0]['text']
    #         output_third = second_grade_mod(text3).get("choices")[0]['text']
    #         # output2 = tldr_summary(text).get("choices")[0]['text']
    #         # output = tldr_summary(output1 + output2).get("choices")[0]['text']
    #         # output = output1 + output2
    #         output_total = output_first + output_second + output_third
    #         text_sentences = tokenize.sent_tokenize(output_total)
    #         for sentence in text_sentences:
    #             st.write('•',sentence)

if __name__ == '__main__':
    main()
