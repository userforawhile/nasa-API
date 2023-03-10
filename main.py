import streamlit as st
import requests


# prepare API key and api url
api_key = "JfKhN1iAgOvR4tsQviEs3UI4n5x1doiVHtZxZi6K"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# get a request data as dictionary
request = requests.get(url)
data = request.json()

# extract image,data,url,title, and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
