import datetime

#PART A

# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters and numbers)
#             (3) the last character must be a number
# output:     boolean (True if valid, False if invalid)
def valid_username(string):
    char_length = False
    is_alphanum = False
    last_is_num = False
    #is not an empty string
    if not string:
        return False
    # must be 5 characters or longer
    if len(string)>=5:
        char_length = True

    # must be alphanumeric
    for char in string:
        if char.isalnum:
            is_alphanum = True

    #last character must be a number
    if string[-1].isdigit():
        last_is_num = True
    return char_length and is_alphanum and last_is_num

# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 6 characters or longer
#             (2) must not contain any numbers
#	          (3) at least one letter must be lower case and one upper case
# output:     boolean (True if valid, False if invalid)
def valid_password(password):
    char_length = False
    is_not_num = False
    one_upper = False
    one_lower = False

    # is not an empty string
    if not password:
        return False
    # must be 6 characters or longer
    if len(password) >= 6:
        char_length = True
    # must not contain any numbers
    for char in password:
        if not char.isdigit():
            is_not_num = True
    # one lowercase letter
    for char in password:
        if not char.isupper():
            one_upper = True
    # one uppercase letter
    for char in password:
        if not char.islower():
            one_lower = True
    return char_length and is_not_num and one_lower and one_upper
#PART B

#create the file
write_file = open("user_info.txt", "w")
write_file.write(f"Pikachu1,Abcdef\nCharmander3,XyzaBc\nSquirtle1,SquirtleSquad\n20Pidgey20,PqrPqr$$$\nFerow100,Pidgey")
write_file.close()


# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)
def username_exists(username):
      try:
        # Open the file for reading
        user_file = open("user_info.txt", "r")

      except FileNotFoundError:
        print(f"Error: File user_info.txt not found.")
      else:
          # Read all lines into a list
          lines = user_file.readlines()

          # for loop that checks each line in index 0 (usernames)
          for line in lines:
              all_values = line.strip().split(",")
              if all_values[0] == username:
                  return True
          else:
              return False



# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)
def check_password(username, password):
    try:
        # Open the file for reading
        user_file = open("user_info.txt", "r")

    except FileNotFoundError:
        print(f"Error: File user_info.txt not found.")
    else:
        # Read all lines into a list
        lines = user_file.readlines()

        # for loop that checks each line in index 0 (usernames)
        for line in lines:
            all_values = line.strip().split(",")
            if all_values[0] == username and all_values[1]== password:
                return True
        else:
            return False


#PART C

# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)
def add_user(username, password):
    if not username_exists(username):
        add_to_file = open("user_info.txt", "a")
        add_to_file.write(f"\n{username},{password}")
        add_to_file.close()
        return True
    else:
        return False


#PART D

# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given user
#             with the following information:
#
#             sender|date_and_time|message\n
#
# output:     nothing
def send_message(sender, recipient, message):

    # Get current date and time
    d = datetime.datetime.now()
    formatted_date = f"{d.month:02d}/{d.day:02d}/{d.year}"
    formatted_time = f"{d.hour:02d}:{d.minute:02d}:{d.second:02d}"

    # Create message content
    msg_content = f"{sender}|{formatted_date} {formatted_time}|{message}\n"

    # open the files under append and write the messages down
    try:
        user_msg = open(f"messages/{recipient}.txt", "a")
    except FileNotFoundError:
        print(f"Error: Could not open file '{recipient}.txt'.")
    else:
        #write down messages
        user_msg.write(msg_content)
        user_msg.close()


#PART E

# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.
# output:     no return value (simply prints the messages)
def print_messages (username):
    #make sure the file can be opened
    try:
        user_file = open(f"messages/{username}.txt", "a")
    except FileNotFoundError:
        print(f"Error: Could not open file '{username}.txt'")
    else:
        #close append file and open read file so error does not occur
        user_file.close()
        user_file = open(f"messages/{username}.txt", "r")
        #read each line
        all_messages = (user_file.readlines())
        if all_messages:
            #format for message numbers
            msg_counter = 0
            for message in all_messages:
                msg_counter += 1
                #strip new line and split username time and message
                user_time_msg = message.strip("\n").split("|")
                print(f"Message #{msg_counter} received from {user_time_msg[0]}")
                print(f"Time: {user_time_msg[1]}")
                print(f"{user_time_msg[2]} \n")
            user_file.close()
        else:
            #if there is nothing in the file
            print("no messages in your inbox")


# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value
def delete_messages(username):
    open_msgs = open(f"messages/{username}.txt", "w")
    #write blank txt over previous text
    open_msgs.write("")
    open_msgs.close()


#PART F

#welcome message
print(f"Welcome to our new Messaging System!!! \n What would you like to do?")
while True:
    user_start = input("(l)ogin, (r)egister, or (q)uit: ").lower()
    #if user chooses to log in
    if user_start == "l":
        print("Log In")
        username = input("Username: ")

        #check to see if username exists
        if username_exists(username):
            password = input("Password: ")

            #if username exists check if the password is valid
            if check_password(username, password):
                print("Login successful")
                print(f"--------------------------------------------------------------------------------------\n")
                while True:
                    rsdl_msgs = input(f"Would you like to: \n (r)ead messages, (s)end a message, (d)elete messages, or (l)og out: ")
                    #user chooses to read their messages
                    if rsdl_msgs == "r":
                        print(f"--------------------------------------------------------------------------------------\n")
                        print_messages(username)
                        #print a line to separate different steps
                        print(f"\n--------------------------------------------------------------------------------------\n")
                        continue
                    #user chooses to send a message to another user and go back homepage after
                    elif rsdl_msgs == "s":
                        print(f"--------------------------------------------------------------------------------------\n")
                        recepient = input("Username of recipient: ")
                        #make sure user exists and then send message
                        if username_exists(recepient):
                            message = input("Type your message:")
                            send_message(username, recepient, message)
                            # print a line to separate different steps
                            print(f"--------------------------------------------------------------------------------------\n")
                            continue
                        #recipient username does not exist
                        else:
                            print("unknown recipient")
                            print(f"--------------------------------------------------------------------------------------\n")
                            continue
                    elif rsdl_msgs == "d":
                        print(f"--------------------------------------------------------------------------------------\n")
                        delete_messages(username)
                        print("Your messages have been deleted.")
                        # print a line to separate different steps
                        print(f"--------------------------------------------------------------------------------------\n")
                        continue
                    elif rsdl_msgs == "l":
                        print(f"--------------------------------------------------------------------------------------\n")
                        print("logging out...")
                        break
                    else:
                        print("Invalid entry.")
            else:
                print("Incorrect password. Login failed.")
                # print a line to separate different steps
                print(f"--------------------------------------------------------------------------------------\n")
                continue

        #if username does not exist, login fails
        else:
            print("Unknown username. Login failed.")

    #user chooses to register
    elif user_start == "r":
        print("Register for an account: ")
        username = input("Username (case sensitive): ")
        #check to see if username exists
        if username_exists(username):
            print("Duplicate username, registration cancelled.")
            # print a line to separate different steps
            print(f"--------------------------------------------------------------------------------------\n")
            continue
        else:
            #check to see if new username is valid
            if valid_username(username):
                #prompt user for a password
                password = input("Password (case sensitive): ")
                #check if password is valid
                if valid_password(password):
                    #if password is valid, add login to user info
                    try:
                        add_info = open("user_info.txt", "a")
                    except FileNotFoundError:
                        print("File not found")
                        print(f"--------------------------------------------------------------------------------------\n")
                        continue
                    else:
                        add_info.write(f"\n{username},{password}")
                        add_info.close()
                        print("Registration successful")
                        # print a line to separate different steps
                        print(f"--------------------------------------------------------------------------------------\n")
                        continue
                else:
                    print("Password is invalid, registration cancelled.")
                    print("Password Requirements:")
                    print("- Must be 6 characters or longer.")
                    print("- Must not contain any numbers.")
                    print("- Must contain at least one lowercase letter and one uppercase letter.")

                    # print a line to separate different steps
                    print(f"--------------------------------------------------------------------------------------\n")
                    continue
            #if username is invalid, restart the program
            else:
                print("Username is invalid, registration cancelled.")
                print("Username Requirements:")
                print("- Must be 5 characters or longer.")
                print("- Must be alphanumeric (only letters and numbers).")
                print("- The last character must be a number.")

                # print a line to separate different steps
                print(f"--------------------------------------------------------------------------------------\n")
                continue

    #user chooses to quit the program
    elif user_start == "q":
        break
    else:
        print("Invalid entry, try again.")
