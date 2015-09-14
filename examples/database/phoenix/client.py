# -*- encoding: utf-8 -*-
__author__ = 'tao'

import jaydebeapi

class PhoenixClient:
    def __init__(self, dirver, zkNode, zkPort, logger=None):
        self.conn = jaydebeapi.connect("org.apache.phoenix.jdbc.PhoenixDriver",
                                       ["jdbc:phoenix:" + zkNode + ":" + zkPort],
                                       dirver)
        self.curs = self.conn.cursor()
        self.logger = logger



    def fetchAll(self, sql):
        self.curs.execute(sql)
        return self.curs.fetchall()



    def addColumn(self, table, column, ctype):
        sql = 'alter table "' + table + '" add "' + column + '" ' + ctype
        self.logInfo("SQL is [" + sql + "]")
        self.curs.execute(sql)



    def execute(self, sql):
        self.curs.execute(sql)
        # 注意： 如果不进行commit，则`upsert`操作会没有效果
        self.conn.commit()



    def close(self):
        self.conn.close()



    def logInfo(self, msg):
        if None == self.logger:
            print msg
        else:
            self.logger.info(msg)