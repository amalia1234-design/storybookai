from openai import OpenAI
import google.generativeai as genai 
from google.colab import userdata 
from IPython.display import Image 
import streamlit as st
import os 

client = OpenAI(
    api_key=os.environ["OPENAI_SECRET_KEY"] 
)
GOOGLE_API_KEYS = userdata.get('GOOGLE_API_KEYS')
genai.configure(api_key=GOOGLE_API_KEYS)

def story_ai(msg, syspromt):
  story_response = client.chat.completions.create(
      model="gpt-4o",
      messages=
       [
          {

              "role":
              "system", "content":sysprompt
              },
          {
              "role":
           "user", "content": msg

              }], 

      max_tokens = 300

  )

  story = story_response.choices[0].message.content 
  return story


sysprompt= """ 
Your are a bestselling author. You will take in  a user's request and create a 100 words short story. 
The story should be suitable for children ages 7-9.  

"""

story_ai("write a story about Sang Kancil",sysprompt)

def art_ai(msg): 
  art_response = client.images.generate(
      model = "dall-e-2", 
      prompt = msg, 
      size = "1024x1024",
      n = 1
  )

  art = art_response.data[0].url
  return art

def design_ai(msg): 
      design_model = genai.GenerativeModel('gemini-1.5-flash')
      design = design_model.generate_content(["""

      creaft a fitting promt for an AI iamge generator 
      to generate a most fitting cover art for this story:
      {msg}
      """])
      return design.text

def storybook_ai(msg,sysprompt):
    story = story_ai(msg,sysprompt)
    art = art_ai(story)
    st.image(art)
    st.write(story)

def main(): 
msg = st.text_input("What story that do you want to make")
if = st.button("Generate story"):
storybook_ai(msg,sysprompt)

if __name__ == "__main__":
    main()