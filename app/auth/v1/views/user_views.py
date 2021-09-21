from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()
parser.add_argument("username",type='str')

class User(Resource):
    required=True
    help='please put your email'

    '''
    user endpoints
    '''
    def post(self):
        args = parser.parse_args()
        args =request.get_json()
        username = args["username"]
        password =args["password"]
        confirm_password= args["confirm_password"]
        work =args["work"]
        worktimer=args["worktime"]
        breaktime=args["breaktime"]
       
        newsUser= UserModels(username,password,confirm_password,work,worktimer,breaktime)
        newsUser.save_user()

        return{
           "message":"user registered successfully",
           "user":newsUser.__dict__
        }, 201

    def get(self):
        pass
