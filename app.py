from tkinter import *
from database import Database

database = Database("bookstore.db")


# Commands
def view_command():
    book_listbox.delete(0, END)
    for row in database.view_all():
        book_listbox.insert(END, row)


def search_command():
    book_listbox.delete(0, END)
    for row in database.search(title_data.get(), author_data.get(), year_data.get(), isbn_data.get()):
        book_listbox.insert(END, row)


def add_entry():
    database.insert(title_data.get(), author_data.get(), year_data.get(), isbn_data.get())
    book_listbox.delete(0, END)
    book_listbox.insert(END, (title_data.get(), author_data.get(), year_data.get(), isbn_data.get()))


def delete_entry():
    database.delete(selected_row[0])


def update_entry():
    database.update(selected_row[0], title_data.get(), author_data.get(), year_data.get(), isbn_data.get())


def get_selected_row(event):
    try:
        global selected_row
        index = book_listbox.curselection()[0]
        selected_row = book_listbox.get(index)
        title_text.delete(0, END)
        title_text.insert(END, selected_row[1])
        author_text.delete(0, END)
        author_text.insert(END, selected_row[2])
        year_text.delete(0, END)
        year_text.insert(END, selected_row[3])
        isbn_text.delete(0, END)
        isbn_text.insert(END, selected_row[4])
    except IndexError:
        pass


# UI Setup
window = Tk()
window.title("Bookstore")

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)
title_data = StringVar()
title_text = Entry(window, textvariable=title_data)
title_text.grid(row=0, column=1)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)
author_data = StringVar()
author_text = Entry(window, textvariable=author_data)
author_text.grid(row=0, column=3)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)
year_data = StringVar()
year_text = Entry(window, textvariable=year_data)
year_text.grid(row=1, column=1)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)
isbn_data = StringVar()
isbn_text = Entry(window, textvariable=isbn_data)
isbn_text.grid(row=1, column=3)

book_listbox = Listbox(window, height=6, width=35)
book_listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
book_listbox.bind("<<ListboxSelect>>", get_selected_row)

list_scrollbar = Scrollbar(window)
list_scrollbar.grid(row=2, column=2, rowspan=6)
book_listbox.configure(yscrollcommand=list_scrollbar.set)
list_scrollbar.configure(command=book_listbox.yview)

view_button = Button(window, text="View All", width=12, command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search Entries", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add Entry", width=12, command=add_entry)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update Entry", width=12, command=update_entry)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_entry)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
