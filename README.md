Steps to setup:


1. Install openAI package

You can follow the steps here: https://platform.openai.com/docs/api-reference/introduction


2. Add .env file parallel to muse.py location with the following contents:

Generate openAI keys here: https://platform.openai.com/account/api-keys

Add it to .env file inside your muse directory (parallel to muse.py file) using the following line:
OPENAI_API_KEY="add your openAI key here"

note: Do not share your OpenAI API key with anyone! It should remain a secret.
 

3. Add alias in your shell startup script:

alias muse="python -W ignore <location-to-muse-dir>/muse.py"
alias musex="python -W ignore <location-to-muse-dir>/muse.py -model gpt-4-0613" 

note: you can replace python with the python installton you want to use

#END OF INSTRUCTIONS#


You're done.
Open terminal and try: muse "Hello GPT"
