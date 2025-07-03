from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from controller.ticket_contoller import TicketController

from model.tools.validation import city_list


class TicketView:
    def save_click(self, code):
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
            msg.shoself.winfo("Save", message)
        else:
            msg.showerror("Save Error", message)


    def __init__(self):
        self.win = Tk()
        self.win.geometry("1330x600")

        self.code = IntVar()
        self.origin = StringVar()
        self.destination = StringVar()
        self.airline = IntVar()
        self.start_date_time = StringVar()
        self.end_date_time = StringVar()
        self.price = IntVar()
        self.seat_no = IntVar()
        self.sold = BooleanVar()




        Label(self.win, text="Code").place(x=20, y=20)
        Entry(self.win, textvariable=self.code).place(x=20, y=20)

        Label(self.win, text="Origin").place()
        Entry(self.win, textvariable=self.origin).place()

        Label(self.win, text="Destination").place()
        Entry(self.win, textvariable=self.destination).place()

        Label(self.win, text="Airline").place()
        ttk.Combobox(self.win, textvariable=self.airline ,values=city_list).place()

        Label(self.win, text="Start Date Time").place()
        Entry(self.win, textvariable=self.start_date_time).place()

        Label(self.win, text="End Date Time").place()
        Entry(self.win, textvariable=self.end_date_time).place()

        Label(self.win, text="Price").place()
        Entry(self.win, textvariable=self.price).place()

        Label(self.win, text="Seat No").place()
        Entry(self.win, textvariable=self.seat_no).place()

        Label(self.win, text="Sold").place()
        Label(self.win, textvariable=self.sold).place()


        Button(self.win, text="Save", command=self.save_click).place()

        self.win.mainloop()