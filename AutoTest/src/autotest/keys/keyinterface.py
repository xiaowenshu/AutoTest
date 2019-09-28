#!/usr/bin/python
# encoding:utf-8

from autotest.testresource import testresource


class keyinterface():
    __instance = None

    @classmethod
    def get_instance(cls):
        if (cls.__instance == None):
            cls.__instance = cls()
        #             print(cls.__instance)
        return cls.__instance
