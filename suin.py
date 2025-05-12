import streamlit as st

st.title("환영합니다!")
# pip install streamlit
st.subheader("이것은 Streamlit 앱입니다.")
st.code("x=2021")

st.video("https://www.youtube.com/watch?v=_TjwNAXKzyk")

class YouTubeSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search(self, query, max_results=5):
        request = self.youtube.search().list(q=query, part='snippet', maxResults=max_results)
        response = request.execute()