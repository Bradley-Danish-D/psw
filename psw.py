import getpass as p
import pickle as P

try:
    with open('login.dat', 'rb') as f:
        user_info = P.load(f)
except FileNotFoundError:
    user_info = {}

def sign_up():
    # Allow multiple attempts for a unique username
    for _ in range(3):
        username = input("Enter a username: ")
        if username in user_info:
            print("Username already exists. Please try a different username.")
        else:
            password = p.getpass("Enter a password: ")
            user_info[username] = password
            with open('login.dat', 'wb') as f:
                P.dump(user_info, f)
            print("Account created successfully!")
    print("Maximum attempts reached. Sign-up failed.")

def login(username, password):
    if username not in user_info:
        print("Username not found.")
        return False
    elif user_info[username] != password:
        print("Incorrect password.")
        return False
    else:
        print("Login successful!")
        return True
