#!/usr/bin/python
# _*_ coding:utf-8 _*_
import threading

import re
from selenium import webdriver
import unittest

from app import create_app, db
from app.models import Role, User, Post


class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        # start firefox
        try:
            cls.client = webdriver.Firefox()
        except:
            pass
        # if can not enable the browser skip the test
        if cls.client:
            # create app
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # forbidden log, keep print clean
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel('ERROR')

            # create db
            db.create_all()
            Role.insert_roles()
            User.generate_fake(10)
            Post.generate_fake(10)

            # add administrator
            admin_role = Role.query.filter_by(permission=0xff).first()
            admin = User(email='john@qq.com',
                         username='john', password='cat',
                         role=admin_role, confirmed=True)
            db.session.add(admin)
            db.session.commit()

            # enable the flask server in a thread
            threading.Thread(target=cls.app.run).start()

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # close flask server and browser
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.close()

            # destroy db
            db.drop_all()
            db.session.remove()

            # pop app context
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not available')

    def tearDown(self):
        pass

    def test_admin_home_page(self):
        # insert the home
        self.client.get('http://localhost:5000/')
        self.assertTrue(re.search('Hello,\s+Stranger',
                                  self.client.page_source))
        # insert the login page
        self.client.find_element_by_link_text('Log In').click()
        self.assertTrue('<h1>Login</h1>' in self.client.page_source)

        # login
        self.client.find_element_by_name('email'). \
            send_keys('john@qq.com')
        self.client.find_element_by_name('password').send_keys('cat')
        self.client.find_element_by_name('submit').click()
        self.assertTrue(re.search('Hello,\s+john', self.client.page_source))

        # insert personal profile page
        self.client.find_element_by_link_text('Profile').click()
        self.assertTrue('<h1>john</h1>' in self.client.page_source)
