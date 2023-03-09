import openai
import uuid
import datetime
import pyperclip
import sys
import json
import hashlib
from os.path import exists

args = sys.argv

del args[0]

chat_id = args[0]

del args[0]

prompt = " ".join(args)

print(prompt)

prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()

chat_path = 'chats/' + chat_id + '.json'

cache_path = 'cache/' + 'chat_' + str(prompt_hash) + '.json'

if(exists(chat_path)):
	chat_log_file = open(chat_path,'r')
	
	chat_log = json.loads(chat_log_file.read())
else:
	chat_log = [
		{"role": "system", "content": "You are a helpful assistant."}
	]

current_time = datetime.datetime.now()

file = open('.env','r')

openai.api_key = file.read()

chat_log.append({"role": "user", "content": prompt})

response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=chat_log
)

response_text = response['choices'][0]['message']['content']

print(response['usage']['total_tokens'])

chat_log.append({"role": "assistant", "content": response_text})

chat_log_archive = json.dumps(chat_log)

saved_archive = open(chat_path, 'w')

saved_archive.write(chat_log_archive)

saved_archive.close()
	
	
	
print(response_text)

#pyperclip.copy(response_text)
