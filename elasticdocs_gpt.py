import os
import streamlit as st
import openai
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key and GPT model
openai.api_key = os.environ['openai_api']
model = "gpt-3.5-turbo-0301"

# Connect to Elastic Cloud cluster
def es_connect(cid, user, passwd):
    es = Elasticsearch(cloud_id=cid, http_auth=(user, passwd))
    return es

# Search ElasticSearch index and return body and URL of the result
def search(query_text):
    cid = os.environ['cloud_id']
    cp = os.environ['cloud_pass']
    cu = os.environ['cloud_user']
    es = es_connect(cid, cu, cp)

# Elasticsearch query (BM25) and kNN configuration for hybrid search
    query = {
        "bool": {
            "must": [{
                "match": {
                    "title": {
                        "query": query_text,
                        "boost": 1
                    }
                }
            }],
            #filtering for place-vector field does not work
            # "filter": [{
            #     "exists": {
            #         "field": "elastic-docs_title-vector"
            #     }
            # }]
        }
    }
    # kNN query does not work
    # knn = {
    #     "field": "elastic-docs_title-vector",
    #     "k": 1,
    #     "num_candidates": 20,
    #     "query_vector_builder": {
    #         "text_embedding": {
    #             "model_id": "sentence-transformers__all-distilroberta-v1",
    #             "model_text": query_text
    #         }
    #     },
    #     "boost": 24
    # }

    fields = ["title", "body_content", "url"]
    index = 'search-expatistan'
    resp = es.search(index=index,
                    query=query,
                    # knn=knn, # kNN query does not work
                    fields=fields,
                    size=1,
                    source=False)

    # Handle the case when there are no hits in the response
    if resp['hits']['hits']:
        body = resp['hits']['hits'][0]['fields']['body_content'][0]
        url = resp['hits']['hits'][0]['fields']['url'][0]
    else:
       body = None
       url = None

    # Return the body and URL of the result
    return body, url

# Truncate text to fit within the model's context length
def truncate_text(text, max_tokens):
    tokens = text.split()
    if len(tokens) <= max_tokens:
        return text

    return ' '.join(tokens[:max_tokens])

# Generate a response from ChatGPT based on the given prompt
def chat_gpt(prompt, model="gpt-3.5-turbo", max_tokens=1024, max_context_tokens=4000, safety_margin=5):
    # Truncate the prompt content to fit within the model's context length
    truncated_prompt = truncate_text(prompt, max_context_tokens - max_tokens - safety_margin)
    response = openai.ChatCompletion.create(model=model,
                                            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": truncated_prompt}])
    return response["choices"][0]["message"]["content"]

# Set page CSS styles
with open('./css/elastic-styles.css') as f: 
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Set page title/banner
st.title("Explore Away")

# Offer prompt suggestions
with st.chat_message("assistant"):
    st.write('''Prompt suggestions:  
            'I want to go to Italy for 2 months while I work for a company in Miami.'  
            'What do I need to know as a tech nomad from USA working in Mexico.'  
            'How much could it cost to live and work in Morocco for 6 months' ''')

# Initialize chat history ## does not work
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun ## does not work
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Main chat form
with st.form("chat_form"):
    query = st.text_input("You: ")
    submit_button = st.form_submit_button("Send")

# Generate and display response on form submission
negResponse = "I'm unable to answer the question based on the information I have from Nomadiq."
if submit_button:
    resp, url = search(query)
    prompt = f"Answer this question: {query}\nUsing only the information from this Nomadiq Doc: {resp}\nIf the answer is not contained in the supplied doc reply '{negResponse}' and nothing else"
    answer = chat_gpt(prompt)
    
    # if no response
    if negResponse in answer:
        st.write(f"ChatGPT: {answer.strip()}")
    else:
        st.write(f"ChatGPT: {answer.strip()}\n\nDocs: {url}")
