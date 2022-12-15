import openai
import uuid
import datetime

current_time = datetime.datetime.now()

file = open('.env','r')

openai.api_key = file.read()

prompt = "4 color pixel art of a dinosaur"

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="256x256"
)

print(response)

image_url = response['data'][0]['url']

print(image_url)

filename = str(uuid.uuid4()) + '.txt'

result = open('images/' + filename, 'w')

result.write(str(current_time) + '\n')
result.write(prompt + '\n')
result.write(image_url)

result.close()