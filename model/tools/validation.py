import re
from datetime import datetime, date

city_list = ["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Ahvaz", "Qom", "Kermanshah", "Urmia",
             "Rasht", "Zahedan", "Hamadan", "Kerman", "Yazd", "Arak", "Sanandaj", "Bandar Abbas", "Zanjan",
             "Khorramabad", "Gorgan", "Sari", "Bojnord", "Birjand", "Qazvin", "Karaj", "Ilam", "Bushehr", "Shahrekord",
             "Yasuj", "Semnan", "Ardabil"]

airline_list = ["Iran Air", "Iran Airtour", "Iran Aseman Airlines", "Mahan Air", "Kish Air", "Qeshm Air",
                "Caspian Airlines", "Taban Air", "Karun Airlines", "Saha Airlines", "FlyPersia", "Chabahar Airlines",
                "Aria Air", "Safiran Airlines", "Eram Air", "Payam Air"]



def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z]{3,30}&", name)):
        raise ValueError("invalid name")


def family_validator(family):
    if not (type(family) == str and re.match(r"^[a-zA-Z]{3,30}&", family)):
        raise ValueError("invalid family")


def date_validator(date_, message):
    try:
        if type(date_) == str:
            datetime.strptime(date_, "%Y-%m-%d").date
        elif type(date_) != date:
            raise ValueError()
    except:
        raise ValueError(message)


def date_time_validator(date_time, message):
    try:
        if type(date_time) == str:
            datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        elif type(date_time) != datetime:
            raise ValueError()
    except:
        raise ValueError(message)


def user_name_validator(user_name):
    if not (type(user_name) == str and re.match(r"^[a-zA-Z]{3,30}&", user_name)):
        raise ValueError("invalid user name")


def ticket_code_validator(ticket_code):
    if not (type(ticket_code) == int and (re.match(r"^[0-9]{3,10}$", ticket_code))):
        raise ValueError("invalid ticket code")


def city_validator(city, message):
    if not (type(city) == str and city in city_list):
        raise ValueError(message)


def airline_validator(airline):
    if not (type(airline) == str and airline in airline_list):
        raise ValueError("invalid airline")


def sold_validator(sold):
    pass
