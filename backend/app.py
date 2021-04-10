import os
from flask_app import app
from dotenv import load_dotenv
from flask_restful import Api as API
from models.user import User, UserRegister, UserModification, UserData, UserDataList
from models.company import Company, JobRegister, JobData, JobModification, JobDataList
from models.user_company import UserCompany, UserApplication, UserApplicationsList, CompanyAppliedList, CheckUserApplicationsStatus


load_dotenv(".env")
app.secret_key = os.getenv("APP_SECRET_KEY")


api = API(app)


def create_tables():
    User(None, None, None, None, None, None).create_table()
    Company(None, None, None, None, None, None, None, None, None, None, None).create_table()
    UserCompany(None, None, None).create_table()


@app.route('/')
def hello_world():
    return "Hello World"


api.add_resource(UserData, '/user')
api.add_resource(JobData, '/job')

api.add_resource(UserDataList, '/allusers')
api.add_resource(JobDataList, '/alljobs')

api.add_resource(UserRegister, '/user/register')
api.add_resource(JobRegister, '/job/register')

api.add_resource(UserModification, '/user/update')
api.add_resource(JobModification, '/job/update')

api.add_resource(UserApplication, '/applyforopening')
api.add_resource(CompanyAppliedList, '/companyallapplications')
api.add_resource(UserApplicationsList, '/userallapplications')
api.add_resource(CheckUserApplicationsStatus, '/applicationstatus')

create_tables()

if __name__ == '__main__':
    app.run()
