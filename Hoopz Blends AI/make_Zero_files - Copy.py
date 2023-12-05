# Import necessary libraries (if needed)
import random  # For randomizing responses

# Define a function to handle user queries
def chatbot_response(user_query):
    responses = {
        "what do you do": "I am an AI designed to assist with various tasks.",
        "who are you": "I am an AI chatbot programmed to help users.",
        "what do you do": "I am an AI  Assistant called Zero and  programmed to help users.",
        # Add more queries and their corresponding responses as needed
    }

    # Check if the user's query matches any predefined responses
    return responses.get(user_query.lower(), "I'm sorry, I don't understand that question.")

# Example usage
if __name__ == "__main__":
    user_question = input("You: ")  # Get user input
    bot_response = chatbot_response(user_question)  # Get chatbot response
    print(f"Zero: {bot_response}")  # Display the bot's response

def chatbot_response(user_query):
    bot_name = "Zero"  # Assign the name to the bot

    responses = {
        "what do you do": f"I am {bot_name: Zero}, an AI designed to assist with various tasks.",
        "who are you": f"I am {bot_name: Zero}, an AI chatbot programmed to help users.",
        # Add more queries and their corresponding responses as needed
    }

    # Check if the user's query matches any predefined responses
    return responses.get(user_query.lower(), f"I'm sorry, {bot_name:Zero} doesn't understand that question.")

def chatbot_response(user_query):
    bot_name = "Zero"

    responses = {
        "what is your purpose": f"My purpose is to assist users with various tasks as {bot_name}.",
        "do you know yourself": f"I am {bot_name}, an AI chatbot designed to learn and assist users.",
        "what can you do": f"I can perform various tasks such as providing information, performing calculations, and more.",
        # Add more queries and their corresponding responses as needed
    }

    return responses.get(user_query.lower(), f"I'm sorry, {bot_name} doesn't understand that question.")
