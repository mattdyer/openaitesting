run 
	
	python3 -m venv .
	source bin/activate (or equivalent depending on os)
	
	pip install openai
	pip install pyperclip

create .env file in the root with only your openai api key

for putinclipboard.py
	create a folder named cache
	then run python putinclipboard.py {Your Prompt Here}

for chat.py
	create a folder named chats
	then run python chat.py {Conversation_Name} {Your Prompt Here}

Conversation_Name can be any name with letters, numbers and no spaces.  This is used to track the conversation.  If you want to start a new conversation just use a new conversation name.