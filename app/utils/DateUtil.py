# -*- coding: utf-8 -*-
from datetime import datetime, time, date
import time as ti
from flask import json

class DateTimeEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return datetime_to_string(o)
        elif isinstance(o, date):
            return date_to_string(o)
        elif isinstance(o, time):
            return time_to_string(o)
        elif isinstance(o, bytes):
            return o.decode('utf-8')

        return json.JSONEncoder.default(self, o)



def time_in_frame(start, t, end):
    start = time_to_strint(start)
    t =     time_to_strint(t)
    end =   time_to_strint(end)
    return t >= start and t <= end

def time_to_strint(t):
    return int(t.strftime("%H%M%S"))

def string_to_date(str):
    return datetime.strptime(str, '%Y-%m-%d').date()

def date_to_string(t):
    return t.strftime("%Y-%m-%d")

def string_to_time(str):
    return datetime.strptime(str, '%H:%M:%S').time()

def time_to_string(t):
    return t.strftime("%H:%M:%S")

def datetime_to_string(t):
    return t.strftime("%Y-%m-%d %H:%M:%S")



def now_datetime():
    return datetime.now()

def now_time():
    return datetime.now().time()

def now_datetime_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def now_date_string():
    return datetime.now().strftime("%Y-%m-%d")



def now_timestamp():
    return int(ti.time()*10000)


if __name__ == '__main__':
    print(now_datetime())
    print(now_timestamp())
    print(now_date_string())
