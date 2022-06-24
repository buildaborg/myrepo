while True:
    print('What is your age?')
    age = input('> ')
    if age.isdecimal():
        break
    print('Please enter a number for your age')
    
while True:
    print('Please enter a value for your password(letters and numebrs only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have numbers or letters')