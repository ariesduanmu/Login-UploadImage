# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 11:21:54
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 11:24:57
import os 

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBFILE = 'data-dev.sqlite'
TYPE = 'sqlite:///'

db_file_path = os.path.join(BASEDIR, DBFILE)

db_url = TYPE+db_file_path