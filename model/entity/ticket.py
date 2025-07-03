from model.tools.validation import *


class Ticket:
    def __init__(self, code, origin, destination, airline, start_date_time, end_date_time, price, seat_no, sold):
        self.code = code
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.price = price
        self.seat_no = seat_no
        self.sold = sold

    def __repr__(self):
        return f"Ticket(code={self.code})"


    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        ticket_code_validator(value)
        self._code = value


    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        origin_validator(value)
        self._origin = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        destination_validator(value)
        self._destination = value


    @property
    def airline(self):
       return self._airline


    @airline.setter
    def airline(self, value):
       airline_validator(value)
       self._airline = value




    @property
    def start_date_time(self):
       return self._start_date_time


    @start_date_time.setter
    def start_date_time(self, value):
       start_date_time_validator(value)
       self._start_date_time = value


    @property
    def end_date_time(self):
       return self._end_date_time


    @end_date_time.setter
    def end_date_time(self, value):
        end_date_time_validator(value)
        self._end_date_time = value


    @property
    def price(self):
       return self._price


    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value


    @property
    def seat_no (self):
        return self._seat_no

    @seat_no.setter
    def seat_no (self, value):
        self._seat_no = value
