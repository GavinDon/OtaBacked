import time
import datetime


def isNotEmpty(s):
    if s is not None and s != '':
        return True
    else:
        return False


def now_date():
    e_date = datetime.datetime.now().date()
    s_date = e_date - datetime.timedelta(days=180)
    return s_date.strftime('%Y-%m-%d'), e_date.strftime('%Y-%m-%d')
