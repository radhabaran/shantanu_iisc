import faiss
import numpy as np
import pandas as pd
import gradio as gr
from openai import OpenAI
import os
from config.settings import DATA_PATH

# Initialize OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
if not client.api_key:
    raise ValueError("OpenAI API key not found in environment variables")

# Data Loading Function
def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=['title', 'brand', 'description', 'top_review', 'final_price', 'availability'])

# Load Data
data = load_data()

# Handle missing values
data['title'] = data['title'].fillna('')
data['brand'] = data['brand'].fillna('')
data['description'] = data['description'].fillna('')
data['top_review'] = data['top_review'].fillna('')
data['final_price'] = data['final_price'].fillna('N/A')
data['availability'] = data['availability'].fillna('N/A')

# Create combined text
data['combined_text'] = data['title'] + " " + data['brand'] + " " + data['description'] + " " + data['top_review']

# Generate Embeddings
def generate_embeddings(text_list):
    embeddings = []
    for text in text_list:
        try:
            response = client.embeddings.create(
                input=[text],
                model="text-embedding-ada-002"
            )
            embeddings.append(response.data[0].embedding)
        except Exception as e:
            print(f"Error generating embedding for text '{text}': {e}")
    return np.array(embeddings, dtype='float32')

print("Generating embeddings...")
embeddings = generate_embeddings(data['combined_text'].tolist())

# Setup FAISS Index
# dimension = embeddings.shape[1]
dimension = len(embeddings)
print("***** debugging point *********")
print("embeddings :", embeddings)
print("embeddings.shape:",embeddings.shape )
print("dimenesion:", dimension)
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def retrieve(query):
    try:
        response = client.embeddings.create(
            input=[query],
            model="text-embedding-ada-002"
        )
        query_embedding = response.data[0].embedding
        query_embedding = np.array(query_embedding, dtype='float32')
        D, I = index.search(np.array([query_embedding]), k=5)
        
        if len(I[0]) > 0 and I[0][0] != -1:
            return data.iloc[I[0][0]][['title', 'brand', 'description', 'top_review', 'final_price', 'availability']].to_dict()
        return "Sorry, I can't find an answer."
    except Exception as e:
        print(f"Error occurred during retrieval: {e}")
        return f"An error occurred: {e}"

def generate_gpt_response(user_input, product_info):
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant that provides product information."},
            {"role": "user", "content": f"Customer asked: '{user_input}'\nProduct Details:\n- Title: {product_info['title']}\n- Brand: {product_info['brand']}\n- Description: {product_info['description']}\n- Price: {product_info['final_price']}\n- Availability: {product_info['availability']}\n- Top Review: {product_info['top_review']}\nPlease provide a friendly and helpful response."}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"I'm having trouble generating a response right now. Please try again later. (Error: {e})"

def chatbot(input_text, history):
    if history is None:
        history = []
        
    if len(history) > 0:
        last_response = history[-1]
        follow_up_response = generate_gpt_response(input_text, last_response)
        history.append((input_text, follow_up_response))
        return follow_up_response, history

    response = retrieve(input_text)
    if isinstance(response, dict):
        history.append(response)
        gpt_response = generate_gpt_response(input_text, response)
        return gpt_response, history

    history.append((input_text, response))
    return response, history

iface = gr.Interface(
    fn=chatbot, 
    inputs=["text", gr.State()], 
    outputs=["text", gr.State()],
    title="🛍️ ShopWise Bot",
    description="Ask me anything about our products!"
)

iface.launch()

