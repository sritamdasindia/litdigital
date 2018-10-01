from django.shortcuts import render

# Create your views here.


def register( request ):

    if 'who' in request. POST :
        fname = request . POST [ 'fname']
        lname = request . POST [ 'lname']
        email = request . POST [ 'email']
        password = request . POST [ 'password']

        if request . POST ['who'] == 'staff':
            return render ( request , 'registration/staffregister.html', )
        elif request . POST ['who'] == 'student':
            return render ( request, 'registration/studentregister.html', {'fname' : fname , 'lname' : lname, 'email':email, 'password' : password })

    return render ( request , 'registration/register.html')
