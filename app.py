from tkinter import *
from database import Database

database = Database("bookstore.db")


class GUI:

    def __init__(self, window):
        self.window = window
        self.window.title("Bookstore")
        self.selected_row = None

        self.title_label = Label(self.window, text="Title")
        self.title_label.grid(row=0, column=0)
        self.title_data = StringVar()
        self.title_text = Entry(self.window, textvariable=self.title_data)
        self.title_text.grid(row=0, column=1)

        self.author_label = Label(self.window, text="Author")
        self.author_label.grid(row=0, column=2)
        self.author_data = StringVar()
        self.author_text = Entry(self.window, textvariable=self.author_data)
        self.author_text.grid(row=0, column=3)

        self.year_label = Label(self.window, text="Year")
        self.year_label.grid(row=1, column=0)
        self.year_data = StringVar()
        self.year_text = Entry(window, textvariable=self.year_data)
        self.year_text.grid(row=1, column=1)

        self.isbn_label = Label(self.window, text="ISBN")
        self.isbn_label.grid(row=1, column=2)
        self.isbn_data = StringVar()
        self.isbn_text = Entry(self.window, textvariable=self.isbn_data)
        self.isbn_text.grid(row=1, column=3)

        self.book_listbox = Listbox(self.window, height=6, width=35)
        self.book_listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.book_listbox.bind("<<ListboxSelect>>", self.get_selected_row)

        self.list_scrollbar = Scrollbar(self.window)
        self.list_scrollbar.grid(row=2, column=2, rowspan=6)
        self.book_listbox.configure(yscrollcommand=self.list_scrollbar.set)
        self.list_scrollbar.configure(command=self.book_listbox.yview)

        self.view_button = Button(self.window, text="View All", width=12, command=self.view_command)
        self.view_button.grid(row=2, column=3)

        self.search_button = Button(window, text="Search Entries", width=12, command=self.search_command)
        self.search_button.grid(row=3, column=3)

        self.add_button = Button(self.window, text="Add Entry", width=12, command=self.add_entry)
        self.add_button.grid(row=4, column=3)

        self.update_button = Button(self.window, text="Update Entry", width=12, command=self.update_entry)
        self.update_button.grid(row=5, column=3)

        self.delete_button = Button(self.window, text="Delete", width=12, command=self.delete_entry)
        self.delete_button.grid(row=6, column=3)

        self.close_button = Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.close_button.grid(row=7, column=3)

        self.window.mainloop()

    def view_command(self):
        self.book_listbox.delete(0, END)
        for row in database.view_all():
            self.book_listbox.insert(END, row)

    def search_command(self):
        self.book_listbox.delete(0, END)
        for row in database.search(self.title_data.get(), self.author_data.get(), self.year_data.get(),
                                   self.isbn_data.get()):
            self.book_listbox.insert(END, row)

    def add_entry(self):
        database.insert(self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get())
        self.book_listbox.delete(0, END)
        self.book_listbox.insert(END, (self.title_data.get(), self.author_data.get(), self.year_data.get(),
                                       self.isbn_data.get()))

    def delete_entry(self):
        database.delete(self.selected_row[0])

    def update_entry(self):
        database.update(self.selected_row[0], self.title_data.get(), self.author_data.get(), self.year_data.get(),
                        self.isbn_data.get())

    def get_selected_row(self, event):
        try:
            index = self.book_listbox.curselection()[0]
            self.selected_row = self.book_listbox.get(index)
            self.title_text.delete(0, END)
            self.title_text.insert(END, self.selected_row[1])
            self.author_text.delete(0, END)
            self.author_text.insert(END, self.selected_row[2])
            self.year_text.delete(0, END)
            self.year_text.insert(END, self.selected_row[3])
            self.isbn_text.delete(0, END)
            self.isbn_text.insert(END, self.selected_row[4])
        except IndexError:
            pass


GUI(Tk())
