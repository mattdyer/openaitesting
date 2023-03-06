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

prompt = " ".join(args)

print(prompt)

prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()

cache_path = 'cache/' + 'chat_' + str(prompt_hash) + '.json'

if(not exists(cache_path)):
	
	print('from api')
	
	current_time = datetime.datetime.now()

	file = open('.env','r')

	openai.api_key = file.read()

	
	
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": prompt}
		]
	)
	
	response_text = response['choices'][0]['message']['content']
	
	json_response = json.dumps(response)
	
	saved_response = open(cache_path, 'w')
	
	saved_response.write(json_response)
	
	filename = str(uuid.uuid4()) + '.txt'

	result = open('results/' + filename, 'w')

	result.write(str(current_time) + '\n')
	result.write(prompt)
	result.write(response_text)

	result.close()
	
else:
	
	print('from cache')
	
	saved_response = open(cache_path, 'r')
	
	json_response = saved_response.read()
	
	response = json.loads(json_response)
	
	response_text = response['choices'][0]['message']['content']
	


print(response_text)

pyperclip.copy(response_text)
