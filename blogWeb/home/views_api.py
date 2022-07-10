from urllib import response
from matplotlib.style import use
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong 4578'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username not found'
                raise Exception('User not found')

            if data.get('password') is None:
                response['message'] = 'password not found'
                raise Exception('password not found')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid use1r'
                raise Exception('invalid, user not found')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = "welcome"
                
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password not found')

        
        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()

class RegisterView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong 4578'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username not found'
                raise Exception('User not found')

            if data.get('password') is None:
                response['message'] = 'password not found'
                raise Exception('password not found')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'username already taken'
                raise Exception('invalid, user not found')

            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save() 
            response['status'] = 200
            response['message'] = "user created"
            

        
        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()
