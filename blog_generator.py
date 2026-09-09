import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    response = openai.completions.create( 
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph on the following topic. ' + paragraph_topic, 
        max_tokens=400, 
        #temperature make it so every output is consistent and focused
        temperature=0.3
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog

keep_writting = True

while keep_writting:
    answer = input('do you want to write a paragraph? Y for yes, anything else for no. ')
    if(answer == 'Y'):
        paragraph_topic = input('What should the paragraph talk about? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writting = False
