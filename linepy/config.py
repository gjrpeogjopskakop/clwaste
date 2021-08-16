# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'
    LINE_LIFF_SEND              = 'https://api.line.me/message/v3/share'
    LINE_PERMISSION_API         = 'https://access.line.me/dialog/api/permissions'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'

    CHANNEL_ID = {
        'HELLO_WORLD': '1602289196',
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'ANDROID': '10.12.1',
        'IOS': '10.12.1',
        'ANDROIDLITE': '2.14.0',
        'DESKTOPWIN': '6.1.1',
        'DESKTOPMAC': '6.1.1',
        'IOSIPAD': '10.12.1',
        'CHROMEOS': '2.3.8',
        'DEFAULT': '10.12.0'
    }

    SYSTEM_VERSION = {
        'ANDROID': '10.0',
        'IOS': '13.5.1',
        'ANDROIDLITE': '10.0',
        'DESKTOPWIN': '10.0',
        'DESKTOPMAC': '10.15.1',
        'IOSIPAD': '13.5.1',
        'CHROMEOS': '83.0',
        'DEFAULT': '13.5.1'
    }

    APP_TYPE    = ApplicationType._VALUES_TO_NAMES[384]
    APP_VER     = '9.15.1'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'HAO_bot'
    SYSTEM_VER  = '11.2.5'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


    def __init__(self, appType=None):        
        self.APP_NAME = 'ANDROIDLITE\t2.16.0\tAndroid OS\t6.0.1;SECONDARY'        
        self.USER_AGENT = 'LLA/2.16.0 SM-N910U 6.0.1'
