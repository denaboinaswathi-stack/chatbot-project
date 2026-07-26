import random

responses = {
    "hello": ["Hi!", "Hello! How can I help you?"],
    "python": ["Python is a programming language used for AI and development."],
    "machine learning": ["Machine Learning helps computers learn from data."],
    "ai": ["AI stands for Artificial Intelligence."],
    "bye": ["Goodbye! Have a nice day."]
}


def chatbot(message):
    message = message.lower()

    for key in responses:
        if key in message:
            return random.choice(responses[key])

    return "Sorry, I don't understand."


print("AI Chatbot Started (type bye to exit)")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot(user))
