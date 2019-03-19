#coding:utf-8
import urllib2
import sys
import traceback

def mea_query(url):
    try:
        res = urllib2.urlopen(url)
        html = res.read()
    except Exception:
        print("接口请求数据失败")
        print('traceback.format_exc():\n%s' % traceback.format_exc())
    else:
        print(html)

if __name__ == "__main__":
    mea_query(sys.argv[1])
