from cgi import parse_header, parse_multipart
import cgi
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os.path
import subprocess,os,atexit,sys
from shutil import copyfile
import glob
import json

class RequestHandler(SimpleHTTPRequestHandler):

os.chdir(str(gv_home_dir)+"/home")
server = HTTPServer(('', 8000), RequestHandler)
server.serve_forever()
#iterate array
