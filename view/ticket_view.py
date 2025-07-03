from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from controller.ticket_controller import*

class TicketView:
    def save_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.save(
            self.code.get(),
            self.origin.get(),
            self.destination.get(),
            self.airline.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.price.get(),
            self.seat_no.get()
        )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)


    def __init__(self):
        win = Tk()
        win.geometry("1330x600")

        self.code = IntVar()
        self.origin = StringVar()
        self.destination = StringVar()
        self.airline = IntVar()
        self.start_date_time = StringVar()
        self.end_date_time = StringVar()
        self.price = IntVar()
        self.seat_no = IntVar()
        self.sold = BooleanVar()




        Label(win, text="Code").place()
        Entry(win, textvariable=self.code).place()

        Label(win, text="Origin").place()
        Entry(win, textvariable=self.origin).place()

        Label(win, text="Destination").place()
        Entry(win, textvariable=self.destination).place()

        Label(win, text="Airline").place()
        ttk.Combobox(win, textvariable=self.airline ,values=[]).place()

        Label(win, text="Start Date Time").place()
        Entry(win, textvariable=self.start_date_time).place()

        Label(win, text="End Date Time").place()
        Entry(win, textvariable=self.end_date_time).place()

        Label(win, text="Price").place()
        Entry(win, textvariable=self.price).place()

        Label(win, text="Seat No").place()
        Entry(win, textvariable=self.seat_no).place()

        Label(win, text="Sold").place()
        Label(win, textvariable=self.sold).place()


        Button(win, text="Save", command=self.save_click).place()

        win.mainloop()