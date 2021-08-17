
if __name__ == '__main__':
    choice = input("Choose Login or New User: ")  # prompt user choice

    # if user has login credentials
    if choice == "Login":
        d = {} # creating database
        # opening text file and reading saved login information
        with open('passwords.txt') as f:
            for line in f:
                key, val = line.split()
                d[key] = val

        # prompting user credentials
        print("Enter Login Information")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        # Testing the dictionary for username and password combo
        for i in d.keys():
            if username == i:
                while password != d.get(i):
                    password = input("Password incorrect")
                break
        print("Verified User")

    # If user needs to create credentials
    else:
        print("Creating New User")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        lines = [username, password] # storing new username and password
        # adding the new username and password to text file database
        with open('passwords.txt', 'a') as f:
            for line in lines:
                f.write(line)
                f.write(" ")
            f.write('\n')

        # Temporary until making the system continuous
        print("Run the program again to login to the system")

