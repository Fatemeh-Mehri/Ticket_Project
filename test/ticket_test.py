from model.entity.ticket import Ticket

ticket1 = Ticket(1,356,'Tehran','Kish','Iran Air',
                 '1404/05/02','1404/05/07',1000,27,False)

ticket1.save()
print(ticket1.id)


#todo:mikhastam sold ro az vorodi ha hazf konam vali nemidonestam to marahel badesh bayad chikaresh konm
#todo:save kar nemikone nmidonm chera
