import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(
    page_title='CS analyzer',
    layout='wide'
)

st.title('Counter Strike AI Analysis')
st.caption('Ask a question about recent S-tier Counter-Strike match.')

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/query")

prompt = st.text_input(
    'Your prompt',
    placeholder='e.g Which player have the most kills on map de_inferno?',
    help='Type your question and press Enter to get SQL query and results.'
)

if prompt:
    with st.spinner('Generating answer...'):
        try:
            payload={'question': prompt}

            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            result = response.json()

            #st.subheader('Generated SQL query')
            #st.code(result['sql_query'], language='sql')

            if result['error']:
                st.error(f'An error occured: {result['error']}')
            elif result['data']:
                st.subheader('Query Result')

                df = pd.DataFrame(result['data'])
                st.dataframe(df)
            
            else:
                st.info('Query executed successfully, but returned no data.')

        except requests.exceptions.RequestException as e:
            st.error(f'Could not connect to the backend API: {e}')

        except Exception as e:
            st.error(f'An unexpected error occured: {e}') 