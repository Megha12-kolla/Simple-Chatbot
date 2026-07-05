name = input("Hello! What's your name? ")

print("Nice to meet you,", name)

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there!")

    elif user == "hi":
        print("Bot: Hello buddy!!")

    elif user == "bye":
        print("Bot: Goodbye! See you later!! 👋")
        break

    elif user == "how are you?":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name?":
        print("Bot: I am a simple Python Chatbot 🤖, so I don't really have a specific name.")

    elif user == "what is your favorite colour?":
        print("Bot: My favorite colour is Red ❤️.")

    elif user == "how old are you?":
        print("Bot: I am so old that even I don't know my age. 😄")

    elif user == "thank you":
        print("Bot: You're welcome! 😊")

    elif user == "who created you?":
        print("Bot: Meghana Kolla created me using Python! 🐍")

    elif user == "tell me a joke":
        print("Bot: Why did the programmer quit his job? Because he didn't get arrays! 😄")

    elif user == "good morning":
        print("Bot: Good morning! Hope you have an amazing day! ☀️")

    else:
        print("Bot: Sorry! I couldn't understand.")