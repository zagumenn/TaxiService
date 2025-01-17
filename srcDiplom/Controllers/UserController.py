from srcDiplom.Models.User import *
from bcrypt import hashpw, gensalt, checkpw


class UserController:
    @classmethod
    def registration(cls, fullname, login, password, gender, phone, role_id):
        # Проверка логина
        if Users.select().where(Users.login == login):
            return "Пользователь с таким логином существует, попробуйте снова"

        # Хеширование пароля
        hash_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
        Users.create(fullname=fullname, login=login, password=hash_password, gender_id=gender, phone=phone, role_id=role_id)
        return f"Пользователь {login} добавлен в систему"

    @classmethod
    def update(cls, id, new_name):
        Users.update({Users.fullname: new_name}).where(Users.id == id).execute()

    @classmethod
    def delete(cls, id):
        Users.delete_by_id(id)

    @classmethod
    def auth(cls, login, password):
        if Users.get_or_none(Users.login == login) != None:
            paswd = Users.get_or_none(Users.login == login).password

            if checkpw(password.encode('utf-8'), paswd.encode('utf-8')):
                return True

        return False

if __name__ == "__main__":
    #print(UserController.registration('Ivanov Ivan', 'ivan89', '111111111', 2))
    print(UserController.auth('ivan89', '111111111'))
