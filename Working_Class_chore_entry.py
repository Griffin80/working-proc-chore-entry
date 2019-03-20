from tkinter import *
import json


"""working!!!
Do not modify!!!"""


chore_file = 'Class chore file.json'

try:
    with open(chore_file, 'r') as first_try:
        data = json.load(first_try)

except FileNotFoundError:
    with open(chore_file, 'w') as initialize:
        data = json.loads("""{"Chores":{}}""")
        json.dump(data, initialize, indent=2)
        print('created', data)


class ChoreEntry(Frame):
    parts_of_the_day = ['morning', 'afternoon', 'night']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.chore_name = Entry(self)
        self.chore_name.grid(row=0, column=0)
        self.chore_dorm = Entry(self)
        self.chore_dorm.grid(row=0,column=1)
        self.chore_handicap = Entry(self)
        self.chore_handicap.grid(row=0,column=2)

        self.branch_entry = Entry(self)
        self.branch_entry.grid(row=0,column=3)

        self.button = Button(self, text='button', command=self.add)
        self.button.grid(row=1,columnspan=4)

    def add(self):
        new_dict = {self.chore_name.get(): {'dorm': self.chore_dorm.get(), 'handicap': self.chore_handicap.get()}}
        if self.branch_entry.get() not in data['Chores']:
            data['Chores'][self.branch_entry.get()] = {}
            for part in self.parts_of_the_day:
                data['Chores'][self.branch_entry.get()][part] = [new_dict]

        else:

            for part_of_day in data['Chores'][self.branch_entry.get()]:
                data['Chores'][self.branch_entry.get()][part_of_day].append(new_dict)

        data_rep = json.dumps(data, indent=2)
        print('chore added: ', data_rep)


root = Tk()

chore_entry = ChoreEntry(root)
chore_entry.grid(row=0)

root.mainloop()
with open(chore_file, 'w') as file:
    json.dump(data, file, indent=4)
