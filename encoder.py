#Name: Luke Dutrow

def decode(code):
    decoded=""
    for i in range(0,len(code)):
        decoded += str((int(code[i])+7)%10)
    return decoded

def encode_password(password):
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password must be an 8-digit string containing only integers.")
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded_password

def main():
    stored_password = None
    encoded_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            try:
                encoded_password = encode_password(password)
                stored_password = password
                print("Your password has been encoded and stored!")
            except ValueError as e:
                print(e)

        elif option == '2':
            if encoded_password and stored_password:
                print(f"The encoded password is {encoded_password}, and the original password is {stored_password}.")
            else:
                print("No password has been encoded yet.")

        elif option == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
