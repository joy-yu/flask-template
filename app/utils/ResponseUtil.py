from app.utils import JsonUtil

def standard_response(code, data):
    '''standard response
    '''
    rst = {}
    rst['code'] = code
    rst['data'] = data
    return JsonUtil.object_2_json(rst)
