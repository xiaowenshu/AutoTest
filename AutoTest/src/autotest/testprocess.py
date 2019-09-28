#!/usr/bin/python
# encoding:utf-8

import logging

from common.logging_config import logging_config
from common.util import m_dict
from testresource import testresource


class testprocess():

    def __init__(self):
        #         self.l_testprocess=m_dict(dict())
        #         self.tp=testprocess()
        self.ts = testresource()
        self.curtestsuitstep_rs = m_dict(dict())
        self.testsuitpara = m_dict(dict())

        self.curtestcasestep_rs = m_dict(dict())
        self.testcasepara = m_dict(dict())
        self.curuserkeystep_rs = m_dict(dict())

    #         logging_config().set_logging_config(filename='testprocess')
    @staticmethod
    def handle_keywords(keyword, function, args):
        key_class = __import__('autotest.keys.' + keyword, fromlist=[str(keyword)])
        #         from autotest.keys.seleniumkey import seleniumkey

        func = getattr(getattr(getattr(key_class, keyword), 'get_instance')(), str(function))
        #         t=getattr(dd,'OpenURL')
        #         print(t)
        #         print(dir(t))
        #         t()
        return func(args)

    def handle_testsuit_setup(self, testsuit_name):
        rs = self.ts.get_testsuit_setup(testsuit_name)
        for i in range(0, len(rs)):
            if rs[i] != '' and rs[i] != None and rs[i] != 'null':

                if rs[i][0].split('.')[0] == 'basickey':
                    n_para = self.update_para(rs[i][1], 'SUIT')

                    self.curtestsuitstep_rs.m_set_item(rs[i][2], self.handle_keywords(rs[i][0].split('.')[1],
                                                                                      rs[i][0].split('.')[2], n_para))
                    print
                    "'%s' this suit setup step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this suit setup para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2])))
                elif rs[i][0].split('.')[0] == 'userkey':
                    n_para = self.update_para(rs[i][1], 'SUIT')
                    #                     print n_para
                    self.curtestsuitstep_rs.m_set_item(rs[i][2], self.handle_userkey_step(rs[i][3], rs[i][0], n_para))
                    print
                    "'%s' this suit setup para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this suit setup  para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2])))

    #

    def handle_testsuit_teardown(self, testsuit_name):
        rs = self.ts.get_testsuit_teardown(testsuit_name)
        for i in range(0, len(rs)):
            if rs[i] != '' and rs[i] != None and rs[i] != 'null':

                if rs[i][0].split('.')[0] == 'basickey':
                    n_para = self.update_para(rs[i][1], 'SUIT')

                    self.curtestsuitstep_rs.m_set_item(rs[i][2], self.handle_keywords(rs[i][0].split('.')[1],
                                                                                      rs[i][0].split('.')[2], n_para))
                    print
                    "'%s' this suit teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this suit teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2])))
                elif rs[i][0].split('.')[0] == 'userkey':
                    n_para = self.update_para(rs[i][1], 'SUIT')
                    #                     print n_para
                    self.curtestsuitstep_rs.m_set_item(rs[i][2], self.handle_userkey_step(rs[i][3], rs[i][0], n_para))
                    print
                    "'%s' this suit teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this suit teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestsuitstep_rs.m_get_item(rs[i][2])))

    def handle_testcase_setup(self, testcase_id):
        rs = self.ts.get_testcase_setup(testcase_id)
        for i in range(0, len(rs)):
            if rs[i] != '' and rs[i] != None and rs[i] != 'null':
                if rs[i][0].split('.')[0] == 'basickey':
                    n_para = self.update_para(rs[i][1], 'CASE')

                    self.curtestcasestep_rs.m_set_item(rs[i][2], self.handle_keywords(rs[i][0].split('.')[1],
                                                                                      rs[i][0].split('.')[2], n_para))
                    print
                    "'%s' this testcase setup step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this testcase setup step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2])))
                elif rs[i][0].split('.')[0] == 'userkey':
                    n_para = self.update_para(rs[i][1], 'CASE')
                    #                     print n_para
                    self.curtestcasestep_rs.m_set_item(rs[i][2], self.handle_userkey_step(rs[i][3], rs[i][0], n_para))
                    print
                    "'%s' this testcase setup step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this testcase setup step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2])))

    def handle_testcase_teardown(self, testcase_id):
        rs = self.ts.get_testcase_setup(testcase_id)
        for i in range(0, len(rs)):
            if rs[i] != '' and rs[i] != None and rs[i] != 'null':
                if rs[i][0].split('.')[0] == 'basickey':
                    n_para = self.update_para(rs[i][1], 'CASE')

                    self.curtestcasestep_rs.m_set_item(rs[i][2], self.handle_keywords(rs[i][0].split('.')[1],
                                                                                      rs[i][0].split('.')[2], n_para))
                    print
                    "'%s' this testcase teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this suit teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2])))
                elif rs[i][0].split('.')[0] == 'userkey':
                    n_para = self.update_para(rs[i][1], 'CASE')
                    #                     print n_para
                    self.curtestcasestep_rs.m_set_item(rs[i][2], self.handle_userkey_step(rs[i][3], rs[i][0], n_para))
                    print
                    "'%s' this testcase teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' testcase  teardown step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2])))

    def handle_testcase_steps(self, testcase_id):
        rs = self.ts.get_testcase_setup(testcase_id)
        for i in range(0, len(rs)):
            if rs[i] != '' and rs[i] != None and rs[i] != 'null':
                if rs[i][0].split('.')[0] == 'basickey':
                    n_para = self.update_para(rs[i][1], 'CASE')

                    self.curtestcasestep_rs.m_set_item(rs[i][2], self.handle_keywords(rs[i][0].split('.')[1],
                                                                                      rs[i][0].split('.')[2], n_para))
                    print
                    "'%s' this testcase  step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' this testcase  step para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2])))
                elif rs[i][0].split('.')[0] == 'userkey':
                    n_para = self.update_para(rs[i][1], 'CASE')
                    #                     print n_para
                    self.curtestcasestep_rs.m_set_item(rs[i][2], self.handle_userkey_step(rs[i][3], rs[i][0], n_para))
                    print
                    "'%s' this testcase step  para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s' testcase  step  para is '%s' and this step result is '%s'" % (
                    rs[i][2], n_para, self.curtestcasestep_rs.m_get_item(rs[i][2])))

    def handle_userkey_step(self, project, userkeyname, args):

        rs = self.ts.get_userkey_steps(project, userkeyname)
        for i in range(0, len(rs)):
            if rs[i] != '' and rs[i] != None and rs[i] != 'null':
                if rs[i][0].split('.')[0] == 'userkey':

                    n_para = self.update_para(rs[i][1], 'USERKEY')
                    #                     rs=self.ts.get_userkey_steps(userkeyname,project)
                    self.curuserkeystep_rs.m_set_item(rs[i][2], self.handle_userkey_step(rs[i][3], rs[i][0], n_para))
                #                     logging.info('this suit_step para is '+args+' and this step result is '+str(self.curuserkeystep_rs.m_get_item(rs[i][2])))
                elif rs[i][0].split('.')[0] == 'basickey':
                    n_para = self.update_para(rs[i][1], 'USERKEY')
                    self.curuserkeystep_rs.m_set_item(rs[i][2], self.handle_keywords(rs[i][0].split('.')[1],
                                                                                     rs[i][0].split('.')[2], n_para))
                    #                     return self.handle_keywords(rs[i][0].split('.')[1], rs[i][0].split('.')[2], args)
                    print
                    "'%s'this userkey_step  para is '%s' and this userkey step result is '%s'" % (
                    rs[i][2], n_para, self.curuserkeystep_rs.m_get_item(rs[i][2]))
                    logging.info("'%s'this userkey_step  para is '%s' and this userkey step result is '%s'" % (
                    rs[i][2], n_para, self.curuserkeystep_rs.m_get_item(rs[i][2])))

        return self.curuserkeystep_rs.m_get_item(rs[i][2])

    def update_para(self, args, level):
        n_arg = []
        if level == 'SUIT':
            for arg in args.split(','):
                #                 print arg
                if arg.split(':')[1][0] == '$':
                    if self.curtestsuitstep_rs.m_has_key(arg.split(':')[1][2:-1]):
                        self.testsuitpara.m_set_item(arg.split(':')[0],
                                                     self.curtestsuitstep_rs.m_get_item(arg.split(':')[1][2:-1]))
                        n_arg.append(self.curtestsuitstep_rs.m_get_item(arg.split(':')[1][2:-1]))
                else:
                    self.testsuitpara.m_set_item(arg.split(':')[0], arg.split(':')[1])
                    n_arg.append(arg.split(':')[1])
        #                     logging.info('after update suit para is '+str(n_arg))

        elif level == 'CASE':
            for arg in args.split(','):
                #                 print arg
                if arg.split(':')[1][0] == '$':
                    if self.curtestcasestep_rs.m_has_key(arg.split(':')[1][2:-1]):
                        self.testcasepara.m_set_item(arg.split(':')[0],
                                                     self.curtestsuitstep_rs.m_get_item(arg.split(':')[1][2:-1]))
                        n_arg.append(self.curtestcasestep_rs.m_get_item(arg.split(':')[1][2:-1]))
                else:
                    self.testcasepara.m_set_item(arg.split(':')[0], arg.split(':')[1])
                    n_arg.append(arg.split(':')[1])
        #                 logging.info('after update case para is '+str(n_arg))

        elif level == 'USERKEY':
            for arg in args.split(','):
                #                 print arg
                if arg.split(':')[1][0] == '$':
                    if self.testsuitpara.m_has_key(arg.split(':')[1][2:-1]):
                        n_arg.append(self.testsuitpara.m_get_item(arg.split(':')[1][2:-1]))

                    elif self.testcasepara.m_has_key(arg.split(':')[1][2:-1]):
                        n_arg.append(self.testcasepara.m_get_item(arg.split(':')[1][2:-1]))

                    elif self.curuserkeystep_rs.m_has_key(arg.split(':')[1][2:-1]):
                        n_arg.append(self.curuserkeystep_rs.m_get_item(arg.split(':')[1][2:-1]))

                    elif self.curtestcasestep_rs.m_has_key(arg.split(':')[1][2:-1]):
                        n_arg.append(self.curtestcasestep_rs.m_get_item(arg.split(':')[1][2:-1]))

                else:
                    self.testsuitpara.m_set_item(arg.split(':')[0], arg.split(':')[1])
                    n_arg.append(arg.split(':')[1])
        #                     logging.info('after update userkey para is '+str(n_arg))
        #         print(n_arg)
        return n_arg

    def clear_testsuitpara(self):
        self.testsuitpara.clear()

    def clear_testcasepara(self):
        self.testcasepara.clear()

    def clear_testcasesuitstep_rs(self):
        self.curtestsuitstep_rs.clear()

    def clear_testcasetep_rs(self):
        self.curtestcasestep_rs.clear()

    def clear_userkeystep_rs(self):
        self.curuserkeystep_rs.clear()

# if __name__=='__main__':
#     t1=testprocess()
# #     t1.handle_keywords(keyword='seleniumkey',function='OpenURL',args=['sdfafdsfsdf','dfdfdfd'],type=None)
#     t1.handle_testsuit_setup('testdebug')
#     t1.handle_testsuitl_teardown('testdebug')
#     t1.clear_testsuitpara()
#     t1.handle_testcase_setup('1')