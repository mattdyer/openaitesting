import openai

file = open('.env','r')

openai.api_key = file.read()

response = openai.Completion.create(model="code-davinci-002", temperature=0, prompt="//coldfusion language \n//Hello World", max_tokens=100)

print(response)

print(response['choices'][0]['text'])