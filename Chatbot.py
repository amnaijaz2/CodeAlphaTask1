def chatbot():
    print("Welcome to the MiniChatbot")
    print("Type 'bye' to exit")
   
    while True:
        user_input = input("\nYou: ").lower().strip()
        
        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi there!")
        elif user_input == "how are you":
            print("Bot: I'm doing great, thanks for asking! How about you?")
        elif user_input == "by" or user_input == "goodby":
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I don't understand that yet.")
    
    print("\nChat ended. Thanks for chatting!")
        
chatbot()