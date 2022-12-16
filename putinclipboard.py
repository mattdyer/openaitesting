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

cache_path = 'cache/' + str(prompt_hash) + '.json'

if(not exists(cache_path)):
	
	print('from api')
	
	current_time = datetime.datetime.now()

	file = open('.env','r')

	openai.api_key = file.read()

	response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=400)
	
	response_text = response['choices'][0]['text']
	
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
	
	response_text = response['choices'][0]['text']
	


print(response_text)

pyperclip.copy(response_text)
