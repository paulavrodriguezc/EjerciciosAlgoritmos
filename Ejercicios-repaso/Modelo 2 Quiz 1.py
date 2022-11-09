from Recordatorios import Reminder
from Tareas import Chore
def validate_option(option: str):
    while not option.isnumeric() or not option in ["1","2","3","4","5"]:
        option=input("Invalid input. Please select one option from the following: \n1. Create a reminder \n2. Delete a reminder \n3. Update a reminder \n4. Show all reminders \n5. Exit \n---> ")
    return int(option)
def greet_and_menu():
    print("Welcome to our app!")
    option=input("Please select one option from the following: \n1. Create a reminder \n2. Delete a reminder \n3. Update a reminder \n4. Show all reminders \n5. Exit \n---> ")
    option=validate_option(option)
    return option
def make_reminder(reminder_list: list):
    adding=True
    chores_list=[]
    name=input("Please enter the name of the reminder you wish to create: ")
    date=input("Please enter the date of the reminder in this format (DD/MM): ")
    time=input("Please enter the time of the day for the reminder in this format (10:00): ")
    while adding:
        chores=input("Please enter the activity you would like to be reminded to do: ")
        chores_list.append(chores)
        if input("Do you wish to add another activity to complete? \n1. for yes \n2. for no \n---> ")=="2":
            adding=False
    reminder_list.append((Reminder(name, date, time, Chore(chores_list))))
def show_reminders(reminder_list: list):
    reminder_number=0
    for reminder in reminder_list:
        reminder_number+=1
        print(f"*Reminder #{reminder_number}: ")
        reminder.print_reminder()
        reminder.chores.print_chore()
def delete_reminder(reminder_list: list):
    reminder_deleted=input("Please enter the number of the reminder you wish to delete: ")
    while not reminder_deleted.isnumeric():
        reminder_deleted=input("Invalid input. Please enter the number of the reminder you wish to delete: ")
    reminder_deleted=int(reminder_deleted)-1
    for reminder in reminder_list:
        index=reminder_list.index(reminder)
        if reminder_deleted==index:
            reminder_list.remove(reminder)
def change_reminder(reminder_list: list):
    reminder_modified=input("Please enter the number of the reminder you wish to modify: ")
    while not reminder_modified.isnumeric():
        reminder_modified=input("Invalid input. Please enter the number of the reminder you wish to modify: ")
    reminder_modified=int(reminder_modified)-1
    for reminder in reminder_list:
        index=reminder_list.index(reminder)
        if reminder_modified==index:
            data=select_information()
            if data=="Name":
                reminder.name=input("Please enter the new name of the reminder: ")
            elif data=="Date":
                reminder.date=input("Please enter the new date of the reminder in this format (DD/MM): ")
            elif data=="Time":
                reminder.time=input("Please enter the new time of the day for the reminder in this format (10:00): ")
            else:
                reminder.chores.modify_chore()
def select_information():
    information=input("Please select the option of the data you wish to modify: \n1. Name \n2. Date \n3. Time \n4. Activities \n---> ")
    while not information.isnumeric() or not information in ["1","2","3","4"]:
        information=input("Please select the option of the data you wish to modify: \n1. Name \n2. Date \n3. Time \n4. Activities \n---> ")
    if information=="1":
        information="Name"
    elif information=="2":
        information="Date"
    elif information=="3":
        information="Time"
    else:
        information="Activities"
    return information
def main():
    continuing=True
    reminder_list=[]
    while continuing:
        option=greet_and_menu()
        if option==1:
            make_reminder(reminder_list)
        elif option==2:
            show_reminders(reminder_list)
            delete_reminder(reminder_list)
        elif option==3:
            show_reminders(reminder_list)
            change_reminder(reminder_list)
        elif option==4:
            show_reminders(reminder_list)
        elif option==5:
            print("Thank you for preferring us. Have a nice day!")
            continuing=False
main()