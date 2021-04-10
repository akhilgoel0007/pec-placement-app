from db_config import mysql
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, first_name, last_name, email, password, is_active=None, date_of_birth=None, gender=None, linkedin_url=None, github_url=None, phone_number=None, address=None, admin=False, student_id=None, batch=None, branch=None, semester=None, current_cg=None, total_backlogs=None, cg_marksheet=None, school_name_12=None, percentage_12=None, marksheet_12=None, school_name_10=None, percentage_10=None, marksheet_10=None):
        self.id = _id
        self.email = email
        self.admin = admin
        self.batch = batch
        self.gender = gender
        self.branch = branch
        self.address = address
        self.semester = semester
        self.password = password
        self.last_name = last_name
        self.is_active = is_active
        self.first_name = first_name
        self.current_cg = current_cg
        self.student_id = student_id
        self.github_url = github_url
        self.cg_marksheet = cg_marksheet
        self.phone_number = phone_number
        self.linkedin_url = linkedin_url
        self.marksheet_12 = marksheet_12
        self.marksheet_10 = marksheet_10
        self.percentage_10 = percentage_10
        self.percentage_12 = percentage_12
        self.date_of_birth = date_of_birth
        self.school_name_12 = school_name_12
        self.school_name_10 = school_name_10
        self.total_backlogs = total_backlogs

    @staticmethod
    def create_table():
        connection = mysql.connect()
        cursor = connection.cursor()

        create_user_table = "CREATE TABLE IF NOT EXISTS users (" \
                            "id INT AUTO_INCREMENT PRIMARY KEY," \
                            "first_name TEXT NOT NULL," \
                            "last_name TEXT NOT NULL," \
                            "date_of_birth TEXT," \
                            "gender TEXT," \
                            "linkedin_url TEXT," \
                            "github_url TEXT," \
                            "email TEXT NOT NULL UNIQUE," \
                            "password TEXT NOT NULL," \
                            "phone_number TEXT," \
                            "address TEXT," \
                            "admin BOOLEAN DEFAULT FALSE," \
                            "student_id TEXT," \
                            "batch TEXT," \
                            "branch TEXT," \
                            "semester TEXT," \
                            "current_cg FLOAT," \
                            "total_backlogs INT," \
                            "cg_marksheet TEXT," \
                            "school_name_12 TEXT," \
                            "percentage_12 TEXT," \
                            "marksheet_12 TEXT," \
                            "school_name_10 TEXT," \
                            "percentage_10 TEXT," \
                            "marksheet_10 TEXT," \
                            "is_active BOOLEAN DEFAULT TRUE" \
                            ");"

        cursor.execute(create_user_table)
        connection.commit()
        connection.close()

    def find_id_by_email(self):
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT id FROM users WHERE email='{self.email}'")
        user_id = cursor.fetchone()[0]
        connection.close()

        return user_id if user_id else None

    def user_authentication(self):
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM users WHERE email='{self.email}' AND password='{self.password}'")
        user_data = cursor.fetchone()

        connection.close()

        return user_data if user_data else None

    @staticmethod
    def find_by_id(_id):
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM users WHERE id={_id}")
        user = cursor.fetchone()

        connection.close()

        return user if user else None

    @staticmethod
    def find_all_users():
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM users")
        all_users = cursor.fetchall()

        return all_users if all_users else None


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("first_name", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("last_name", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("email", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("password", type=str, required=True, help="This field cannot be blank")

    @staticmethod
    def post():
        """This method will be used for signing up students initially."""

        data = UserRegister.parser.parse_args()

        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"INSERT INTO users (first_name,last_name,email,password) VALUES ('{data['first_name']}','{data['last_name']}','{data['email']}','{data['password']}')"
        )

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201


class UserModification(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("email", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("date_of_birth", type=str, required=False)
    parser.add_argument("gender", type=str, required=False)
    parser.add_argument("linkedin_url", type=str, required=False)
    parser.add_argument("github_url", type=str, required=False)
    parser.add_argument("phone_number", type=str, required=False)
    parser.add_argument("address", type=str, required=False)
    parser.add_argument("admin", type=bool, required=False)
    parser.add_argument("is_active", type=bool, required=False)
    parser.add_argument("student_id", type=str, required=False)
    parser.add_argument("batch", type=str, required=False)
    parser.add_argument("branch", type=str, required=False)
    parser.add_argument("semester", type=str, required=False)
    parser.add_argument("current_cg", type=float, required=False)
    parser.add_argument("total_backlogs", type=int, required=False)
    parser.add_argument("cg_marksheet", type=str, required=False)
    parser.add_argument("school_name_12", type=str, required=False)
    parser.add_argument("percentage_12", type=str, required=False)
    parser.add_argument("marksheet_12", type=str, required=False)
    parser.add_argument("school_name_10", type=str, required=False)
    parser.add_argument("percentage_10", type=str, required=False)
    parser.add_argument("marksheet_10", type=str, required=False)

    @staticmethod
    def add_response(response, status, field):
        if status:
            response[field] = 'updated'
        else:
            response[field] = 'update_failed'
        return response

    def patch(self):
        data = UserModification.parser.parse_args()

        user_id = User(None, None, None, data['email'], None).find_id_by_email()
        response = {}

        if user_id:
            if data['date_of_birth']:
                response = self.add_response(response, self.update(user_id, 'date_of_birth', data['date_of_birth']), "date_of_birth")
            if data['gender']:
                response = self.add_response(response, self.update(user_id, 'gender', data['gender']), "gender")
            if data['linkedin_url']:
                response = self.add_response(response, self.update(user_id, 'linkedin_url', data['linkedin_url']), "linkedin_url")
            if data['github_url']:
                response = self.add_response(response, self.update(user_id, 'github_url', data['github_url']), "github_url")
            if data['phone_number']:
                response = self.add_response(response, self.update(user_id, 'phone_number', data['phone_number']), "phone_number")
            if data['address']:
                response = self.add_response(response, self.update(user_id, 'address', data['address']), "address")
            if data['admin'] == False or data['is_active'] == True:
                response = self.add_response(response, self.update(user_id, 'admin', data['admin']), "admin")
            if data['is_active'] == False or data['is_active'] == True:
                response = self.add_response(response, self.update(user_id, 'is_active', data['is_active']), "is_active")
            if data['student_id']:
                response = self.add_response(response, self.update(user_id, 'student_id', data['student_id']), "student_id")
            if data['batch']:
                response = self.add_response(response, self.update(user_id, 'batch', data['batch']), "batch")
            if data['branch']:
                response = self.add_response(response, self.update(user_id, 'branch', data['branch']), "branch")
            if data['semester']:
                response = self.add_response(response, self.update(user_id, 'semester', data['semester']), "semester")
            if data['current_cg']:
                response = self.add_response(response, self.update(user_id, 'current_cg', data['current_cg']), "current_cg")
            if data['total_backlogs']:
                response = self.add_response(response, self.update(user_id, 'total_backlogs', data['total_backlogs']), "total_backlogs")
            if data['cg_marksheet']:
                response = self.add_response(response, self.update(user_id, 'cg_marksheet', data['cg_marksheet']), "cg_marksheet")
            if data['school_name_12']:
                response = self.add_response(response, self.update(user_id, 'school_name_12', data['school_name_12']), "school_name_12")
            if data['percentage_12']:
                response = self.add_response(response, self.update(user_id, 'percentage_12', data['percentage_12']), "percentage_12")
            if data['marksheet_12']:
                response = self.add_response(response, self.update(user_id, 'marksheet_12', data['marksheet_12']), "marksheet_12")
            if data['school_name_10']:
                response = self.add_response(response, self.update(user_id, 'school_name_10', data['school_name_10']), "school_name_10")
            if data['percentage_10']:
                response = self.add_response(response, self.update(user_id, 'percentage_10', data['percentage_10']), "percentage_10")
            if data['marksheet_10']:
                response = self.add_response(response, self.update(user_id, 'marksheet_10', data['marksheet_10']), "marksheet_10")
            return {"message": "user found!", "update_status": response}, 202
        else:
            return {"message": "user was not found!"}, 401

    @classmethod
    def update(cls, user_id, field, field_value):
        connection = mysql.connect()
        cursor = connection.cursor()

        if field not in ['is_active', 'admin', 'current_cg', 'total_backlogs']:
            cursor.execute(f"UPDATE users SET {field}='{field_value}' WHERE id={user_id}")
        elif field == 'current_cg':
            cursor.execute(f"UPDATE users SET current_cg={field_value} WHERE id={user_id}")
        elif field == 'total_backlogs':
            cursor.execute(f"UPDATE users SET total_backlogs={field_value} WHERE id={user_id}")
        elif field == 'admin':
            cursor.execute(f"UPDATE users SET admin={field_value} WHERE id={user_id}")
        elif field == 'is_active':
            cursor.execute(f"UPDATE users SET is_active={field_value} WHERE id={user_id}")
        else:
            connection.commit()
            connection.close()
            return False

        connection.commit()
        connection.close()
        return True


class UserData(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("email", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("password", type=str, required=True, help="This field cannot be blank")

    @staticmethod
    def json(user):
        return {
            "first_name": user[1],
            "last_name": user[2],
            "date_of_birth": user[3],
            "gender": user[4],
            "linkedin_url": user[5],
            "github_url": user[6],
            "email": user[7],
            "phone_number": user[9],
            "address": user[10],
            "admin": user[11],
            "student_id": user[12],
            "batch": user[13],
            "branch": user[14],
            "semester": user[15],
            "current_cg": user[16],
            "total_backlogs": user[17],
            "cg_marksheet": user[18],
            "school_name_12": user[19],
            "percentage_12": user[20],
            "marksheet_12": user[21],
            "school_name_10": user[22],
            "percentage_10": user[23],
            "marksheet_10": user[24],
            "is_active": user[25]
        }

    def get(self):
        data = UserData.parser.parse_args()

        user = User(None, None, None, data['email'], data['password']).user_authentication()
        if user:
            return {"user": self.json(user)}, 200
        else:
            return {"message": "user not found!"}, 404


class UserDataList(Resource):

    @staticmethod
    def get():
        users = User(None, None, None, None, None, None, None, None, None, None).find_all_users()

        all_users = []

        for user in users:
            all_users.append(UserData.json(user))

        if all_users:
            return {"all_users": all_users}, 200
        else:
            return {"message": "No user was found!"}, 404