#!/usr/bin/env python3.5
#Author: Laura Chavez
#Module used to connect to database
#Note: Should load db beforehand.

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

# Inserting data to Users Table
# PARAM1: username value
# PARAM2: bio value
# PARAM3: passwd (NOT HASHED IN FUNCTION)
def insert_data_users(username,bio,passwd):
    query = "INSERT INTO users(idusers,username,bio,pass) " \
        "VALUES(NULL,%s,%s,%s)"
    args = (username, bio, passwd)
    __change_data(query,args)
    userid = get_field("idusers","users","username",username)
    return userid

# Inserting data to Routes Table
# PARAM1: route value
# PARAM2: route start point latitude
# PARAM3: route start point longitude
# PARAM4: userid value, user that the route belongs to
def insert_data_routes(route,startPointLat,startPointLon,userid):
    query = "INSERT INTO routes(idroutes,route,startPointLat,startPointLon,userid) " \
        "VALUES(NULL,%s,%s,%s,%s)"
    args = (route, startPointLat, startPointLon, userid)
    __change_data(query,args)


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
def __change_data(query,args):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        
        cursor = conn.cursor()
        cursor.execute(query, args)
        try:
            conn.commit()
        except:
            pass
        return cursor.fetchall()

    except Error as error:
        print(error)
        try:
            db_config = read_db_config('./src/rest/dbUtil/config_test.ini')
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            return cursor.fetchall()
        except Error as error:
            print(error)
    
    finally:
        cursor.close()
        conn.close()

################ TESTING ##################
# USED FOR TESTING
def get_field(fieldname, tablename,fieldnamecondition,fieldvaluecondition):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        
        query = "SELECT %s FROM %s WHERE %s = %s" % (fieldname,tablename,fieldnamecondition, '%s')
        args = (fieldvaluecondition,)
        cursor.execute(query,args)
        
        row = cursor.fetchone()
        return row[0]
    
    except Error as error:
        print(error)
    
    finally:
        conn.close()

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
