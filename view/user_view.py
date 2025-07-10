from controller.user_controller import UserController
import tkinter.messagebox as msg
from tkinter import *
import tkinter.ttk as ttk

from view.ticket_view import TicketView


class UserView:
    def save_click(self):
        user_controller = UserController()
        status, message = user_controller.save(
            self.id.get(),
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.user_name.get(),
            self.password.get(),
        )
        if status:
            msg.showinfo("save", message)

        else:
            msg.showerror("save error", message)


    def __init__(self):
        win = Tk()
        win.title("user info")
        win.geometry("300x300")


        self.id = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birth_date = StringVar()
        self.user_name = StringVar()
        self.password = StringVar()


        Label(win, text="id").place(x=10, y=10)
        Entry(win, textvariable=self.id).place(x=40, y=10)

        Label(win, text="Name").place(x=10, y=40)
        Entry(win, textvariable=self.name).place(x=40, y=40)

        Label(win, text="Family").place(x=10, y=80)
        Entry(win, textvariable=self.family).place(x=40, y=80)

        Label(win, text="Birth Date").place(x=10, y=100)
        Entry(win, textvariable=self.birth_date).place(x=40, y=100)

        Label(win, text="User Name").place(x=10, y=140)
        Entry(win, textvariable=self.user_name).place(x=40, y=140)

        Label(win, text="Password").place(x=10, y=180)
        Entry(win, textvariable=self.password).place(x=40, y=180)



        table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9], show='headings')
        table.place(x=270, y=20)

        table.heading(1, text='id')
        table.heading(2, text='name')
        table.heading(3, text='family')
        table.heading(4, text='birth date')
        table.heading(5, text='user name')

        self.table.column(1, width=100)
        self.table.column(2, width=130)
        self.table.column(3, width=130)
        self.table.column(4, width=130)
        self.table.column(5, width=130)

        Button(self.win, text="Save", command=self.save_click).place(x=70, y=500)
#        Button(self.win, text="Save", command=self.edit).place()
#        Button(self.win, text="Save", command=self.remove).place()



        self.win.mainloop()






if __name__ == "__main__":
    TicketView()






