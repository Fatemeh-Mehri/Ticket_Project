from model.tools.validation import *

class User:
    def __init__(self, id_, name, family, birth_date, user_name, password):
        self.id_ = id_
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.user_name = user_name
        self.password = password


    @property
    def id_(self):
        return self.id_

    @id_.setter
    def id_(self, value):
        self.id_ = value


    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        name_validator(value)
        self.name = value


    @property
    def family(self):
        return self.family

    @family.setter
    def family(self, value):
        family_validator(value)
        self.family = value


    @property
    def birth_date(self):
        return self.birth_date

    @birth_date.setter
    def birth_date(self, value):
        date_validator(value)
        self.birth_date = value


    @property
    def user_name(self):
        return self.user_name

    @user_name.setter
    def user_name(self, value):
        user_name_validator(value)
        self.user_name = value


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        password_validator(password)
        self.password = value
