from model.entity.ticket import Ticket

ticket_list = []


class TicketController:
    def save(self, id, code, origin, destination, airline, start_date_time, end_date_time, price, seat_no, sold):
        try:
            ticket = Ticket(id,code, origin, destination, airline, start_date_time, end_date_time, price, seat_no, sold)
            ticket_list.append(ticket)
            return True, f"ticket info saved successfully {ticket}"

        except Exception as e:
            e.with_traceback()
            return False, f"error saving ticket info {e}"

    def edit(self,id, code, origin, destination, airline, start_date_time, end_date_time, price, seat_no, sold):
        try:
            ticket_ = Ticket(id,code, origin, destination, airline, start_date_time, end_date_time, price, seat_no, sold)

            return True, f"ticket info edited successfully {ticket_}"

        except Exception as e:
            return False, f"error editing ticket info {e}"

    def delete(self, code):
        try:
            return True, f"ticket info deleted successfully {code}"
        except Exception as e:
            return False, f"error deleting ticket info {e}"
