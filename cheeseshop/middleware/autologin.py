from django.contrib import auth

class AutoLoginMiddleware(object):
    def process_request(self, request):
        if request.user.is_anonymous():
            auth.login(request, auth.authenticate(
                    username="nferrier", 
                    password="1"
                    ))
    

# End
