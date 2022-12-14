import openai

file = open('.env','r')

openai.api_key = file.read()

response = openai.Image.create(
  prompt="A cartoon picture of a turtle and a frog sitting at a pond",
  n=1,
  size="1024x1024"
)

print(response)

image_url = response['data'][0]['url']

print(image_url)