def chat_with_bot():
    print(" Bot: Hey there! I'm ChatterPy, your friendly Python chatbot!")
    print("You can talk to me by typing things like:")
    print("- hello")
    print("- how are you")
    print("- what's your name")
    print("- tell me a joke")
    print("- bye")
    print("Type 'exit' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Bot: Hello! Nice to meet you! ")
        elif user_input == "how are you":
            print("🤖 Bot: I'm feeling awesome!!! thanks for asking!")
        elif user_input == "what's your name":
            print("🤖 Bot: I'm ChatterPy! I'm made of pure Python ")
        elif user_input == "tell me a joke":
            print("🤖 Bot: Why did the Python go to school? To improve its 'byte'-sized knowledge! 😂")
        elif user_input == "bye":
            print("🤖 Bot: See you next time! Stay curious. ")
        elif user_input == "exit":
            print("🤖 Bot: Chat ended. Goodbye human!")
            break
        else:
            print("🤖 Bot: Hmm... I didn't get that. Try saying something else!")

# Start the chatbot
chat_with_bot()