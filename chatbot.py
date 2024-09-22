def banking_chatbot():
    print("Welcome to BankingBot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("BankingBot: Thank you for using our services. Goodbye!")
            break
        elif "balance" in user_input:
            print("BankingBot: Your current account balance is $1,000.")
        elif "open account" in user_input:
            print("BankingBot: You can open a new account by visiting our website or nearest branch.")
        elif "loan" in user_input:
            print("BankingBot: We offer personal, home, and car loans. For more details, visit our loans page.")
        elif "help" in user_input:
            print("BankingBot: How can I assist you? You can ask about your balance, opening an account, transfering funds or loans.")
        elif "transfer" in user_input:
            print("BankingBot: 1. Log in to your online banking.\n2. Go to Transfers.\n3. Select accounts and enter transfer details.\n4. Review and confirm the transfer.\n5. Check transfer status.")
        else:
            print("BankingBot: I'm sorry, I don't understand that. Please ask something else.")

banking_chatbot()