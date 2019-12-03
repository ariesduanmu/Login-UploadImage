# -*- coding: utf-8 -*-
import os 

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBFILE = 'data-dev.sqlite'
TYPE = 'sqlite:///'

db_file_path = os.path.join(BASEDIR, DBFILE)

db_url = TYPE+db_file_path