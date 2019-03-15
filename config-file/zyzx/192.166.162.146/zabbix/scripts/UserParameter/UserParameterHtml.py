#coding:utf-8
import urllib2
import sys
import traceback


def mea_query(url):
    try:
        res = urllib2.urlopen(url)
        #print(res)
        html = res.read()
        #html = res.read().decode('utf-8')
        #print (html)
    except Exception:
        print("接口请求数据失败")
        print('traceback.format_exc():\n%s' % traceback.format_exc())
    else:
        #print(html)
        print(html)
if __name__ == "__main__":
    url=sys.argv[1]
    mea_query(url)
    #print(sys.argv[1])
    #mea_query(sys.argv[1])
    #mea_query("http://192.166.162.146:7788/smcs-api/monitor/v1/timeline/summary?metricNames=ComponentsIP&appId=MAPREDUCE2")
    #http://192.166.162.146:7788/smcs-api/monitor/v1/timeline/summary?metricNames=ComponentsIP&appId=Smcs
