import os
import openai

openai.api_key = "API KEY AS STRING"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
while True:
    ques=input('Enter the query: ')
    if ques == 'quit':
        print('Process ended...')
        break
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ques,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
    print(response["choices"][0]['text'])

