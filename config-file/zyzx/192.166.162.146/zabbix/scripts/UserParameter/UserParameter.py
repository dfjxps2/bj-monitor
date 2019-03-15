# coding: utf-8
import sys
import json
import requests
import traceback

def mea_query(url):
    try:
        rs = requests.get(url)
        content = rs.text
        body = json.loads(content)
        l = body["metrics"]
    except Exception:
        print("接口请求数据失败")
        print('traceback.format_exc():\n%s' % traceback.format_exc())
    else:
        # 遍历列表
        for i in l:
            # print(i["values"])
            s = i["values"]
            for key, value in s.items():
                print(value.encode('utf8'))

if __name__ == "__main__":
    mea_query(sys.argv[1])
    #mea_query("http://10.10.10.35:7788/smcs-api/monitor/v1/timeline/metrics?metricNames=state&appId=YARN/NodeManager")
    #mea_query("http://10.10.10.23/monitor/v1/timeline/metrics?metricNames=serviceCalllog&hostName=a&appId=b&startTime=2018-11-8 12:39:00&endTime=2018-11-8 12:40:00&precision=10")