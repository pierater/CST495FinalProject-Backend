#!/usr/bin/env python3.4
#Author: Martin Almaraz
#Module used to connect to database
#Note: Should load db beforehand.

from mysql.connector import MySQLConnection, Error, errorcode
from python_mysql_dbconfig import read_db_config

'''
Added these so that our SED functinos AWS, LOCAL, and CIRCLE can
change our db to whatever is needed
'''
AWS = './src/rest/dbUtil/configAWS.ini'
CIRCLE = './src/rest/dbUtil/config_test.ini'
LOCAL = './src/rest/dbUtil/config.ini'

dbConfig=LOCAL

# Inserting data to Users Table
def insert_data_users(username, password):
    if( len(get_field("idusers", "users", "username", username)) > 0): return -1
    query = "INSERT INTO users(idusers,username,pass) " \
        "VALUES(NULL,%s,%s)"
    args = (username, password)
    __change_data(query,args)
    userid = get_field("idusers","users","username",username)
    return userid[0]['idusers']


# Update a single field in specified table
def update_data(tableName, fieldName, newValue, fieldNameForCondition, valueForCondition):
    query = "UPDATE %s SET %s = %s WHERE %s = %s" % (tableName, fieldName, '%s', fieldNameForCondition, '%s')
    args = (newValue, valueForCondition)
    __change_data(query,args)

# Deletes row from specified table
def delete_data(tableName, fieldNameForCondition, valueForCondition):
    query = "DELETE FROM %s WHERE %s = %s" % (tableName, fieldNameForCondition, '%s')
    args = (valueForCondition,)
    __change_data(query,args)

# Connects to database and processes the query
def __change_data(query,args):
    try:
        db_config = read_db_config(dbConfig)
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor(buffered=True, dictionary=True)
        cursor.execute(query, args)
        try:
            conn.commit()
            return cursor.fetchall()
        except Error as error:
            if error.errno == errorcode.ER_DUP_ENTRY:
                return None
            print(error)
    except Error as error:
        print(error)

def get_field(fieldname, tablename,fieldnamecondition,fieldvaluecondition):
    try:
        db_config = read_db_config(dbConfig)
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT %s FROM %s WHERE %s = %s" % (fieldname,tablename,fieldnamecondition, '%s')
        args = (fieldvaluecondition,)
        cursor.execute(query,args)
        row = cursor.fetchall()
        return row
    except Error as error:
        print(error)
