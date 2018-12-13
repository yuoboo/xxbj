from pymongo import MongoClient
import time
import json


class GetSysData(object):
    MG_COLLECTION = 'sys_info'
    MG_IP = "134.175.101.39"
    MG_PORT = "27017"
    MG_USER = "user"
    MG_PASSWD = "passwd"

    def __init__(self, hostname, monitor_item, timing, no=0):
        self.hostname = hostname
        self.monitor_item = monitor_item
        self.timing = timing
        self.no = no

    @classmethod
    def connect_db(cls):
        mongodb_ip = cls.MG_IP
        mongodb_port = cls.MG_PORT
        mongodb_user = cls.MG_USER
        mongodb_pwd = cls.MG_PASSWD
        if mongodb_user:
            uri = 'mongodb://'+mongodb_user+':'+mongodb_pwd+'@'+mongodb_ip+':'+mongodb_port+'/'+cls.db
            client = MongoClient(uri)
        else:
            client = MongoClient(mongodb_ip, int(mongodb_port))
        return client

    def get_data(self):
        client = self.connect_db()
        db = client[self.MG_COLLECTION]
        collection = db[self.hostname]
        now_time = int(time.time())
        find_time = now_time-self.timing
        cursor = collection.find({'timestamp': {'$gte': find_time}}, {self.monitor_item: 1, "timestamp": 1}).limit(self.no)
        return cursor
