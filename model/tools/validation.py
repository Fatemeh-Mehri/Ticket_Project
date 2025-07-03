import re


# user validator
def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z]{3,30}&", name)):
        raise ValueError("invalid name")


def family_validator(family):
    if not (type(family) == str and re.match(r"^[a-zA-Z]{3,30}&", family)):
        raise ValueError("invalid family")


def birth_date_validator(birth_date):
    if not (type(birth_date) == str and re.match(r"^\d{4}-\d{2}-\d{2}$", birth_date)):
        raise ValueError("invalid birth date")


def user_name_validator(user_name):
    if not (type(user_name) == str and re.match(r"^[a-zA-Z]{3,30}&", user_name)):
        raise ValueError("invalid user name")


# ticket validator


def ticket_code_validator(ticket_code):
    if not (type(ticket_code) == int and (re.match(r"^[0-9]{3,10}$", ticket_code))):
        raise ValueError("invalid ticket code")


def orgin_validator(orgin):
    pass


def destination_validator(destination):
    if not (type(destination) == str and
            destination not in ["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Ahvaz", "Qom", "Kermanshah",
                                "Urmia",
                                "Rasht", "Zahedan", "Hamadan", "Kerman", "Yazd", "Arak", "Sanandaj", "Bandar Abbas",
                                "Zanjan",
                                "Khorramabad", "Gorgan", "Sari", "Bojnord", "Birjand", "Qazvin", "Karaj", "Ilam",
                                "Bushehr", "Shahrekord",
                                "Yasuj", "Semnan", "Ardabil"]):

        raise ValueError("invalid destination")


def airline_validator(airline):
    pass


def time_validator(time):
    pass
