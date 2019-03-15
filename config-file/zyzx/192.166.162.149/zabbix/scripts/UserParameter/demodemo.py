# coding: utf-8
import cx_Oracle

db=cx_Oracle.connect('bsc_emp_lh/bsc_emp_lh@192.166.162.65/orcl')
cr=db.cursor()
#sql='SELECT t.tablespace_name, round(SUM(bytes / (1024 * 1024)), 0) ts_size FROM dba_tablespaces t, dba_data_files d WHERE t.tablespace_name = d.tablespace_name GROUP BY t.tablespace_name'
sql='SELECT total.tablespace_name,Round(total.MB, 2) AS Total_MB,Round(total.MB - free.MB, 2) AS Used_MB,Round(( 1 - free.MB / total.MB ) * 100, 2) AS Used_Pct FROM (SELECT tablespace_name,Sum(bytes) / 1024 / 1024 AS MB FROM   dba_free_space GROUP  BY tablespace_name) free,(SELECT tablespace_name,Sum(bytes) / 1024 / 1024 AS MB FROM   dba_data_files GROUP  BY tablespace_name) total WHERE  free.tablespace_name = total.tablespace_name'
cr.execute(sql)
rs=cr.fetchall()
print rs
#for i in rs:
#    print i
#    for s in range(len(i)):
#    print("TableSpace_Name:"+i[0]+"Ts:"),
#    print(i[1])
#print(rs)
db.close()


