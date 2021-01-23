#!/usr/bin/env python
# encoding: utf-8
"""
# @Software: PyCharm
# @Author : wsf
# @Email：785707939@qq.com
# @Time：2020/01/23 08:52
# @File : mysql_tool.py
"""
import logging
import warnings
import pymysql

warnings.simplefilter("ignore")

__author__ = 'wangshifeng'
__version__ = '1.0.6'


class my_mysql():
    driver = pymysql
    """The my_mysql is a tool for mysql connect."""

    def __init__(self, host, user, database, password, port=3306, default_character_set="utf-8"):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.port = port
        self.default_character_set = default_character_set

    def _connect(self):
        try:
            return self.driver.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
                                       db=self.database, charset='utf8')
        except AttributeError:
            logging.error("No connect method found in self.driver module")

    def my_fetchall(self, sql, args=None, return_type=None):
        rows = []
        try:
            con = self._connect()
            if return_type == "dict":
                cur = con.cursor(self.driver.cursors.DictCursor)
            else:
                cur = con.cursor()
            try:
                if ";" not in sql:
                    logging.warning('mysql_toool.my_fetchall: sql not end with \";\";')
                cur.execute(sql, args)
                rows = cur.fetchall()
                rows = [r for r in rows]
            except self.driver.Error as error:
                logging.error('mysql_toool.my_fetchall: sql:' + str(error))
            finally:
                con.close()
        except self.driver.Error as error:
            logging.error('mysql_toool.my_fetchall: default.cnf error:' + str(error))
        if str(rows) == "[(None,)]":
            rows = []
        return rows

    def my_fetchone(self, sql, args=None, return_type=None):
        row = []
        try:
            con = self._connect()
            if return_type == "dict":
                cur = con.cursor(self.driver.cursors.DictCursor)
            else:
                cur = con.cursor()
            try:
                if ";" not in sql:
                    logging.warning('mysql_toool.my_fetchone: sql not end with \";\";')
                cur.execute(sql, args)
                row = cur.fetchone()
            except self.driver.Error as error:
                logging.error('mysql_toool.my_fetchone: sql:' + str(error))
            finally:
                con.close()
        except self.driver.Error as error:
            logging.error('mysql_toool.my_fetchone: default.cnf error:' + str(error))
        if row is None:
            row = []
        if str(row) == "(None,)":
            row = []
        return row

    def my_fetchone_new(self, sql_list, args=None, return_type=None):
        row_list = []
        try:
            con = self._connect()
            if return_type == "dict":
                cur = con.cursor(self.driver.cursors.DictCursor)
            else:
                cur = con.cursor()
            try:
                for sql in sql_list:
                    if ";" not in sql:
                        logging.warning('mysql_toool.my_fetchone: sql not end with \";\";')
                    cur.execute(sql, args)
                    row = cur.fetchone()
                    row_list.append(row)
            except self.driver.Error as error:
                logging.error('mysql_toool.my_fetchone: sql:' + str(error))
            finally:
                con.close()
        except self.driver.Error as error:
            logging.error('mysql_toool.my_fetchone: default.cnf error:' + str(error))
        return row_list

    def execute(self, sql, args=None):
        """

        :param sql: type must be str.
            if update success, return count of update rows.
            if delete success, return count of delete rows.
            if insert success, return 1.
            else return 0.

        :return:
        """
        handled_item = 0
        try:
            con = self._connect()
            cur = con.cursor()
            try:
                if ";" not in sql:
                    logging.warning('mysql_toool.execute: sql not end with \";\";')
                handled_item = cur.execute(sql, args)
            except self.driver.Error as error:
                raise error
                logging.error('mysql_toool.execute: sql:' + str(error))
            finally:
                con.commit()
                con.close()
        except self.driver.Error as error:
            print(sql)
            raise error
            logging.error('mysql_toool.execute: default.cnf error:' + str(error))
        return handled_item

    def insert(self, sql, args=None):
        """
        insert action
        :return:
        """
        handled_item = 0
        try:
            con = self._connect()
            cur = con.cursor()
            try:
                cur.execute(sql, args)
                handled_item = cur.lastrowid
            except self.driver.Error as error:
                logging.error('mysql_toool.execute: sql:' + sql+str(error))
            finally:
                con.commit()
                con.close()
        except self.driver.Error as error:
            logging.error('mysql_toool.execute: default.cnf error:' + str(error))
        return handled_item

    def execute_transaction(self, array_sql_action):
        """

        :param array_sql_action:
            The format is a single SQL, or list ﹣ SQL
        All the list SQL executed successfully, return len (list_sql)
        :return:
        """
        handled_item = 0
        try:
            con = self._connect()
            cur = con.cursor()
            sql = ""
            try:
                con.autocommit(False)
                if type(array_sql_action) is list:
                    for item in array_sql_action:
                        sql = item
                        if ";" not in sql:
                            logging.warning('mysql_toool.execute_transaction: sql not end with \";\";')
                        handled_item = handled_item + cur.execute(sql)
                else:
                    handled_item = cur.execute(array_sql_action)
            except self.driver.Error as error:
                handled_item = -1
                con.rollback()
                logging.error('mysql_toool.execute_transaction: sql: %s : %s' % (sql, str(error)))
            finally:
                con.commit()
                con.close()
        except self.driver.Error as error:
            logging.error('mysql_toool.execute_transaction: default.cnf error:' + str(error))
        return handled_item
