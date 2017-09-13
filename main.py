from tkinter import *
import back_end

def view_command():
    list_box.delete(0,END)
    for row in back_end.view_all():
        list_box.insert(END,row)

def search_command():
    list_box.delete(0,END)
    for row in back_end.search(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()):
        list_box.insert(END,row)

def add_command():
    back_end.insert(title_var.get(),author_var.get(),year_var.get(),isbn_var.get())
    list_box.delete(0,END)
    list_box.insert(END,(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()))

def get_select_row(event):
    index = list_box.curselection()[0]
    global selected_tuple
    selected_tuple = list_box.get(index)
    entry_title.delete(0,END)
    entry_title.insert(END,selected_tuple[1])
    entry_author.delete(0,END)
    entry_author.insert(END,selected_tuple[2])
    entry_year.delete(0,END)
    entry_year.insert(END,selected_tuple[3])
    entry_isbn.delete(0,END)
    entry_isbn.insert(END,selected_tuple[4])


def delete_command():
    back_end.delete(selected_tuple[0])
    list_box.delete(0,END)
    view_command()

def update_command():
    back_end.update(selected_tuple[0],entry_title.get(),entry_author.get(),entry_year.get(),entry_isbn.get())
    list_box.delete(0,END)
    view_command()

window = Tk()
window.wm_title("BOOKSTORE Version@1.0")

label_title = Label(window,text="TITLE")
label_title.grid(row=0,column=0)

label_author = Label(window,text="AUTHOR")
label_author.grid(row=1,column=0)

label_year = Label(window,text="YEAR")
label_year.grid(row=2,column=0)

label_isbn = Label(window,text="ISBN")
label_isbn.grid(row=3,column=0)

title_var = StringVar()
entry_title = Entry(window,textvariable=title_var)
entry_title.grid(row=0,column=1)

author_var = StringVar()
entry_author = Entry(window,textvariable=author_var)
entry_author.grid(row=1,column=1)

year_var = StringVar()
entry_year = Entry(window,textvariable=year_var)
entry_year.grid(row=2,column=1)

isbn_var = StringVar()
entry_isbn = Entry(window,textvariable=isbn_var)
entry_isbn.grid(row=3,column=1)

scrollbar = Scrollbar(window)
scrollbar.grid(row=0,column=2,rowspan=10,columnspan=1)

list_box = Listbox(window,height=10,width=60,borderwidth=3,yscrollcommand=scrollbar.set)
list_box.grid(row=0,column=3,rowspan=10,columnspan=6)

list_box.bind("<<ListboxSelect>>",get_select_row)

button1 = Button(window,text="Add Entry",width=15,cursor='dot',command=add_command)
button1.grid(row=4,column=0)

button2 = Button(window,text="View All",width=15,cursor='dot',command=view_command)
button2.grid(row=4,column=1)

button3 = Button(window,text="Update Entry",width=15,cursor='dot',command=update_command)
button3.grid(row=5,column=0)

button4 = Button(window,text="Search Entry",width=15,cursor='dot',command=search_command)
button4.grid(row=5,column=1)

button5 = Button(window,text="Delete Entry",width=15,cursor='dot',command=delete_command)
button5.grid(row=6,column=0)

button6 = Button(window,text="Close",width=15,cursor='dot',command=window.destroy)
button6.grid(row=6,column=1)

window.mainloop()
