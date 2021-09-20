from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser =RequestParser()
parser.add_argument("email",type='str')

class user(Resource):
   required=True
   help='please put your email'

   '''
   user endpoints
   '''
   def post(self):
       args = parser.parse_args()
       args =request.get_json()
       email = args["email"]
       password =args["password"]
       confirm_password= args["confirm_password"]

       newsUser= UserModels(email,password,confirm_password)
       newsUser.save_user()

       return{
           "message":"user registered successfully",
           "user":newsUser.__dict__

       }
