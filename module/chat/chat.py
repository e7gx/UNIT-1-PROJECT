import os
import openai
from termcolor import colored 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


def chat_with_gpt_abdullah(messages):
    """
    Sends messages to the OpenAI API and returns the GPT-3.5-turbo model's response.

    Parameters:
    messages (list): The conversation history including the user's latest message.

    Returns:
    str: The text of the GPT-3.5-turbo model's response.

    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,  # Adjusts randomness in the response. Closer to 1 means more creative.
        messages=messages  # The conversation history including the user's latest message.
    )
    return response.choices[0].message.content.strip()  # Extracts and returns the text of the response.

def chatgpt_chat():
    """
    Initializes a chat conversation with GPT-3.5-turbo.

    This function allows the user to have a conversation with GPT-3.5-turbo, an AI language model.
    The conversation starts with a system message and continues with alternating user and AI responses.
    The user can exit the chat by typing 'goodbye' or 'exit'.

    Returns:
    None
    """
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    print(colored("You can type 'exit' to end the conversation.\n", 'green', attrs=['bold']))

    while True:
        user_input = input(colored("You:   ", 'white', attrs=['bold']))
        user_input = "User: " + user_input
        if "goodbye" in user_input.lower() or "exit" in user_input.lower(): 
            break
        conversation.append({"role": "user", "content": user_input})
        response = chat_with_gpt_abdullah(conversation)
        print("\n")
        print(colored("Mr.IT 🤖:    ",'blue'),colored(response, 'green', attrs=['bold']), '\n')
        conversation.append({"role": "system", "content": response})
        
        
