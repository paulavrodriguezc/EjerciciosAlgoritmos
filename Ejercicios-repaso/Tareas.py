class Chore:
    def __init__(self, activities: list):
        self.activities=activities
    def print_chore(self):
        for activity in self.activities:
            print(f"*Activity: {activity}")
        print("\n")
    def modify_chore(self):
        number_activity=0
        choice=input("Do you wish to add or to delete an activity? \n*A for add \n*D for delete \n---> ").capitalize()
        while not choice in ["A","D"]:
            choice=input("Invalid input. Do you wish to add or to delete an activity? \n*A for add \n*D for delete \n---> ").capitalize()
        for activity in self.activities:
            index=self.activities.index(activity)
            number_activity+=1
            print(f"*Activity {number_activity}: {activity}")
        for activity in self.activities:
            if choice=="A":
                while adding:
                    chore=input("Please enter the activity you would like to be reminded to do: ")
                    self.activities.append(chore)
                    if input("Do you wish to add another activity to complete? \n1. for yes \n2. for no \n---> ")=="2":
                        adding=False
            else:
                activity_selected=input("Enter the number of the activity you wish to delete: ")
                while not activity_selected.isnumeric():
                    activity_selected=input("Invalid input. Enter the number of the activity you wish to delete: ")
                if (number_activity-1)==index:
                    self.activities.remove(activity)