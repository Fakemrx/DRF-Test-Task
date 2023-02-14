from django.test import Client
from django.conf import settings

if settings.DEBUG:
    def check_acceptable_response():
        c = Client()
        response = c.get('')
        print(response.status_code)
        return response.status_code


    assert check_acceptable_response() == 200
    print('Tests are done!')
