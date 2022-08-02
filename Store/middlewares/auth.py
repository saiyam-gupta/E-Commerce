from urllib import response
from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        returnUrl = request.META['PATH_INFO']

        if request.session.get("customer"):
            pass
        else:
            return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware