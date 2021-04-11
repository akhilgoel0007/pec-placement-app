from db_config import mysql
from flask_restful import Resource, reqparse
from models.user import User, UserData
from models.company import Company, JobData


class UserCompany:
    def __init__(self, _id, user_id, company_id):
        self.id = _id
        self.user_id = user_id
        self.company_id = company_id

    @staticmethod
    def create_table():
        """Create Company Table."""

        connection = mysql.connect()
        cursor = connection.cursor()

        create_user_company_table = "CREATE TABLE IF NOT EXISTS user_company (" \
                                    "id INT AUTO_INCREMENT PRIMARY KEY," \
                                    "user_id INT NOT NULL," \
                                    "company_id INT NOT NULL," \
                                    "FOREIGN KEY(user_id) REFERENCES users(id)," \
                                    "FOREIGN KEY(company_id) REFERENCES company(id)" \
                                    ");"

        cursor.execute(create_user_company_table)
        connection.commit()
        connection.close()

    def check_application_status(self):
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM user_company WHERE user_id={self.user_id} AND company_id={self.company_id}")
        result = cursor.fetchone()

        connection.close()

        return True if result else False

    def find_all_applicants(self):
        """Find all the applicants who have applied to a particular opening."""

        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM user_company WHERE company_id={self.company_id}")
        companies = cursor.fetchall()

        connection.close()

        return companies if companies else None

    def find_all_applied_companies(self):
        """Find all the companies in which user has applied."""

        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM user_company WHERE user_id={self.user_id}")
        users = cursor.fetchall()

        connection.close()

        return users if users else None


class UserApplication(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("user_email", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("company_id", type=int, required=True, help="This field cannot be blank")

    @staticmethod
    def post():
        data = UserApplication.parser.parse_args()

        connection = mysql.connect()
        cursor = connection.cursor()

        user_id = User(None, None, None, data['user_email'], None).find_id_by_email()

        if user_id:
            cursor.execute(f"INSERT INTO user_company (user_id, company_id) VALUES ({user_id}, {data['company_id']});")
            connection.commit()
            connection.close()

            return {"message": "Applied for the opening!"}, 201
        else:
            connection.close()

            return {"message": "Not a valid user!"}, 404


class UserApplicationsList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("user_email", type=str, required=True, help="This field cannot be blank")

    @staticmethod
    def get():
        data = UserApplicationsList.parser.parse_args()

        user_id = User(None, None, None, data['user_email'], None).find_id_by_email()
        companies = UserCompany(None, user_id, None).find_all_applied_companies()

        all_companies = []
        if companies:
            for company in companies:
                all_companies.append(JobData.json(Company.find_by_id(company[2])))

        return {"all_applications": all_companies}, 200


class CompanyAppliedList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("company_id", type=int, required=True, help="This field cannot be blank")

    @staticmethod
    def get():
        data = CompanyAppliedList.parser.parse_args()

        users = UserCompany(None, None, data['company_id']).find_all_applicants()

        all_users = []
        if users:
            for user in users:
                all_users.append(UserData.json(User.find_by_id(user[1])))

        return {"all_applied_users": all_users}, 200


class CheckUserApplicationsStatus(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("user_email", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("company_id", type=int, required=True, help="This field cannot be blank")

    @staticmethod
    def get():
        data = UserApplication.parser.parse_args()

        user_id = User(None, None, None, data['user_email'], None).find_id_by_email()
        applicationStatus = UserCompany(None, user_id, data['company_id']).check_application_status()

        if applicationStatus:
            return {"status": "applied"}, 200
        else:
            return {"status": "not_applied"}, 200
