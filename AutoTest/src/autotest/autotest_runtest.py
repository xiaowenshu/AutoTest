#!/usr/bin/python
# encoding:utf-8

import logging
import os
from common.util import util
from common.logging_config import logging_config
from autotest.testprocess import testprocess
from autotest.testresource import testresource


class autotest_runtest():
    def __init__(self):
        logging_config().set_logging_config(filename='autotest_runtest')
        self.para = None

    #         self.cp=ConfigParser.ConfigParser().read('autotest_runtest.cfg')
    #         self.autotestcase_id=self.cp.get('RUN_PARA','AUTOTESTCASEID')
    #         self.autotestcase_version=self.cp.get('RUN_PARA','VERSION')
    #         self.project_id=self.cp.get('RUN_PARA','PROJECTNAME')

    def handle_parameters(self):
        parametersdict = dict()
        for run_para in util().cfg_to_dict(os.path.abspath('.') + '\\' + 'autotest_runtest.cfg')['RUN_PARA']:
            parametersdict[run_para[0]] = run_para[1]
        print(parametersdict)
        return parametersdict

    def run_autotest(self):
        try:
            self.para = self.handle_parameters()
            testsuit_name = self.para['testsuit_name']
            testcase_id = self.para['testcase_id']
            project = self.para['project']
            if testsuit_name != '':
                print("\n\n\n\n------------------TESTSUIT %s START--------------" % testsuit_name)
                ts = testresource()
                tp = testprocess()
                testprocess.handle_testsuit_setup(tp, testsuit_name)
                testprocess.handle_testsuit_teardown(tp, testsuit_name)
                if testcase_id == '':
                    testcase_id = ts.get_testcase_id(testsuit_name, project)
                    for i in range(0, len(testcase_id)):
                        try:
                            print("\n\n\n\n------------------TESTCASE %s START--------------" % testcase_id[i])
                            testprocess.handle_testcase_setup(tp, testcase_id[i])
                            testprocess.handle_testcase_steps(tp, testcase_id[i])
                            testprocess.handle_testcase_teardown(tp, testcase_id[i])
                            print("\n\n\n\n------------------TESTCASE %s OVER--------------" % testcase_id[i])
                        except Exception as e:
                            print("\n\n\n\n------------------TESTCASE %s EXCEPTION--------------" % testcase_id[i])
                elif testcase_id != '':
                    testcase_id = testcase_id.split(',')
                    for i in range(0, len(testcase_id)):

                        try:
                            print("\n\n\n\n------------------TESTCASE %s START--------------" % testcase_id[i])
                            testprocess.handle_testcase_setup(tp, testcase_id[i])
                            testprocess.handle_testcase_steps(tp, testcase_id[i])
                            testprocess.handle_testcase_teardown(tp, testcase_id[i])
                            print("\n\n\n\n------------------TESTCASE %s OVER--------------" % testcase_id[i])
                        except Exception as e:
                            print("\n\n\n\n------------------TESTCASE %s EXCEPTION--------------" % testcase_id[i])
            else:
                print("testsuit_name is null,Please set testsuit_name")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    at1 = autotest_runtest()
    at1.run_autotest()