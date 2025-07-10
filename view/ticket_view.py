from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from controller.ticket_contoller import TicketController
from model.tools.validation import city_list


class TicketView:
    def save_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.save(
            self.id.get(),
            self.code.get(),
            self.origin.get(),
            self.destination.get(),
            self.airline.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.price.get(),
            self.seat_no.get(),
            self.sold.get()
        )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)

    def __init__(self):
        self.win = Tk()
        self.win.geometry("1330x600")
        self.win.title("Ticket info")

        self.id = IntVar()
        self.code = IntVar()
        self.origin = StringVar()
        self.destination = StringVar()
        self.airline = IntVar()
        self.start_date_time = StringVar()
        self.end_date_time = StringVar()
        self.price = IntVar()
        self.seat_no = IntVar()
        self.sold = BooleanVar()

        Label(self.win, text='id').place(x=50,y=20)
        Entry(self.win, textvariable=self.id).place(x=100,y=20)

        Label(self.win, text="Code").place(x=25,y=60)
        Entry(self.win, textvariable=self.code).place(x=100,y=60)

        Label(self.win, text="Origin").place(x=40,y=100)
        Entry(self.win, textvariable=self.origin).place(x=100,y=100)

        Label(self.win, text="Destination").place(x=20,y=140)
        Entry(self.win, textvariable=self.destination).place(x=100,y=14)

        Label(self.win, text="Airline").place(x=35,y=180)
        ttk.Combobox(self.win, textvariable=self.airline, values=city_list).place(x=100,y=180)

        Label(self.win, text="Start Date Time").place(x=13,y=220)
        Entry(self.win, textvariable=self.start_date_time).place(x=100,y=220)

        Label(self.win, text="End Date Time").place(x=13,y=260)
        Entry(self.win, textvariable=self.end_date_time).place(x=100,y=260)

        Label(self.win, text="Price").place(x=35,y=300)
        Entry(self.win, textvariable=self.price).place(x=100,y=300)

        Label(self.win, text="Seat No").place(x=35,y=340)
        Entry(self.win, textvariable=self.seat_no).place(x=100,y=340)

        Label(self.win, text="Sold").place(x=35,y=380)
        Label(self.win, textvariable=self.sold).place(x=100,y=380)

        table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9], show='headings')
        table.place(x=270, y=20)

        table.heading(1, text='id')
        table.heading(2, text='ticket code')
        table.heading(3, text='source')
        table.heading(4, text='destination')
        table.heading(5, text='start date time')
        table.heading(6, text='end date time')
        table.heading(7, text='price')
        table.heading(8, text='seat no')
        table.heading(9, text='sold')

        table.column(1, width=70)
        table.column(2, width=100)
        table.column(3, width=130)
        table.column(4, width=130)
        table.column(5, width=130)
        table.column(6, width=130)
        table.column(7, width=110)
        table.column(8, width=110)
        table.column(9, width=110)

        Button(self.win, text="Save", command=self.save_click).place(x=70,y=500,width=80)


#todo:ejra nemishe
        self.win.mainloop()
