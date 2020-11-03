from __futre__ import with_statement
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask, request, session, url_for, redirect, \
    render_template, abort, g, flash
from werkzeug.security import check_passworrd_hash, generate_password_hash

#configuration
DATABASE = 'minitwit.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS' , silent=True)

def connect_db():
    """Returns a new connection to the database."""
    return sqlite3.connect(app.config['DATABASE'])


