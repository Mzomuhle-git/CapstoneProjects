# This program is for a small business to help users manage tasks
import datetime                     # this includes date and time functionality


def reg_user():             # function for registering a user to the system

    print("Enter a new username and password")
    new_username = input("Enter new username: ")

    user_file = open("user.txt", "r+")              # opening a text file
    for line in user_file.readlines():              # reading file line by line
        line = line.split(",")
        while new_username == line[0]:
            print("The username already exists, choose a new username!")
            new_username = input("username: ")
            if new_username != line[0]:
                break                               # escaping a loop
    user_file.close()

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm the new password: ")

    while confirm_password != new_password:         # iterate until a correct user is entered
        print()
        print("The password does not match!")
        confirm_password = input("Confirm the new password: ")

    new_user_details = new_username + ", " + new_password

    user_file = open("user.txt", "r+")
    for line in user_file.readlines():
        lines = line

    user_file.write("\n")                   # adds a blank line after the last user in user file
    user_file.write(new_user_details)           # writes a new user credentials
    user_file.close()
    print("New user, {} has been added to the system".format(new_username))


def add_task():                 # function for adding a user task

    print()
    username = input("Enter the user name of a person: ")
    task_num = input("Enter the task number e.g.[T###]: ")
    task = input("Enter title of the task: ")
    task_description = input("Enter task description: ")
    due_date = input("Enter the task due date in format [yyyy-mm-dd]: ")
    date_assigned = datetime.date.today()                            # adds today's date
    print("The date assigned is today's date: ", date_assigned)
    task_completed = input("Is the task completed: ")
    print()
    print("Task Successfully added Thank you!")

    tasks_file = open('tasks.txt', 'r+')

    for line in tasks_file.readlines():
        file_contents = line

    # writes tasks belonging to the user onto the tasks file
    tasks_file.write("\n")
    tasks_file.write("{} \nAssigned to:\t\t{} \nTask:\t\t\t{} \nDate assigned:\t\t{} \nDue date:\t\t{} "
                     "\nTask completed:\t\t{} \nTask description:\t{} \n"
                     .format(task_num, username, task, date_assigned, due_date, task_completed, task_description))
    tasks_file.close()


def view_all():                     # function for reading and displaying tasks

    tasks_file = open('tasks.txt', 'r+')

    for line in tasks_file.readlines():
        line = line.strip()  # removing whitespaces after each line
        line = line.replace("\t", "")
        line = line.split(":")
        print('{:20s} : {}'.format(line[0], line[-1]))  # aligning the columns evenly in a user friendly format

    tasks_file.close()


def view_mine():                    # function for each user to view their tasks

    username = input("Enter your username again: ")
    line_num = 0
    num_tasks = 0
    line_list = []

    tasks_file = open("tasks.txt")
    for line in tasks_file.readlines():             # loop finding a task belonging to the logged in user
        line = line.strip()
        line_num += 1
        if line == "Assigned to:\t\t"+username:
            num_tasks += 1
            line_list.append(line_num)
    tasks_file.seek(0)
    print("{} you have {} tasks".format(username, num_tasks))

    line = tasks_file.read()
    line = line.split("\n")
    index = -1
    for b in line_list:
        index += 1
        print()
        x = line[line_list[index]-2:line_list[index]+5]         # slicing tasks belonging to the user
        for a in x:
            print(a)

    tasks_file.close()

    print()
    print("Select an option to continue \n1 - to mark the task as complete \n2 - to edit the task \ne - to exit")
    vm_choice = input(": ")

    if vm_choice == "1":

        line_num2 = 0
        print()
        task_num2 = input("Enter the task number e.g.[T###]: ")

        tasks_file2 = open("tasks.txt", "r+")
        for line in tasks_file2.readlines():
            line = line.strip()
            line_num2 += 1
            if line == task_num2:
                break
        tasks_file2.close()

        tasks_file2 = open("tasks.txt", "r+")
        lines = tasks_file2.readlines()
        tasks_file2.close()
        lines[line_num2 + 4] = "Task completed:\t\tYes\n"

        tasks_file2 = open("tasks.txt", "r+")
        tasks_file2.writelines(lines)
        tasks_file2.close()
        print("The task has been updated")

    elif vm_choice == "2":

        line_num3 = 0
        task_num = input("Enter the task number e.g.[T###]: ")

        tasks_file = open("tasks.txt", "r+")
        for line in tasks_file.readlines():
            line = line.strip()
            line_num3 += 1
            if line == task_num:
                break
        tasks_file.close()

        tasks_file = open("tasks.txt", "r+")
        lines = tasks_file.readlines()
        tasks_file.close()
        del lines[line_num3 - 1:line_num3 + 7]

        tasks_file = open("tasks.txt", "r+")
        tasks_file.truncate(0)
        tasks_file.writelines(lines)
        tasks_file.close()

        username = input("Enter the user name of a person: ")
        task = input("Enter title of the task: ")
        task_description = input("Enter task description: ")
        due_date = input("Enter the task due date in format [yyyy-mm-dd]: ")
        date_assigned = datetime.date.today()  # adds today's date
        print("The date assigned is today's date: ", date_assigned)
        task_completed = input("Is the task completed: ")
        print()
        print("Task Successfully edited, it is located at the bottom now")

        tasks_file = open("tasks.txt", "r+")
        for line in tasks_file.readlines():
            file_contents = line

        # writes tasks  belonging to the user onto the tasks file
        tasks_file.write("\n")
        tasks_file.write("{} \nAssigned to:\t\t{} \nTask:\t\t\t{} \nDate assigned:\t\t{} \nDue date:\t\t{} "
                         "\nTask completed:\t\t{} \nTask description:\t{} \n"
                         .format(task_num, username, task, date_assigned, due_date, task_completed, task_description))
        tasks_file.close()

    elif vm_choice == "e":
        print("You exited the program")


def generate_report():                  # generating reports

    a = 0
    b = 0
    line_num = 1

    task_file = open("tasks.txt", "r+")
    for line in task_file.readlines():
        line = line.strip()
        line_num += 1
        if line == "Task completed:\t\tYes":
            a += 1
        elif line == "Task completed:\t\tNo":
            b += 1
    task_file.close()

    # calculating number of tasks and percentage number of tasks
    num_tasks = line_num / 8
    percent_incomplete = (b/int(num_tasks)) * 100

    # creating and writing on a new file called task overview
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("Total number of tasks: "+str(int(num_tasks)))
        task_overview_file.write("\nTotal completed tasks: "+str(a))
        task_overview_file.write("\nTotal incomplete tasks: "+str(b))
        task_overview_file.write("\nPercentage incomplete tasks {}%".format(round(percent_incomplete)))

    task_overview_file.close()

    user_file = open("user.txt", "r+")
    users = user_file.readlines()
    user_file.close()

    users_list = []
    user_file = open("user.txt", "r+")
    for line in user_file.readlines():
        line = line.split(",")[0]
        users_list.append(line)
    user_file.close()

    task_file = open("tasks.txt", "r+")
    # creating and writing on a new file
    with open("user_overview.Txt", "w") as user_overview_file:

        user_overview_file.write("The total number of users registered: "+str(len(users)))
        user_overview_file.write("\nThe total number of tasks: "+str(int(num_tasks))+"\n")
        user_overview_file.write("\n")

        for a in users_list:
            user_overview_file.write("{:15s}".format(a))

            user_tasks = 0
            percent_tasks = 0
            percent_incomplete = 0
            percent_complete = 0
            percent_overdue = 0
            complete = 0
            incomplete = 0
            overdue = 0
            task_file.seek(0)

            for line in task_file.readlines():
                line = line.strip()
                if line == "Assigned to:\t\t{}".format(a):
                    user_tasks += 1
                    percent_tasks = (user_tasks / int(num_tasks)) * 100
                if line == "Task completed:\t\tYes":
                    complete += 1
                    percent_complete = (complete / int(num_tasks)) * 100
                if line == "Task completed:\t\tNo":
                    incomplete += 1
                    percent_incomplete = (incomplete / int(num_tasks)) * 100
                if line == "Due date:\t\t2021-01-01":
                    overdue += 1
                    percent_overdue = (overdue / int(num_tasks)) * 100
            user_overview_file.write("{:2s} tasks\t\t{:2s} % tasks\t\t{:2s} % incomplete tasks\t\t{:2s} % completed\t\t"
                                     "{:2s} % tasks overdue\n"
                                     .format(str(user_tasks), str(round(percent_tasks)), str(round(percent_incomplete)),
                                             str(round(percent_complete)), str(percent_overdue)))

    task_file.close()
    user_overview_file.close()
    print("The reports have been generated, Thank you")


def display_stats():            # displaying statistics and overview informatin

    print("TASK OVERVIEW \n")
    file1 = open("task_overview.txt", "r")
    for line in file1.readlines():
        contents = line
        print(contents)
    file1.close()

    print("\n")
    print("USER OVERVIEW \n")
    file2 = open("user_overview.txt", "r")
    for line in file2.readlines():
        contents2 = line
        print(contents2)
    file2.close()


#               ****    MAIN PROGRAM   ****

print("Welcome to Task Manager! Please login to continue")
admin_user = "admin, adm1n"
login = False
username = input("Enter username: ")
password = input("Enter password: ")
user_details = username + ", " + password           # making username and password as single

user_file = open('user.txt', 'r+')                  # opening a text file containing user credentials

for line in user_file.readlines():             # for loop to read user details line by line to check if user exists
    line = line.strip()
    if line == user_details:
        login = True

while login is False:                               # while loop iterates until users correct details
    user_file.seek(0)                               # resetting a cursor back to the first line
    print()
    print("The username or password entered did not match our records. \nPlease double-check and try again.")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_details = username + ", " + password

    for line in user_file.readlines():
        line = line.strip()
        if line == user_details:
            login = True

user_file.close()               # closing the file
print()                         # adds a blank line

if login is True:
    print("Login Successful!")
print()

if user_details == admin_user:

    print("Please choose one of the following options to continue:")
    print("r - register user \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports "
          "\nds - display statistics \ne - exit \n")
    option = input("Enter option: ")

else:

    print("Please choose one of the following options to continue:")
    print("a - add task \nva - view all tasks \nvm - view my tasks \ne - exit \n")
    option = input("Enter option: ")

# calling each function according to a selected function
if option == "r":
    reg_user()
elif option == "a":
    add_task()
elif option == "va":
    view_all()
elif option == "vm":
    view_mine()
elif option == "gr":
    generate_report()
elif option == "ds":
    display_stats()
elif option == "e":
    print("You have exited the program, Thank you")
