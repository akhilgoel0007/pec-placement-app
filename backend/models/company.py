# For duration send full_time for placement opening

from db_config import mysql
from flask_restful import Resource, reqparse


class Company:
    def __init__(self, _id, profile_name, company_name, location, job_description, offer_type, stipend, ctc, duration):
        self.id = _id
        self.ctc = ctc
        self.stipend = stipend
        self.location = location
        self.duration = duration
        self.offer_type = offer_type
        self.profile_name = profile_name
        self.company_name = company_name
        self.job_description = job_description

    @staticmethod
    def create_table():
        """Create Company Table."""

        connection = mysql.connect()
        cursor = connection.cursor()

        create_company_table = "CREATE TABLE IF NOT EXISTS company (" \
                               "id INT AUTO_INCREMENT PRIMARY KEY," \
                               "profile_name TEXT NOT NULL," \
                               "company_name TEXT NOT NULL," \
                               "location TEXT NOT NULL," \
                               "job_description TEXT NOT NULL," \
                               "offer_type TEXT NOT NULL," \
                               "stipend TEXT NOT NULL," \
                               "ctc TEXT NOT NULL," \
                               "duration TEXT NOT NULL" \
                               ");"

        cursor.execute(create_company_table)
        connection.commit()
        connection.close()

    @staticmethod
    def find_by_id(_id):
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM company WHERE id={_id}")
        company = cursor.fetchone()

        return company if company else None

    @staticmethod
    def find_all_companies():
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM company")
        companies = cursor.fetchall()

        return companies if companies else None


class JobRegister(Resource):
    """Add New Job in Database"""

    parser = reqparse.RequestParser()

    parser.add_argument("profile_name", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("company_name", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("location", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("job_description", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("offer_type", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("stipend", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("ctc", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("duration", type=str, required=True, help="This field cannot be blank")

    @staticmethod
    def post():
        data = JobRegister.parser.parse_args()

        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO company (profile_name, company_name, location, job_description, offer_type, stipend, ctc, duration) VALUES ('{data['profile_name']}', '{data['company_name']}', '{data['location']}', '{data['job_description']}', '{data['offer_type']}', '{data['stipend']}', '{data['ctc']}', '{data['duration']}')")

        connection.commit()
        connection.close()

        return {"message": "Job created successfully."}, 201


class JobModification(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("id", type=int, required=True, help="This field cannot be blank")
    parser.add_argument("profile_name", type=str, required=False)
    parser.add_argument("company_name", type=str, required=False)
    parser.add_argument("location", type=str, required=False)
    parser.add_argument("job_description", type=str, required=False)
    parser.add_argument("offer_type", type=str, required=False)
    parser.add_argument("stipend", type=str, required=False)
    parser.add_argument("ctc", type=str, required=False)
    parser.add_argument("duration", type=str, required=False)

    @staticmethod
    def add_response(response, status, field):
        if status:
            response[field] = 'updated'
        else:
            response[field] = 'update_failed'
        return response

    def patch(self):
        data = JobModification.parser.parse_args()
        response = {}

        if data['id']:
            if data['profile_name']:
                response = self.add_response(response, self.update(data['id'], 'profile_name', data['profile_name']), "profile_name")
            if data['company_name']:
                response = self.add_response(response, self.update(data['id'], 'company_name', data['company_name']), "company_name")
            if data['location']:
                response = self.add_response(response, self.update(data['id'], 'location', data['location']), "location")
            if data['job_description']:
                response = self.add_response(response, self.update(data['id'], 'job_description', data['job_description']), "job_description")
            if data['offer_type']:
                response = self.add_response(response, self.update(data['id'], 'offer_type', data['offer_type']), "offer_type")
            if data['stipend']:
                response = self.add_response(response, self.update(data['id'], 'stipend', data['stipend']), "stipend")
            if data['ctc']:
                response = self.add_response(response, self.update(data['id'], 'ctc', data['ctc']), "ctc")
            if data['duration']:
                response = self.add_response(response, self.update(data['id'], 'duration', data['duration']), "duration")
            return {"message": "Job opening found!", "update_status": response}, 202
        else:
            return {"message": "Job opening was not found!"}, 401

    @classmethod
    def update(cls, job_opening_id, field, field_value):
        connection = mysql.connect()
        cursor = connection.cursor()

        if field in ['profile_name', 'company_name', 'location', 'job_description', 'offer_type', 'stipend', 'ctc', 'duration']:
            cursor.execute(f"UPDATE company SET {field}='{field_value}' WHERE id={job_opening_id}")
        else:
            connection.commit()
            connection.close()
            return False

        connection.commit()
        connection.close()
        return True


class JobData(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("id", type=str, required=True, help="This field cannot be blank")

    @staticmethod
    def json(user):
        return {
            "profile_name": user[1],
            "company_name": user[2],
            "location": user[3],
            "job_description": user[4],
            "offer_type": user[5],
            "stipend": user[6],
            "ctc": user[7],
            "duration": user[8],
        }

    def get(self):
        data = JobModification.parser.parse_args()
        company = Company.find_by_id(data['id'])

        if company:
            return {"job_opening": self.json(company)}, 200
        else:
            return {"message": "Job opening not found!"}, 404


class JobDataList(Resource):

    @staticmethod
    def get():
        companies = Company(None, None, None, None, None, None, None, None, None).find_all_companies()

        all_companies = []

        for company in companies:
            json_company = JobData.json(company)
            json_company['id'] = company[0]
            all_companies.append(json_company)

        if all_companies:
            return {"all_job_opening": all_companies}, 200
        else:
            return {"message": "No job opening was found!"}, 404
