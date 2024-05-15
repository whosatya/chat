import random

def greet():
    responses = ["Hi there!", "Hello!", "Hey!", "Greetings!"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Bye!", "Take care!"]
    return random.choice(responses)

def chat():
    print("Chatbot: " + greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + farewell())
            break
        else:
            # You can add more responses or integrate with APIs for more functionality
            print("Chatbot: I'm just a simple chatbot. I don't understand much.")

if __name__ == "__main__":
    chat()
