import os
import mysql.connector
from mysql.connector import Error
import logging
from LoggerManager import NewLogger


class DatabaseManager:
    
    def __init__(self, host_name, username, password, db, logger_file_name=''):
        self.conn = mysql.connector.connect(host=host_name, user=username, passwd=password, database=db)
        self.database = db
        self.logger_file_name = logger_file_name
        self.database_logger = NewLogger('DatabaseManager', self.logger_file_name)
        self.cursor = self.conn.cursor()

    def select_data(self, sql_string):
        logging.info('get_sql_data run on ' + self.database)
        table_data = self.cursor.execute(sql_string)
        table_data = self.cursor.fetchall()
        return print(table_data)

    def create_table(self,sql_string):
        try:
            logging.info('Create new table in ' + self.database)
            self.cursor.execute(sql_string)
            self.conn.commit()
            print('Table created successfully.')
        except mysql.connector.Error as ex:
            logging.error('create table on: ' + self.database + 'for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")

    def insert_sql_data(self,sql_string):
        try:
            logging.info('Insert sql data run on: ' + self.database)
            self.cursor.execute(sql_string)
            self.conn.commit()
            print('New row added successfully.')
        except mysql.connector.Error as ex:
            logging.error('Insert sql data run on: ' + self.database + 'for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")