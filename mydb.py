# install mysql on mac
# https://dev.mysql.com/downloads/mysql/
# pip3 install mysql
# pip3 install mysql-connector
# pip3 install mysql-connector-pythpn

import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = 'Root#123#'
)

 # cusor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute( "CREATE DATABASE clayco")

print( "All Done with Database inititlization!! ")
