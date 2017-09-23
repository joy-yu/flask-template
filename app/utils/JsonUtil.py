# -*- coding: utf-8 -*-

import json
from app.utils.DateUtil import DateTimeEncoder

def object_2_json(obj):
    '''
    py字典、数据转成json字符转
    '''
    if obj is None:
        obj = {}
    return json.dumps(obj, cls=DateTimeEncoder)


def json_2_dict(json_str):
    '''
    json字符串转成dict，list数据结构
    '''
    try:
        return json.loads(json_str)
    except Exception:
        return None
