#coding: utf-8
import pymysql
import ConfigParser
import json
import logging.handlers
import re
import requests

class myconf(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr
def work():

    # conf = myconf()
    # conf.read("/etc/zabbix/scripts/config/db.conf")
    # option = conf.sections()
    # host = conf.get(option[0], 'host')
    # port = int(conf.get('db', 'port'))
    # user = conf.get('db', 'user')
    # db = conf.get('db', 'db')
    # passwd = conf.get('db', 'passwd')
    # charset = conf.get('db', 'charset')

    host = '10.10.10.42'
    port = 3306
    user = 'root'
    db = 'portaldb'
    passwd = '123456'
    charset = 'utf8'
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()
    #游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql= ""
    row_count = cursor.execute(sql)
    row_3 = cursor.fetchall()
    logger = confLog()
    #print(row_3)
    if row_count == 0:
        print("最近无用户操作")
    else:
        for i in row_3:
            print 1



    # for i in range(len(row_3)):
    #     print(row_3)

    conn.commit()
    cursor.close()
    conn.close()
def sendlog(sql):
    '''发送日志'''
    logger = confLog()
    logger.info("[%s]:[%s]:[%s]:[%s]:[%s]:[%s]","admin","1",sql,'2018-12-28 10:06:30','12','100')


def Get_Session(URL,DATA,HEADERS):
    '''保存登录参数'''
    ROOM_SESSION  = requests.Session()
    ROOM_SESSION.post(URL,data=DATA,headers=HEADERS,verify=False)
    return ROOM_SESSION

def getLog():
    '''从接口拿到json数据'''
    # LOGIN_URL = 'https://localhost:8443/cas/login'  #请求的URL地址
    LOGIN_URL = "http://localhost:8080/portal/druid/submitLogin"
    DATA = {"loginUsername": 'druid', "loginPassword": 'bounter'}  # 登录系统的账号密码,也是我们请求数据

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    # 模拟登陆的浏览器
    }
    RES = requests.post(LOGIN_URL, data=DATA, headers=HEADERS, verify=False)  # 模拟登陆操作

    SESSION = Get_Session(LOGIN_URL, DATA, HEADERS)
    # 保存session后再次请求对应的地址
    RES2 = SESSION.get("http://localhost:8080/portal/druid/sql.json")
    #print(RES2.text)
    sqllog_json = json.loads(RES2)
    print sqllog_json
    #清空sql日志
    requests.get("http://localhost:8080/portal/druid/reset-all.json")

def getsqlLog():
    '''从接口拿到sql日志的json数据'''
    log_json = json.loads(requests.get("http://localhost:8080/portal/druid/sql.json").text)
    #print log_json
    # situation 1 有sql日志
    if log_json['Content'] != None:
        for s in log_json['Content']:
            print s['SQL']
           #sendlog(['SQL'])
        # 收集完毕之后 清空sql日志 避免太臃肿的日志]
        requests.get("http://localhost:8080/portal/druid/reset-all.json")
    # situation 2 没sql日志 {"ResultCode":1,"Content":null}
    else:
        print("目前没日志")

def confLog():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    fh = logging.handlers.SysLogHandler(('10.10.10.42', 6696), logging.handlers.SysLogHandler.LOG_AUTH)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #fh.setFormatter(formatter)
    logger.addHandler(fh)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    #console.setFormatter(formatter)
    logger.addHandler(console)
    return logger

if __name__ == '__main__':
    getsqlLog()


#mysqladmin -uroot -proot status