# coding: utf-8
import cx_Oracle
import json
import sys
#'bsc_emp_lh/bsc_emp_lh@10.10.10.37/orcl'
# 'ZABBIX/ZABBIX@10.1.3.180/orcl'
db = cx_Oracle.connect('bsc_emp_lh/bsc_emp_lh@10.10.10.37/orcl11')
cr = db.cursor()
sql="SELECT tablespace_name as colname , file_id, file_name, round(bytes / (1024 * 1024), 0) total_space FROM dba_data_files ORDER BY tablespace_name"
cr.execute(sql)
rs=cr.fetchall()
def discover():
    reinn = []
    for i in rs:
        # reinn={"{#SQL_NAME_COL}",i["username"]}
        reinn += [{'{#SQL_NAME_COL}': i[0]}]
    #print reinn

    result = {"data": reinn}
    # 避免转成json的时候 更换其编码
    rejson = json.dumps(result, ensure_ascii=False)
    print(rejson.encode('utf8'))

def monitor(key):
    for i in rs:
        if i[0] == key:
            print i[3]
#print rs
# for i in rs:
# #    print i
#     for s in range(len(i)):
#         print("TableSpace_Name:"+i[0]+"File_Id:"),
#         print(i[1]),
#         print("File_Name"+i[2]+"Total_Space"),
#         print(i[3])
# for i in rs:
#     print("TableSpace_Name:"+i[0]+"File_Id:"),
#     print(i[1]),
#     print("File_Name"+i[2]+"Total_Space"),
#     print(i[3])
#print(rs)
db.close()

if __name__=="__main__":
    #print type(sys.argv[1])
    #print sys.argv[1] == str(1)
    if sys.argv[1] == str(1):
        discover()
    else:
        monitor(sys.argv[1])
    #discover()

