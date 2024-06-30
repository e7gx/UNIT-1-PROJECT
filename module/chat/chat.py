import openai
from termcolor import colored 
from termcolor import colored
from module.users.users_manger import Employees
from simple_term_menu import TerminalMenu
# Set your OpenAI API key directly. This should ideally be loaded from an environment variable for security reasons.
openai.api_key = 'sk-proj-Lvj3ExQYzUmOEOJhd1xCT3BlbkFJ91b16l8c70Wer1WtY8mX'  

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
        if "goodbye" in user_input.lower() or "exit" in user_input.lower(): 
            break
        conversation.append({"role": "user", "content": user_input})
        response = chat_with_gpt_abdullah(conversation)
        print("\n")
        print(colored("Mr.IT 🤖:    ",'blue'),colored(response, 'green', attrs=['bold']), '\n')
        conversation.append({"role": "system", "content": response})
        
        
        
    def user_manager_menu(self):
        user_manager_menu = [
                "1. Add User 👨🏻‍💻",
                "2. Delete User 🙅🏻‍♂️",
                "3. Display All Users 👀",
                "4. Find User 🔍",
                "5. Exit 🚪"
            ]
    
        quitting = False  # Corrected spelling

        while not quitting:  # More Pythonic way to write `while quitting == False:`
            terminal_menu1 = TerminalMenu(user_manager_menu)
            choice_index1 = terminal_menu1.show()

            print(colored("\n===== Data Analysis Dashboard =====", 'blue', attrs=['bold']))
            
            if choice_index1 == 0:
                self.reg_new_admin()
            elif choice_index1 == 1:
                self.delete_user()
            elif choice_index1 == 2:
                self.get_users()
            elif choice_index1 == 3:
                self.find_user()
            elif choice_index1 == 4:
                print(colored("Exiting the Data Analysis Dashboard...", 'red', attrs=['bold']))
                quitting = True  # Properly set quitting to True to exit the loop
            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))