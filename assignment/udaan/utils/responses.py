from rest_framework.response import Response


def success_response(status, msg, data, *args, **kwargs):
    response = {
        "status": "success",
        "msg": msg,
        "data": data
    }
    return Response(data=response, status=status)


def error_response(status, msg, data, *args, **kwargs):
    response = {
        "status": "error",
        "msg": msg,
        "data": data
    }
    return Response(data=response, status=status)
