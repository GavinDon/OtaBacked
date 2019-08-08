from flask import Response
import json


class ErrorResponse(Response):
    def __init__(self, err_code=1, error_msg=''):
        result = json.dumps(dict(code=err_code, msg=error_msg, data=None))
        Response.__init__(self, result, mimetype='application/json')


class SuccessResponse(Response):
    def __init__(self, data, msg='成功', total=0):
        result = json.dumps(dict(code=0, msg=msg, data=data, total=total))
        Response.__init__(self, result, mimetype='application/json')


class SucNoticeResponse(Response):
    def __init__(self, msg='成功'):
        result = json.dumps(dict(code=0, msg=msg, data=None))
        Response.__init__(self, result, mimetype='application/json')


class UnauthorizedResponse(Response):
    def __init__(self):
        result = json.dumps(dict(code=4001, msg='未登陆', data=None))
        Response.__init__(self, response=result, mimetype='application/json')
