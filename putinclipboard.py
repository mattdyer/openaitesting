import openai
import uuid
import datetime
import pyperclip
import sys

args = sys.argv

del args[0]

print(args)

prompt = " ".join(args)

print(prompt)

current_time = datetime.datetime.now()

file = open('.env','r')

openai.api_key = file.read()

response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=400)

print(response)

response_text = response['choices'][0]['text']

filename = str(uuid.uuid4()) + '.txt'

result = open('results/' + filename, 'w')

result.write(str(current_time) + '\n')
result.write(prompt)
result.write(response_text)

result.close()

pyperclip.copy(response_text)
