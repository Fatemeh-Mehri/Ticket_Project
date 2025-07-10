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


        self.win.mainloop()






if __name__ == "__main__":
    TicketView()






