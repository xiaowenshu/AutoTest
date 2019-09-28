#!/usr/bin/python
# encoding:utf-8

from common.mysql_connect import mysql_connect
from common.util import m_dict


class testresource():
    __instance = None

    def __init__(self):
        self.testsource = dict()
        self.testsuit_setup = []
        self.testsuit_teardown = []
        self.testcase_setup = []
        self.testcase_teardown = []
        self.testcase_steps = []
        self.userkey_steps = []
        self.basickey = m_dict(dict())
        self.userkey = m_dict(dict())

    def get_testsuit_setup(self, testsuit_name):
        sql = "select keyword_name,keyword_parameters,step_name,project from autotestsuit_step where name='" + testsuit_name + "'and type='SETUP' and status='1' order by step_no"
        self.testsuit_setup = mysql_connect().execute_sql(sql)
        return self.testsuit_setup

    def get_testsuit_teardown(self, testsuit_name):
        sql = "select keyword_name,keyword_parameters,step_name,project from autotestsuit_step where name='" + testsuit_name + "'and type='TEARDOWN' and status='1' order by step_no"
        self.testsuit_teardown = mysql_connect().execute_sql(sql)
        return self.testsuit_teardown

    def get_testcase_setup(self, testcase_id):
        sql = "select keyword_name,keyword_parameters,step_name,project  from autotestcase_step where testcase_id=' " + testcase_id + "' and type='SETUP' and status='1' order by step_no"
        self.testcase_setup = mysql_connect().execute_sql(sql)
        return self.testcase_setup

    #
    def get_testcase_teardown(self, testcase_id):
        sql = "select keyword_name,keyword_parameters,step_name,project  from autotestcase_step where testcase_id=' " + testcase_id + "' and type='TEARDOWN' and status='1' order by step_no"
        self.testcase_teardown = mysql_connect().execute_sql(sql)
        return self.testcase_teardown

    def get_testcase_steps(self, testcase_id):
        sql = "select keyword_name,keyword_parameters,step_name,project  from autotestcase_step where testcase_id=' " + testcase_id + "' and type='NORMAL' and status='1' order by step_no"
        self.testcase_steps = mysql_connect().execute_sql(sql)
        return self.testcase_steps

    def get_userkey_steps(self, project, userkeyname):
        #         if stage=='testsuit':
        #         sql="SELECT keyword_name,step_name,keyword_parameters,project FROM userkey_steps  where project ='"+project+"' and status='1' and name ='"+userkeyname+"'"
        sql = "SELECT keyword_name,keyword_parameters,step_name,project FROM userkey_steps  where project ='" + project + "' and status='1' and name ='" + userkeyname + "'"
        #         elif stage=='testcase':
        #             sql="SELECT keyword_name,keyword_parameters,step_name FROM userkey_steps  where project =' "+project+"' and status='1'"
        self.userkey_steps = mysql_connect().execute_sql(sql)
        #         print(self.userkey_steps)
        return self.userkey_steps

    def get_basickey(self):
        sql = "select name,func_name,func_parameters from keywords where project='ALL' and type='basic'"
        for key, funcname in mysql_connect().execute_sql(sql):
            print(key, funcname)
            self.basickey.m_set_item(key, funcname)
        return self.basickey

    def get_userkey(self, project):
        sql = "select name,func_name,func_parameters from keywords where project='" + project + "' and type='user'"
        for key, funcname in mysql_connect().execute_sql(sql):
            print(key, funcname)
            self.userkey.m_set_item(key, funcname)
        return self.userkey

    def get_testcase_id(self, testsuit_name, project):
        case_id = []
        sql = "SELECT testcase_id FROM autotestsuit where name='" + testsuit_name + "' and project='" + project + "'"

        for id in mysql_connect().execute_sql(sql):
            case_id.append(id[0])
        #         print case_id
        return case_id


if __name__ == '__main__':
    #     ts1=testresource()
    #     ts1.get_testsuit_setup('testdebug', ['func_name','func_parameters'])
    #     ts1.get_testsuit_teardown('testdebug', ['func_name','func_parameters'])
    #     ts1.get_testcase_setup('1', ['keyword_name','keyword_parameters'])
    #     ts1.get_testcase_steps('1', ['keyword_name','keyword_parameters'])
    #     ts1.get_testcase_teardown('1', ['keyword_name','keyword_parameters'])
    #     ts1.get_basickey()
    #     ts1.get_userkey('FLEET')
    #     ts1.get_userkey_steps('FLEET', 'adfda')
    pass
