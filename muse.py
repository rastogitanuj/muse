import os
import openai
from dotenv import load_dotenv
import requests
import sys
import argparse
import json
import warnings

# Suppress warnings within this scope
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

#keys
load_dotenv() # Load all the ENV variables into your os enviroment.
api_key = os.getenv("OPENAI_API_KEY") # Get your API key from env variable

#url
URL = "https://api.openai.com/v1/chat/completions"

#headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

#parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('prompt')
parser.add_argument('-t', '--temperature', required = False, default = 0.7)
parser.add_argument('-tp', '--top_p', required = False, default = 1)
parser.add_argument('-mt', '--max_tokens', required = False, default = 2048)
parser.add_argument('-n', '--n', required = False, default = 1)
parser.add_argument('-pp', '--presence_penalty', required = False, default = 0.0)
parser.add_argument('-fp', '--frequency_penalty', required = False, default = 0.0)
parser.add_argument('-model', '--model', required = False, default = "gpt-3.5-turbo-16k-0613")
parser.add_argument('-sp', '--sys_prompt', required = False, default = "You are an assitant")
parser.add_argument('-debug', '--debug', required = False, default = False)


args = parser.parse_args()
prompt = args.prompt
temperature = float(args.temperature)
top_p = float(args.top_p)
max_tokens = int(args.max_tokens)
n = int(args.n)
presence_penalty = float(args.presence_penalty)
frequency_penalty = float(args.frequency_penalty)
model = args.model
sys_prompt = args.sys_prompt
debug = args.debug

#model-params:
messages = [{"role": "system", "content": sys_prompt},{"role": "user", "content": f"{prompt}"}]
payload = {"model": model, "messages": messages, "temperature": temperature, "top_p": top_p, "max_tokens": max_tokens, "n": n, "presence_penalty": presence_penalty, "frequency_penalty": frequency_penalty}

if(debug):
    print(f"headers: {headers}, payload: {payload}, messages: {messages}")

response = requests.post(URL, headers=headers, json=payload, verify=False)
if response.status_code == 200:
    content = response.content
    json = json.loads(content)
    gap = ""
    for idx in range(2, n+2):
        reply = json["choices"][idx-2]["message"]["content"]
        print(gap+reply)
        gap = f"-----\nResponse {idx}:\n"
else:
    print("Error. Resposne status code:", response.status_code)
    print("Error content:", response.content)
