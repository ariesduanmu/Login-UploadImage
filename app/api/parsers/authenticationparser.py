# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 12:32:20
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 12:35:02
from flask_restful import reqparse

check_auth_parser = reqparse.RequestParser()
check_auth_parser.add_argument(
    'username',
    type=str,
    required=True,
    )
check_auth_parser.add_argument(
    'password', 
    type=str,
    required=True,
) 