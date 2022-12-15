import openai
import uuid
import datetime
 
current_time = datetime.datetime.now()

file = open('.env','r')

openai.api_key = file.read()

prompt = 'Generate a sql insert statement for 10 rows in a table containing First Name, Last Name, Address, Phone, Username columns'

response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=400)

print(response)

filename = str(uuid.uuid4()) + '.txt'

result = open('results/' + filename, 'w')

result.write(str(current_time) + '\n')
result.write(prompt)
result.write(response['choices'][0]['text'])

result.close()

#Write a paragraph about labrador retreivers in the style of Edgar Allen Poe: The Labrador Retriever is a breed of canine that is shrouded in mystery and intrigue. Its origins are unknown, yet its presence is unmistakable. Its coat is a deep, glossy black, and its eyes are a piercing, soulful brown. Its demeanor is gentle and loyal, and its intelligence is unparalleled. It is a breed that is beloved by many, and its loyalty and companionship are unmatched. It is a breed that is sure to capture the hearts of all who encounter it

#Write a paragraph about border collies in the style of Edgar Allen Poe: The border collie is a creature of mystery and intrigue, its eyes a deep, dark abyss that seem to peer into the depths of one's soul. Its fur is a soft, silky black, with white markings that seem to dance in the moonlight. Its agility and intelligence are unmatched, and its loyalty is unparalleled. It is a creature of beauty and grace, and its presence is a reminder of the power of nature.

#Who is your daddy and what does he do?: My dad is John and he is a software engineer.