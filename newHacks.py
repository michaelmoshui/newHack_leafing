# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 07:36:44 2022

@author: micha
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()