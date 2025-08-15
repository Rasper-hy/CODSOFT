# Simple Rule-Based Chatbot

print("Chatbot: Hi! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello there! How can I help you today?")

    elif "how are you" in user_input:
        print(
            "Chatbot: I'm just a bunch of code, but I'm feeling great! How about you?"
        )

    elif "your name" in user_input:
        print("Chatbot: You can call me RuleBot.")

    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day.")
        break

    else:
        print("Chatbot: Sorry, I didn’t understand that. Can you rephrase?")
