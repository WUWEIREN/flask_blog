#!/usr/bin/python
# _*_ coding:utf-8 _*_

from flask import Blueprint

from app import db
from app.models import Permission

main = Blueprint('main', __name__)


# 把Permission类加入模板上下文可全局访问
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


from . import views, errors

