#!/usr/bin/python
# encoding:utf-8


import os
import time
import json
import random
from autotest.keys.keyinterface import keyinterface
import logging


class commonlogic(keyinterface):

    def Cmd(self, args):
        os.system(args[0])

    def Getsystemtime(self, name, args):
        system_time = None
        if args[0] == None:
            system_time = time.strftime('%Y-%m-$d', time.localtime())
        else:
            system_time = time.strftime(args[0], time.localtime())
        return system_time

    def GernerateRNO(self, name, args):
        return random.randint(args[0], args[1])

    def xprint(self, name, args):
        #         print(args[0])
        return args[0]

    def check_rs(self, name, args):
        """args[0] is exp-rs,args[1] is rel-rs,args[2] is对比方式支持JSON """
        if args[1] != None and args[0] != None:
            if args[2] != None and args[2] == 'json':
                exp_rs = json.loads(args[0])
                rel_rs = json.loads(args[1])
                if exp_rs == rel_rs:
                    rs = True
                    rs_str = 'pass'
                else:
                    rs = False
                    rs_str = 'fail'
        else:
            print("exp-rs or rel-rs is none")
            logging.info("exp-rs or rel-rs is none")
        print("%s step check result is  %s , exp-rs is %s and rel-rs is %s" % (name, rs_str, exp_rs, rel_rs))
