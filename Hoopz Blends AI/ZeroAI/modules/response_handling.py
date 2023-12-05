import speech_recognition as sr
import pyttsx3

# Initialize recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

def speak(response):
    engine.say(response)
    engine.runAndWait()

# Usage
user_input = listen()
print("User said:", user_input)

# Example response
response = "Hello! How can I assist you?"
speak(response)


import random  # For selecting random responses

# Function to handle text inputs
# Function to handle text inputs
def text_input():
    return input("Type your query: ").lower()  # Example: Accepting text input from the console

# Function to handle text output
def text_output(response):
    print("Zero AI:", response)  # Example: Displaying responses as text in the console

# Function to retrieve current time
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")  # Example: Returns the current time

# Function to solve equations (Example: using sympy library)
from sympy import sympify, solve, symbols

def solve_equation(equation):
    x = symbols('x')
    try:
        eq = sympify(equation)
        solution = solve(eq, x)
        return solution
    except:
        return "Sorry, I couldn't solve that equation."

# Continuous loop for voice and text interaction
while True:
    user_input = listen() if voice_input else text_input()  # Listen for voice or accept text input

    # Rest of the logic remains unchanged
    print("User said/typed:", user_input)

    # Responses to casual inquiries or small talk
    casual_inquiries = ["how are you", "how you doing", "what's up"]
    if any(inquiry in user_input for inquiry in casual_inquiries):
        responses = [
            "I'm functioning optimally, thank you for asking!",
            "I'm doing well, thanks.",
            "All systems operational, thank you!"
        ]
        response = random.choice(responses)

    # Responses to time-related queries
    elif "time" in user_input:
        response = f"The current time is {get_current_time()}."

    # Responses to solving equations
    elif "solve" in user_input:
        equation = user_input.replace("solve", "").strip()
        response = solve_equation(equation)

    # Process user input and generate responses accordingly
    # ... (rest of the response generation logic)

    # Speak or output response based on the input type
    if voice_input:
        speak(response)  # Speak response for voice input
    else:
        text_output(response)  # Display response as text for text input
