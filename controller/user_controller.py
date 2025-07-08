from model.entity.user import User

user_list = []


class UserController:
    def save(self, id, name, family, birth_date, user_name, password):
        try:
            user = User(id, name, family, birth_date, user_name, password)
            user_list.append(user)
            return True, f"user saved successfully"
        except Exception as e:
            return False, f"error saving user"

    def edit(self, id, name, family, birth_date, user_name, password):
        try:
            user = User(id, name, family, birth_date, user_name, password)
            return True, f"user edited successfully{user}"

        except Exception as e:
            return False, f"error editing user{e}"

    def delete(self, id):
        try:
            # remove from database

            return True, f"user deleted successfully{id}"
        except Exception as e:
            return False, f"error deleting user{e}"
