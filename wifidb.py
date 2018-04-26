#-*- coding: utf-8 -*-
import pymysql

def InsertData(wifi,newwifi):
    try:
        conn = pymysql.connect(host='localhost', user='royce', password='cvl89804142', port=3306, db='ruckus', charset="utf8")
        cur = conn.cursor()
        COLstr = ''  # 列的字段
        ROWstr = ''  # 行字段

        ColumnStyle = ' CHAR(20)'


        for key in ["mac", "team_name", "team_user", "customer"]:
            COLstr = COLstr + ' ' + key + ColumnStyle + ','
            ROWstr = (ROWstr + '"%s"' + ',') % (newwifi.get(key))

            # 判断表是否存在，存在执行try，不存在执行except新建表，再insert
        try:
            cur.execute("SELECT * FROM  %s" % (wifi))
            cur.execute("INSERT INTO %s VALUES (%s)" % (wifi, ROWstr[:-1]))

        except pymysql.Error as e:
            cur.execute("CREATE TABLE %s (%s)" % (newwifi, COLstr[:-1]))
            cur.execute("INSERT INTO %s VALUES (%s)" % (newwifi, ROWstr[:-1]))
        conn.commit()
        cur.close()
        conn.close()

    except pymysql.Error as e:
        print
        "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
  #  newwifi = {"mac": "ff:ff:cc:bb:aa:55", "team_name": "喜樂隊", "team_user": "彭文豪", "customer": "裴玉貞"}
    newwifi = { "team_user": "彭豪", "team_name": "喜樂隊","mac": "ff:ff:cc:bb:aa:10","customer": "裴玉貞"}
    InsertData('wifi', newwifi)

