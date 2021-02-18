print('''
Welcome to the Car Game!
    Enter 'help' to begin!
    ''')

user_input = ""

while user_input != "quit":
    user_input = input('> ').lower()
    if user_input == "start":
        print('Car started... Ready to go!')
    elif user_input == "stop":
        print('Car stopped.')
    elif user_input == "quit":
        print('Goodbye!')
    elif user_input == "help":
        print('''
            Enter:
            start - to start the car
            stop - to stop the car
            quit - to exit
        ''')
    else:
        print("I don't understand...")

