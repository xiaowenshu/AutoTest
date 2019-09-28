#!/usr/bin/python
# encoding:utf-8

import pymysql
import socket
import configparser
from common.logging_config import logging_config
import logging
import os


class mysql_connect():
    def __init__(self):
        self.mysql_connect = None
        self.m_cursor = None
        self.m_sqlob = None
        logging_config().set_logging_config(filename='mysql_connect')

    def get_sql_parameters(self):
        #         print(os.path.dirname(__file__)+'\common_config.cfg')
        self.cp = configparser.ConfigParser()
        self.cp.read(os.path.dirname(__file__) + '\common_config.cfg')
        self.post = self.cp.get('MYSQL', 'PORT')
        self.charset = self.cp.get('MYSQL', 'CHARSET')
        if self.cp.get('MYSQL', 'ENV') == 'QA':
            self.host = self.cp.get('MYSQL', 'QA_HOST')
            self.user = self.cp.get('MYSQL', 'QA_USER')
            self.passwd = self.cp.get('MYSQL', 'QA_PASSWD')
            self.database = self.cp.get('MYSQL', 'QA_DATA_BASE')

        elif self.cp.get('MYSQL', 'ENV') == 'UAT':
            self.host = self.cp.get('MYSQL', 'UAT_HOST')
            self.user = self.cp.get('MYSQL', 'UAT_USER')
            self.passwd = self.cp.get('MYSQL', 'UAT_PASSWD')
            self.database = self.cp.get('MYSQL', 'UAT_DATA_BASE')

        elif self.cp.get('MYSQL', 'ENV') == 'PRO':
            self.host = self.cp.get('MYSQL', 'PRO_HOST')
            self.user = self.cp.get('MYSQL', 'PRO_USER')
            self.passwd = self.cp.get('MYSQL', 'PRO_PASSWD')
            self.database = self.cp.get('MYSQL', 'PRO_DATA_BASE')

    def connect_sql(self):
        try:
            self.get_sql_parameters()
            self.mysql_connect = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.database,
                                                 charset=self.charset)
            logging.info('mysql connect successfully')
            self.m_cursor = self.mysql_connect.cursor()
        except Exception as e:
            logging.error('mysql_connect failed please check the mysql connection')
        return self.m_cursor

    def execute_sql(self, sql):
        try:
            self.connect_sql()
            self.m_cursor.execute(sql)
            logging.info(sql + '  execute successfully')
            self.m_sqlob = self.m_cursor.fetchall()

        except Exception as e:
            logging.error(sql + '  execute error')
        return self.m_sqlob

    def rollback(self):
        self.mysql_connect.rollback()

    def commit_sql(self):
        self.mysql_connect.commit()

    def close_sql(self):
        self.mysql_connect.close()

# if __name__=='__main__':
#     m1=mysql_connect()
#     m1.connect_sql()