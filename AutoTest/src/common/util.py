#!/usr/bin/python
# encoding:utf-8
import configparser
import os


class m_dict():
    def __init__(self, object_dict):
        for key in object_dict:
            self.__dict__[key] = object_dict[key]

    #         print(self.__dict__)
    def m_has_attr(self, attr):
        if attr in self.__dict__.keys():
            return True

    def m_has_key(self, key):
        #         print(self.__dict__.has_key(key))
        return self.__dict__.has_key(key)

    def m_len(self):
        #         print(len(self.__dict__))
        return len(self.__dict__)

    def m_get_item(self, key):
        if self.__dict__.has_key(key):
            #             print(self.__dict__[key])
            return self.__dict__[key]

    def m_set_item(self, key, value):
        self.__dict__[key] = value

    def m_get_items(self):
        #         print(self.__dict__.items())
        return self.__dict__.items()

    def m_search_item(self, item):
        for key, value in self.__dict__.iteritems():
            if key.find(item) == 0:
                print(value)
                return value
        return None

    def clear(self):
        self.__dict__.clear()


class util():
    def cfg_to_dict(self, args):
        to_dict = dict()
        cfg = configparser.ConfigParser()
        cfg.read(args)
        #         print(cfg.sections())
        for k in cfg.sections():
            #             print k
            #             print cfg.items(k)
            to_dict[k] = cfg.items(k)
        #         print( to_dict)
        return to_dict

# if __name__=='__main__':
#     u1=util()
#     print(os.path.dirname(__file__)+'\common_config.cfg')
#     u1.cfg_to_dict(os.path.dirname(__file__)+'\common_config.cfg')
#     m=m_dict({'1':'aaa','2':'bbb'})
#     m.m_has_key('1')
#     m.m_get_item('1')
#     m.m_has_key('3')
#     m.m_set_item('3', 'ccc')
#     m.m_has_key('3')
#     m.m_search_item('3')
#     m.m_get_items()