#!/usr/bin/python
# encoding:utf-8

# import datetime
import os
import logging
import datetime


class logging_config():
    def __init__(self):
        self.level = logging.DEBUG
        self.format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        self.datefmt = '%a, %d %b %Y %H:%M:%S'
        self.filemode = 'w'

    #         self.path=os.path.dirname(__file__)+"\log"
    #         print(self.path)
    def set_logging_config(self, **kwagrs):

        if kwagrs.get('level') != None:
            self.level = kwagrs.get('level')

        if kwagrs.get('filename') != None:
            self.filename = kwagrs.get('filename')

        if kwagrs.get('filemode') != None:
            self.filemode = kwagrs.get('filemode')

        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            #                     filename='C:\Users\XIAOWENSHU297\workspace\data_execute\src\log\'+self.filename+'.log',
                            filename=os.path.abspath('..') + '\logs' + '\\' + self.filename + '_' + str(
                                os.getpid()) + '_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log',
                            filemode=self.filemode
                            )









