#!/usr/bin/python
# encoding:utf-8

import requests
from autotest.keys.keyinterface import keyinterface


class webrequestkey(keyinterface):
    def __init__(self):
        self.m_session = requests.Session()

    def GetSesstion(self, name, args):
        if self.m_session == None:
            self.m_session = requests.Session()
        return self.m_session

    def SetHeader(self, name, args):
        m_session = self.GetSesstion()
        m_headers = m_session.headers
        if args[0] != '' and args[0] != None:
            m_headers = args[0]
        m_session.headers.update(m_headers)

    def POST(self, name, args):
        m_session = self.GetSesstion()
        hearders = m_session.headers
        contentType = None
        files = None
        if args[2] == 'form':
            data_post = args[1]
        elif args[2] == 'json':
            data_post = args[1]
        elif args[2] == 'multipart':
            files = args[2]
        m_session.post(args[0],
                       data=data_post,
                       files=files)

    def GET(self, name, args):
        m_session = self.GetSesstion()
        hearders = m_session.headers
        contentType = None
        files = None
        if args[2] == 'form':
            data_post = args[1]
        elif args[2] == 'json':
            data_post = args[1]
        elif args[2] == 'multipart':
            files = args[2]
        m_session.get(args[0],
                      data=data_post,
                      files=files)

    def DELETE(self, name, args):
        m_session = self.GetSesstion()
        hearders = m_session.headers
        contentType = None
        files = None
        if args[2] == 'form':
            data_post = args[1]
        elif args[2] == 'json':
            data_post = args[1]
        elif args[2] == 'multipart':
            files = args[2]
        m_session.delete(args[0],
                         data=data_post,
                         files=files)

    def PUT(self, name, args):
        m_session = self.GetSesstion()
        hearders = m_session.headers
        contentType = None
        files = None
        if args[2] == 'form':
            data_post = args[1]
        elif args[2] == 'json':
            data_post = args[1]
        elif args[2] == 'multipart':
            files = args[2]
        m_session.put(args[0],
                      data=data_post,
                      files=files)


if __name__ == '__main__':
    web1 = webrequestkey()
    web1.POST(args)