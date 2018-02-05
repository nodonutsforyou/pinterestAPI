import os


def before_all(context):
    print("before all")
    context.apiVersion = os.getenv('API_VERSION', 'v1')
    context.authCode = os.getenv('TOKEN', '')
    #TODO this assert is a wrong way to check if we got the parameter - but I do not have time to find the best one
    assert len(context.authCode) > 0, "TOKEN is not set - you need to set TOKEN environment variable"
    context.userId = os.getenv('USERID', '')
    assert len(context.userId) > 0, "USERID is not set - you need to set USERID environment variable"
    context.host = os.getenv('HOST', 'https://api.pinterest.com')