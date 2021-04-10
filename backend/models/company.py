# For duration send full_time for placement opening

from db_config import mysql
from flask_restful import Resource, reqparse


class Company:
    """
        [+] Add job status
        [+] Add company icon.
    """
    
    def __init__(self, _id, profile_name, company_name, location, job_description, offer_type, stipend, ctc, duration, application_open_date, application_close_date, company_icon=None, min_cg=None, min_10_percentage=None, min_12_percentage=None, max_backlogs=None, is_active=None):
        self.id = _id
        self.ctc = ctc
        self.min_cg = min_cg
        self.stipend = stipend
        self.location = location
        self.duration = duration
        self.is_active = is_active
        self.offer_type = offer_type
        self.company_icon = company_icon
        self.profile_name = profile_name
        self.company_name = company_name
        self.max_backlogs = max_backlogs
        self.job_description = job_description
        self.min_10_percentage = min_10_percentage
        self.min_12_percentage = min_12_percentage
        self.application_open_date = application_open_date
        self.application_close_date = application_close_date

    @staticmethod
    def create_table():
        """Create Company Table."""

        connection = mysql.connect()
        cursor = connection.cursor()

        create_company_table = "CREATE TABLE IF NOT EXISTS company (" \
                               "id INT AUTO_INCREMENT PRIMARY KEY," \
                               "company_icon TEXT," \
                               "profile_name TEXT NOT NULL," \
                               "company_name TEXT NOT NULL," \
                               "location TEXT NOT NULL," \
                               "job_description TEXT NOT NULL," \
                               "offer_type TEXT NOT NULL," \
                               "stipend TEXT NOT NULL," \
                               "ctc TEXT NOT NULL," \
                               "duration TEXT NOT NULL," \
                               "min_cg FLOAT," \
                               "min_10_percentage INT," \
                               "min_12_percentage INT," \
                               "max_backlogs INT," \
                               "application_close_date TEXT," \
                               "application_open_date TEXT," \
                               "is_active BOOLEAN DEFAULT TRUE" \
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

    parser.add_argument("company_icon", type=str, required=False)
    parser.add_argument("profile_name", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("company_name", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("location", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("job_description", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("offer_type", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("stipend", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("ctc", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("duration", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("min_cg", type=float, required=False)
    parser.add_argument("min_10_percentage", type=int, required=False)
    parser.add_argument("min_12_percentage", type=int, required=False)
    parser.add_argument("max_backlogs", type=int, required=False)
    parser.add_argument("application_open_date", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("application_close_date", type=str, required=True, help="This field cannot be blank")

    @staticmethod
    def post():
        data = JobRegister.parser.parse_args()

        connection = mysql.connect()
        cursor = connection.cursor()

        company_icon = None
        min_cg = None
        min_10_percentage = None
        min_12_percentage = None
        max_backlogs = None

        if data['company_icon']:
            company_icon = data['company_icon']
        if data['min_cg']:
            min_cg = data['min_cg']
        if data['min_10_percentage']:
            min_10_percentage = data['min_10_percentage']
        if data['min_12_percentage']:
            min_12_percentage = data['min_12_percentage']
        if data['max_backlogs']:
            max_backlogs = data['max_backlogs']

        query = f"INSERT INTO " \
                f"company (company_icon, profile_name, company_name, location, job_description, offer_type, stipend, ctc, duration, min_cg, min_10_percentage, min_12_percentage, max_backlogs, application_open_date, application_close_date) " \
                f"VALUES ('{company_icon}', '{data['profile_name']}', '{data['company_name']}', '{data['location']}', '{data['job_description']}', '{data['offer_type']}', '{data['stipend']}', '{data['ctc']}', '{data['duration']}', {min_cg}, {min_10_percentage}, {min_12_percentage}, {max_backlogs}, '{data['application_open_date']}', '{data['application_close_date']}')"

        cursor.execute(query)

        connection.commit()
        connection.close()

        return {"message": "Job created successfully."}, 201


class JobModification(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("id", type=int, required=True, help="This field cannot be blank")
    parser.add_argument("company_icon", type=str, required=False)
    parser.add_argument("profile_name", type=str, required=False)
    parser.add_argument("company_name", type=str, required=False)
    parser.add_argument("location", type=str, required=False)
    parser.add_argument("job_description", type=str, required=False)
    parser.add_argument("offer_type", type=str, required=False)
    parser.add_argument("stipend", type=str, required=False)
    parser.add_argument("ctc", type=str, required=False)
    parser.add_argument("duration", type=str, required=False)
    parser.add_argument("min_cg", type=float, required=False)
    parser.add_argument("min_10_percentage", type=int, required=False)
    parser.add_argument("min_12_percentage", type=int, required=False)
    parser.add_argument("max_backlogs", type=int, required=False)
    parser.add_argument("application_open_date", type=str, required=False)
    parser.add_argument("application_close_date", type=str, required=False)
    parser.add_argument("is_active", type=bool, required=False)

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
            if data['company_icon']:
                response = self.add_response(response, self.update(data['id'], 'company_icon', data['company_icon']), "company_icon")
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
            if data['min_cg']:
                response = self.add_response(response, self.update(data['id'], 'min_cg', data['min_cg']), "min_cg")
            if data['min_10_percentage']:
                response = self.add_response(response, self.update(data['id'], 'min_10_percentage', data['min_10_percentage']), "min_10_percentage")
            if data['min_12_percentage']:
                response = self.add_response(response, self.update(data['id'], 'min_12_percentage', data['min_12_percentage']), "min_12_percentage")
            if data['max_backlogs']:
                response = self.add_response(response, self.update(data['id'], 'max_backlogs', data['max_backlogs']), "max_backlogs")
            if data['application_open_date']:
                response = self.add_response(response, self.update(data['id'], 'application_open_date', data['application_open_date']), "application_open_date")
            if data['application_close_date']:
                response = self.add_response(response, self.update(data['id'], 'application_close_date', data['application_close_date']), "application_close_date")
            if data['is_active'] == False or data['is_active'] == True:
                response = self.add_response(response, self.update(data['id'], 'is_active', data['is_active']), "is_active")
            return {"message": "Job opening found!", "update_status": response}, 202
        else:
            return {"message": "Job opening was not found!"}, 401

    @classmethod
    def update(cls, job_opening_id, field, field_value):
        connection = mysql.connect()
        cursor = connection.cursor()

        if field in ['company_icon', 'profile_name', 'company_name', 'location', 'job_description', 'offer_type', 'stipend', 'ctc', 'duration', 'application_open_date', 'application_close_date']:
            cursor.execute(f"UPDATE company SET {field}='{field_value}' WHERE id={job_opening_id}")
        elif field in ['min_cg', 'min_10_percentage', 'min_12_percentage', 'max_backlogs', 'is_active']:
            cursor.execute(f"UPDATE company SET {field}={field_value} WHERE id={job_opening_id}")
        else:
            connection.commit()
            connection.close()
            return False

        connection.commit()
        connection.close()
        return True


class JobData(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("id", type=int, required=True, help="This field cannot be blank")

    @staticmethod
    def json(user):
        return {
            "company_icon": user[1],
            "profile_name": user[2],
            "company_name": user[3],
            "location": user[4],
            "job_description": user[5],
            "offer_type": user[6],
            "stipend": user[7],
            "ctc": user[8],
            "duration": user[9],
            "min_cg": user[10],
            "min_10_percentage": user[11],
            "min_12_percentage": user[12],
            "max_backlogs": user[13],
            "application_open_date": user[14],
            "application_close_date": user[15],
            "is_active": user[16]
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
        companies = Company(None, None, None, None, None, None, None, None, None, None, None).find_all_companies()

        all_companies = []

        for company in companies:
            json_company = JobData.json(company)
            json_company['id'] = company[0]
            all_companies.append(json_company)

        if all_companies:
            return {"all_job_opening": all_companies}, 200
        else:
            return {"message": "No job opening was found!"}, 404
