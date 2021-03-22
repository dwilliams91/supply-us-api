import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from rest_framework.decorators import action



@csrf_exempt
def login_user(request):

    # get the post method information
    req_body = json.loads(request.body.decode())

    if request.method == 'POST':
        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            # get the token with the user
            token = Token.objects.get(user=authenticated_user)
            # if the user is_staff, return true
            if authenticated_user.is_staff:
                data = json.dumps(
                    {"valid": True, "token": token.key, "is_staff": True})
                if authenticated_user.is_superuser:
                    data = json.dumps(
                    {"valid": True, "token": token.key, "is_staff": True, "is_superuser":True})
            else:
                # send else send back false
                data = json.dumps(
                    {"valid": True, "token": token.key, "is_staff": False})

            return HttpResponse(data, content_type='application/json')
        else:
            
            data=json.dumps({"valid":False})
            return HttpResponse(data, content_type='application/json')



@csrf_exempt
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
        request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())
    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if req_body["is_staff"]==0:
        is_staff=False
        new_user = User.objects.create_user(
        password=req_body['password'],
        last_login=None,
        username=req_body['email'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        email=req_body['email'],
        is_staff=is_staff,
        is_active=True,
        date_joined=datetime.now()
    )
    else:
        is_staff=True
        new_user = User.objects.create_user(
        password=req_body['password'],
        last_login=None,
        username=req_body['email'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        email=req_body['email'],
        is_staff=is_staff,
        is_active=False,
        date_joined=datetime.now()
    )
    



    # Now save the extra info in the rareapi_rareuser table
    

    # Commit the user to the database by saving it
    new_user.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')

