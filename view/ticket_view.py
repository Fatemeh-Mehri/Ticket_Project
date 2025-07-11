from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from controller.ticket_contoller import TicketController
from model.tools.validation import city_list, airline_list


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
            self.table.insert("", END, values=(
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
            ))
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
        self.airline = StringVar()
        self.start_date_time = StringVar()
        self.end_date_time = StringVar()
        self.price = IntVar()
        self.seat_no = IntVar()
        self.sold = BooleanVar()

        Label(self.win, text='id').place(x=50,y=20)
        Entry(self.win, textvariable=self.id).place(x=100,y=20)

        Label(self.win, text="Code").place(x=40,y=60)
        Entry(self.win, textvariable=self.code).place(x=100,y=60)

        Label(self.win, text="Origin").place(x=35,y=100)
        ttk.Combobox(self.win, textvariable=self.origin, values=city_list).place(x=100,y=100)

        Label(self.win, text="Destination").place(x=20,y=140)
        ttk.Combobox(self.win, textvariable=self.destination, values=city_list).place(x=100,y=140)

        Label(self.win, text="Airline").place(x=35,y=180)
        ttk.Combobox(self.win, textvariable=self.airline, values=airline_list).place(x=100,y=180)

        Label(self.win, text="Start Date Time").place(x=13,y=220)
        Entry(self.win, textvariable=self.start_date_time).place(x=100,y=220)

        Label(self.win, text="End Date Time").place(x=13,y=260)
        Entry(self.win, textvariable=self.end_date_time).place(x=100,y=260)

        Label(self.win, text="Price").place(x=35,y=300)
        Entry(self.win, textvariable=self.price).place(x=100,y=300)

        Label(self.win, text="Seat No").place(x=35,y=340)
        Entry(self.win, textvariable=self.seat_no).place(x=100,y=340)

        Label(self.win, text="Sold").place(x=35,y=380)
        ttk.Checkbutton(self.win, variable=self.sold,onvalue=True, offvalue=False).place(x=100,y=380)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9], show='headings')
        self.table.place(x=270, y=20)

        self.table.heading(1, text='id')
        self.table.heading(2, text='ticket code')
        self.table.heading(3, text='source')
        self.table.heading(4, text='destination')
        self.table.heading(5, text='start date time')
        self.table.heading(6, text='end date time')
        self.table.heading(7, text='price')
        self.table.heading(8, text='seat no')
        self.table.heading(9, text='sold')

        self.table.column(1, width=70)
        self.table.column(2, width=100)
        self.table.column(3, width=130)
        self.table.column(4, width=130)
        self.table.column(5, width=130)
        self.table.column(6, width=130)
        self.table.column(7, width=110)
        self.table.column(8, width=110)
        self.table.column(9, width=110)

        Button(self.win, text="Save", command=self.save_click).place(x=70,y=500,width=80)



        self.win.mainloop()
