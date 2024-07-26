import requests
import streamlit as st

def search_wikipedia(query):
    """
    Search Wikipedia for the given query and return the summary of the top result.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
    response = requests.get(url)
    data = response.json()
    
    if data['query']['search']:
        title = data['query']['search'][0]['title']
        page_id = data['query']['search'][0]['pageid']
        snippet = data['query']['search'][0]['snippet']
        
        # Get the full content of the top search result
        content_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={page_id}&exintro=&format=json"
        content_response = requests.get(content_url)
        content_data = content_response.json()
        
        page_content = content_data['query']['pages'][str(page_id)]['extract']
        
        return {
            'title': title,
            'snippet': snippet,
            'content': page_content
        }
    else:
        return None

# Streamlit App
st.title("Search Bot")
st.write("Enter a search query to get information from Wikipedia.")

query = st.text_input("Search Query")

if query:
    result = search_wikipedia(query)
    if result:
        st.subheader(result['title'])
        st.write(result['snippet'])
        st.markdown(result['content'], unsafe_allow_html=True)
    else:
        st.write("No results found.")
