'''
Created on 26 Haz 2017

@author: erdem
'''

#!/usr/bin/python
# coding: utf-8
import sqlite3
from SQLiteConnection.config import SQLiteHost

class SqlClass:
    ''' 
    Sql Constructor
    db = The directory where the database is located
    '''
    def __init__(self):
        try:
            self.conn = sqlite3.connect(SQLiteHost)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("An error occurred:",e.args[0])
    
    ''' 
    Sql Select
    Returning all results
    '''
    def Get(self,query,bind=""):
        try:
            getAll = self.cursor.execute(query,bind)
            self.conn.commit()
            return getAll.fetchall()
        except sqlite3.Error as e:
            print("An error occurred:",e.args[0])
    
    ''' 
    Sql Select
    Returning first row
    '''
    def GetRow(self,query,bind=""):
        try:
            getRow = self.cursor.execute(query,bind)
            self.conn.commit()
            return getRow.fetchone()
        except sqlite3.Error as e:
            print("An error occurred:",e.args[0])
    
    ''' 
    Sql Select
    Returning first column of first row
    '''
    def GetOne(self,query,bind=""):
        try:
            getOne = self.cursor.execute(query,bind)
            self.conn.commit()
            return getOne.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occurred:",e.args[0])
    
    ''' 
    Sql Insert
    Returning last insert id
    '''
    def Insert(self,query,bind=""):
        try:
            insert = self.cursor.execute(query,bind)
            self.conn.commit()
            return insert.lastrowid
        except sqlite3.Error as e:
            print("An error occurred:",e.args[0])
    
    ''' 
    Sql Insert
    Returning number of affected rows
    Can't work with SELECT query
    '''        
    def Exec(self,query,bind=""):
        try:
            affectRow = self.cursor.execute(query,bind)
            self.conn.commit()
            return affectRow.rowcount
        except sqlite3.Error as e:
            print("An error occurred:",e.args[0])
                   
