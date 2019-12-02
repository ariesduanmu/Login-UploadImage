# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 10:37:41
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 10:42:43
from sql import db
from .user import User

class ImportData(db.Model):
    __tablename__ = 'import_data'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(collation="utf8_unicode_ci", length=64), comment="图片信息")
    image_path = db.Column(db.String(collation="utf8_unicode_ci", length=64), comment="图片路径")
    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete="CASCADE"), comment="上传的用户的id")

    def __init__(self, info, image_path, user_id):
        self.info = info
        self.image_path = image_path
        self.user_id = user_id

    def __repr__(self):
        return f'<ImportData: (info | {self.info})>'