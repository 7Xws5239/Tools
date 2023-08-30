import csv
import webbrowser
import tkinter as tk
from tkinter import filedialog

status_list = ['Waiting for Customer', 'Solution Deliver', 'Escalated', 'Researching', 'Self-Answered',
               'Deleted', 'Off-Topic', 'Answered', 'Reopen', 'New Issue', 'Follow Up', 'Need Follow Up']


def get_title_and_link_col_from_csv(file_path, selected_statuses):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] in selected_statuses:
                print(row[2])
                webbrowser.open(row[2])


class StatusWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Status List")
        self.geometry("300x400")

        self.check_vars = [tk.BooleanVar() for _ in status_list]
        self.check_buttons = []

        for i, status in enumerate(status_list):
            cb = tk.Checkbutton(self, text=status, variable=self.check_vars[i])
            cb.pack(anchor="w", padx=10)
            self.check_buttons.append(cb)

        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.pack(anchor="center", pady=10)

    def submit(self):
        selected_statuses = [status for i, status in enumerate(status_list) if self.check_vars[i].get()]
        print("Selected statuses:", selected_statuses)

        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            get_title_and_link_col_from_csv(file_path, selected_statuses)


if __name__ == "__main__":
    app = StatusWindow()
    app.mainloop()



# #open file in current folder named Thread List 2023-03-01-2023-03-24.csv

# import csv
# import webbrowser
# import tkinter as tk

# status_list = ['Waiting for Customer','Solution Deliver','Escalated','Researching','Self-Answered','Deleted','Off-Topic','Answered','Reopen','New Issue','Follow Up','Need Follow Up']

# def get_title_and_link_col_from_csv(file_path, selected_statuses):
#     f = open(file_path, 'r')
#     reader = csv.reader(f)
#     for row in reader:
#         #check if row[7] is a member of selected_statuses
#         if row[7] in selected_statuses:
#             print(row[2])
#             #open the link in browser
#             webbrowser.open(row[2])
# #create a window to show the status list, all of the items are checkboxes
# class StatusWindow(tk.Tk):

#     def __init__(self):
#         super().__init__()

#         self.title("Status List")
#         self.geometry("300x400")

#         self.check_vars = [tk.BooleanVar() for _ in status_list]
#         self.check_buttons = []

#         for i, status in enumerate(status_list):
#             cb = tk.Checkbutton(self, text=status, variable=self.check_vars[i])
#             cb.pack(anchor="w", padx=10)
#             self.check_buttons.append(cb)

#         submit_button = tk.Button(self, text="Submit", command=self.submit)
#         submit_button.pack(anchor="center", pady=10)

#     def submit(self):
#         selected_statuses = [status for i, status in enumerate(status_list) if self.check_vars[i].get()]
#         print("Selected statuses:", selected_statuses)
#         get_title_and_link_col_from_csv('Thread List 2023-03-01-2023-03-24.csv', selected_statuses)

# if __name__ == "__main__":
#     app = StatusWindow()
#     app.mainloop()






