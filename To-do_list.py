from datetime import datetime, timedelta

class Activity:
    def __init__(self, title, description, due_date):
       
        self.title = title
        self.description = description
        self.due_date = due_date

    def print_activity(self):

        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")


class Day:
    def __init__(self, date):

        self.date = date
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def print_activities(self):
        print(f"Activities for {self.date}:")
        for activity in self.activities:
            activity.print_activity()
            print("-" * 20)

class Month:
    def __init__(self, name, year):

        self.name = name
        self.year = year
        self.days = {}

    def add_activity(self, day, activity):

        if day not in self.days:
            self.days[day] = Day(f"{self.year}-{self.name}-{day:02d}")
        self.days[day].add_activity(activity)

    def print_month_activities(self):

        print(f"Activities for {self.name} {self.year}:")
        for day in sorted(self.days):
            self.days[day].print_activities()
            print("=" * 40)

class TodoList:
    def __init__(self, month, year):
        
        self.month = Month(month, year)
        self.current_date = datetime.now()
    
    def add_activity(self, title, description, day, recurrence=None):
        
        date_str = f"{self.month.year}-{self.month.name}-{day:02d}"
        activity = Activity(title, description, date_str)
        
        if recurrence == 'daily':
            for d in range(day, 32): 
                self.month.add_activity(d, Activity(title, description, f"{self.month.year}-{self.month.name}-{d:02d}"))
        elif recurrence == 'weekly':
            for d in range(day, 32, 7):
                self.month.add_activity(d, Activity(title, description, f"{self.month.year}-{self.month.name}-{d:02d}"))
        else:
            self.month.add_activity(day, activity)

    def view_activities_today(self):
        
        today = self.current_date.day
        if today in self.month.days:
            self.month.days[today].print_activities()
        else:
            print("No activities for today.")
    
    def view_activities_tomorrow(self):
    
        tomorrow = self.current_date.day + 1
        if tomorrow in self.month.days:
            self.month.days[tomorrow].print_activities()
        else:
            print("No activities for tomorrow.")
    
    def view_activities_month(self):
        
        self.month.print_month_activities()