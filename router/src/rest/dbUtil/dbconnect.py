#!/usr/bin/env python3.4
#Author: Laura Chavez
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

'''
this is the line that is changed
'''
dbConfig=LOCAL

# Inserting data to Users Table
# PARAM1: username value
# PARAM2: bio value
# PARAM3: passwd (NOT HASHED IN FUNCTION)
# Returns new user's id
def insert_data_users(username,bio,passwd,email):
    if( len(get_field("idusers", "users", "username", username)) > 0): return -1
    query = "INSERT INTO users(idusers,username,bio,pass,email) " \
        "VALUES(NULL,%s,%s,%s,%s)"
    args = (username, bio, passwd, email)
    error = __change_data(query,args)
    userid = get_field("idusers","users","username",username)
    return userid[0]['idusers']

# Inserting data to Routes Table
# PARAM1: route value
# PARAM2: route start point latitude
# PARAM3: route start point longitude
# PARAM4: userid value, user that the route belongs to
def insert_data_routes(route,startPointLat,startPointLon,userid,routeName):
    if( len(get_field("idroutes", "routes", "route", route)) > 0): return -1

    query = "INSERT INTO routes(route,startPointLat,startPointLon,userid,routeName) " \
        "VALUES(%s,%s,%s,%s,%s)"
    args = (route, startPointLat, startPointLon, userid, routeName)
    __change_data(query,args)

    return get_field("idroutes", "routes", "route", route)


# OPTING OUT COMMENTS TABLE FOR NOW..

# Update a single field in specified table
# PARAM1: Name of the table that will be updated
# PARAM2: Name of field that's value will be changed
# PARAM3: New value for field specified in (PARAM2)
# PARAM4 & PARAM5: Condition for where statement (field, value) respectively
def update_data(tablename, setfield, newvalue, wherefield, cond):
    query = "UPDATE %s SET %s = %s WHERE %s = %s" % (tablename, setfield, '%s', wherefield, '%s')
    args = (newvalue,cond)
    __change_data(query,args)

# Deletes row from specified table
# PARAM1: Name of table where row is deleted from
# PARAM2 & PARAM3: Condition for where statement (field, value) respectively
def delete_data(tablename, wherefield, condition):
    query = "DELETE FROM %s WHERE %s = %s" % (tablename, wherefield, '%s')
    args = (condition,)
    __change_data(query,args)

# Connects to database and processes the query
'''
I was able to get rid of that horrendoous try/except messs
that we had before. Now it should only try ONE time
'''
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
################ TESTING ##################
# USED FOR TESTING
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
    
def testInsert():
    insert_data_users("user123", "bioInfo","pw098")
    assert (get_field("idusers", "users","username","user123") > 0 ),"Insert Users error"
    delete_data("users","username","user123") # Deleting for in case test is ran again
    
    insert_data_routes("rtemp","1")
    assert (get_field("idroutes","routes","route","rtemp") > 0),"Insert Routes error"
    insert_data_routes("rtemp2","1")
    assert (get_field("idroutes","routes","route","rtemp2") > 0),"Insert Routes error"
    delete_data("routes","route","rtemp")
    delete_data("routes","route","rtemp2")

def testUpdate():
    insert_data_users("user123", "bioInfo","pw098")
    update_data("users", "username", "user4", "username", "user123")
    assert(get_field("username","users","username", "user4") > 0), "Update Users Error"
    delete_data("users","username","user4")

if __name__ == '__main__':
    testInsert()
    testUpdate()
