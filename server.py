#!/usr/bin/env python
#https://gist.github.com/bradmontgomery/2219997
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urllib2

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        url="http://"+dict(self.headers)["host"]+self.path
        print url
        try:
            print "cookie:\n"+dict(self.headers)["cookie"]
        except:
            print "NO cookie!"

        req = urllib2.Request(url,None,dict(self.headers))
        # req.add_header(dict(self.headers))
        # resp = urllib2.urlopen(req)
        # content = resp.read()
        self._set_headers()
        self.wfile.write("<img src='https://cdn.pixabay.com/photo/2017/01/01/14/37/hacker-1944673_960_720.png'/>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()