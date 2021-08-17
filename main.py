# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choice = input("Choose Login or New User")

    if choice == "Login":
        d = {}
        with open('passwords.txt') as f:
            for line in f:
                (key, val) = line.split()
                d['key'] = val

        username = input("Enter Username")
        password = input("Enter Password")


    else:
        username = input("Enter Username")
        password = input("Enter Password")
        lines = [username, password]
        with open('passwords.txt', 'a') as f:
            for line in lines:
                f.write(line)
                f.write(" ")
            f.write('\n')

        print("Run the program again to login to the system")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
