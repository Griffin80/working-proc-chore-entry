from tkinter import *
import json

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
        self.name_label = Label(self, text='Name')
        self.name_label.grid(row=0, column=0)
        self.chore_name = Entry(self)
        self.chore_name.grid(row=1, column=0)
        self.dorm_label = Label(self, text='Dorm')
        self.dorm_label.grid(row=0, column=1)
        self.chore_dorm = Entry(self)
        self.chore_dorm.grid(row=1, column=1)
        self.handicap_label = Label(self, text='Handicap')
        self.handicap_label.grid(row=0, column=2)
        self.chore_handicap = Entry(self)
        self.chore_handicap.grid(row=1, column=2)
        self.branch_label = Label(self, text='Branch')
        self.branch_label.grid(row=0, column=3)
        self.branch_entry = Entry(self)
        self.branch_entry.grid(row=1, column=3)

        self.button = Button(self, text='button', command=self.add)
        self.button.grid(row=2, columnspan=4)

        self.indication_label = Label(self)
        self.indication_label.grid(row=2, column=3)

    def add(self):
        new_dict = {self.chore_name.get(): {'dorm': self.chore_dorm.get(), 'handicap': self.chore_handicap.get()}}
        if self.branch_entry.get() not in data['Chores']:
            data['Chores'][self.branch_entry.get()] = {}
            for part in self.parts_of_the_day:
                data['Chores'][self.branch_entry.get()][part] = [new_dict]

        else:

            for part_of_day in data['Chores'][self.branch_entry.get()]:
                if new_dict not in data['Chores'][self.branch_entry.get()][part_of_day]:
                    data['Chores'][self.branch_entry.get()][part_of_day].append(new_dict)
                    self.indication_label.configure(text='Entered', fg='green')
                else:
                    self.indication_label.configure(text='Already in the system', fg='red')

        data_rep = json.dumps(data, indent=2)
        print('chore added: ', data_rep)


# class EntryArray(Frame):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for category in data['Chores']:
#             self.button = Button(self, text=category, command=self.create_array)
#             self.button.grid()
#
#     def create_array(self):
#
#         print(self.button['text'])


root = Tk()

# array = EntryArray(root)
# array.grid(row=0, column=0)

chore_entry = ChoreEntry(root)
chore_entry.grid(row=0)

root.mainloop()
with open(chore_file, 'w') as file:
    json.dump(data, file, indent=4)
