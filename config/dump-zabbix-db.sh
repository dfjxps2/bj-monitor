#!/bin/bash
PASSWORD=123456
HOST=localhost
USER=root
DATABASE=zabbix
DB_FILE=zabbix-dump.sql
EXCLUDED_TABLES=(
history_uint
history_text
history_str
history_log
history
trends_uint
trends
)

IGNORED_TABLES_STRING=''
for TABLE in "${EXCLUDED_TABLES[@]}"
do :
   IGNORED_TABLES_STRING+=" --ignore-table=${DATABASE}.${TABLE}"
done

#echo "Dump structure"
#mysqldump --host=${HOST} --user=${USER} --password=${PASSWORD} --single-transaction --no-data --routines ${DATABASE} > ${DB_FILE}

echo "Dump content"
mysqldump --host=${HOST} --user=${USER} --password=${PASSWORD} ${DATABASE} --default-character-set=utf8 --skip-triggers ${IGNORED_TABLES_STRING} >> ${DB_FILE}
