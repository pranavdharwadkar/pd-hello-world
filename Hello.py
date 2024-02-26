# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from openai import OpenAI
import json
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Pranav Hello World OpenAI",
        page_icon="👋",
    )
    st.markdown("# Pranav's Sentiment Analysis Demo using Open AI")
    st.write(
    """This app shows how to do Sentiment Analysis using Open AI and Streamlit."""
    )

if __name__ == "__main__":
    run()


def simple_classify(client, input_string: str, prompt_string:str) -> str:

  completion = client.completions.create(model='gpt-3.5-turbo-instruct',
                                         prompt=f"{prompt_string}: {input_string}")
  response=completion.choices[0].text
  print(f"For {input_string}, response is:\n----------{response}\n=============")
  #print(dict(completion).get('usage'))
  #print(completion.model_dump_json(indent=2))
  return response

password=st.text_input("Enter OpenAI Key")
prompt = st.text_input("Enter the prompt:")
user_input = st.text_area("User Input")

if password:
  client = OpenAI(api_key=password)
  print(client.api_key)
  response = simple_classify(client,user_input, prompt)
  st.write(f"response is{response}")


