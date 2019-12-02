# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 17:16:40
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:37:52
from flask import g

from sql.user import User

from app.utils.response_utils import response_success
from app.utils.response_utils import unauthorized
from app.utils.response_utils import forbidden

from app.extensions import auth

from app.api import api

from config.paths import API_CHECK_AUTH
from config.paths import API_TOKEN

from ..parsers.authenticationparser import check_auth_parser


@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:
        return forbidden()

@auth.verify_password
def verify_password(username_or_token, password):
    '''使用账户/密码 token进行认证
    '''
    if username_or_token == '':
        return False
    if password == '':
        # 密码为空，默认接收的是token
        g.current_user = User.verify_auth_token(username_or_token)
        g.token_used = True
        return g.current_user is not None

    user = User.query.filter_by(username=username_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized()

@api.route(API_CHECK_AUTH, methods=['POST'])
def check_auth():
    args = check_auth_parser.parse_args()
    username = args.get('username')
    password = args.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None:
        return unauthorized()
    g.current_user = user
    g.token_used = False
    return response_success()

@api.route(API_TOKEN, methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized()
    return response_success({'token': g.current_user.generate_auth_token(
        expiration=3600), 'expiration': 3600})