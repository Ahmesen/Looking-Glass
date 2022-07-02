from flask import Flask, render_template, send_from_directory, redirect, request
import os
import random
import subprocess
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(os.environ.get('MAIN_PAGE'))

@app.route("/server/dls/<ip>/<op>")
def pingServerSide(ip,op):
    # userip = request.environ['REMOTE_ADDR']
    #nginx request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    dest = ip.lstrip('ip=')
    dest = dest.lower()
    cmd = "ping -c 4"
    root = ""
    if(op == "op=1"):
        cmd = "ping -c 4 -4"
    if(op == "op=2"):
        cmd = "ping -c 4 -6"
    if(op == "op=3"):
        cmd = "traceroute -I -4"
        root = "sudo"
    if(op == "op=4"):
        cmd = "traceroute -I -6"
        root = "sudo"
    if(op == "op=5"):
        cmd = "mtr -4 --report --report-wide"
    if(op == "op=6"):
        cmd = "mtr -6 --report --report-wide"
    chars_to_remove = "!\"#$%&'()*+,;/<= >?@[\\]^_`{|}~\t\n\r " # \t TAB, \r: RETURN, \n NEWLINE
    translation_table = {ord(c): None for c in chars_to_remove }
    destsan = dest.translate(translation_table)
    if(destsan != dest):
        return render_template("nice-try.html"),500
    # operation = ('ping -c 4'+' '+dest)
    operation = (root+' '+cmd+' '+' '+dest)
    result = subprocess.run(operation, shell=True, check=True, stdout=subprocess.PIPE)
    if result.returncode == 1:
        return "No response from Host."
    result = result.stdout.decode("utf-8")
    return render_template("serverside.html", result=result, dest=dest, cmd=cmd)

@app.route("/wait")
def waitpage():
    return render_template("wait.html")
