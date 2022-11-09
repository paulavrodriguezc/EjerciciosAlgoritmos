class Reminder:
    def __init__(self, name, date, time, chores: list):
        self.name=name
        self.date=date
        self.time=time
        self.chores=chores
    def print_reminder(self):
        print(f"Name: {self.name} \nDate: {self.date} \nTime: {self.time}")