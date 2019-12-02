# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 12:44:58
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 12:52:41
from flask import jsonify


def response_success(content={'success':'success'}):
    response = jsonify(content)
    response.status_code = 200
    return response

def response_error(content={"error":"error"}, status_code=401):
    response = jsonify(content)
    response.status_code = status_code
    return response

def unauthorized():
    response = jsonify({'error': 'unauthorized', 'message': 'Invalid credentials'})
    response.status_code = 403
    return response


def forbidden():
    response = jsonify({'error': 'forbidden', 'message': 'Unconfirmed account'})
    response.status_code = 403
    return response

