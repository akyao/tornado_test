#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import tornado.ioloop
import tornado.web

class SimpleHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, mother fucker")


class HtmlHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html.html")


application = tornado.web.Application([
    (r"/", SimpleHandler),
    (r"/html", HtmlHandler)
    ],
    template_path=os.path.join(os.getcwd(),  "templates"),
    static_path=os.path.join(os.getcwd(),  "static"),
)

if __name__ == "__main__":
    application.listen(8888)
    print("Server is up ...")
    tornado.ioloop.IOLoop.instance().start()
