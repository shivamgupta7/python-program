import os
import mysql.connector
from mysql.connector import Error
import logging
from LoggerManager import NewLogger
import os
import json
import csv


class DatabaseManager:
    
    def __init__(self, host_name, username, password, db, logger_file_name=''):
        self.conn = mysql.connector.connect(host=host_name, user=username, passwd=password, database=db, allow_local_infile=True)
        self.database = db
        self.logger_file_name = logger_file_name
        self.database_logger = NewLogger('DatabaseManager', self.logger_file_name)
        self.cursor = self.conn.cursor()

    def select_data(self, sql_string):
        logging.info('Select data run on ' + self.database + ' database')
        table_data = self.cursor.execute(sql_string)
        table_data = self.cursor.fetchall()
        return print(table_data)

    def create_table(self,sql_string):
        try:
            logging.info('Create new table in ' + self.database + ' database')
            self.cursor.execute(sql_string)
            self.conn.commit()
            print('Table created successfully.')
        except mysql.connector.Error as ex:
            logging.error('create table on: ' + self.database + ' for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")

    def insert_sql_data(self,sql_string):
        try:
            logging.info('Insert sql data run on: ' + self.database + ' database')
            self.cursor.execute(sql_string)
            self.conn.commit()
            print('New row added successfully.')
        except mysql.connector.Error as ex:
            logging.error('Insert sql data run on: ' + self.database + ' for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")
    
    def modify_sql_data(self,SqlString):
        try:
            logging.info('Modify sql data run on ' + self.database + ' database')
            self.cursor.execute(SqlString)
            self.conn.commit()
            print('Modify data successfully.')
        except mysql.connector.Error as ex:
            logging.error('Modify sql data run on ' + self.database + ' for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")

    def delete_sql_data(self,SqlString):
        try:
            logging.info('Delete sql data run on ' + self.database + ' database')
            self.cursor.execute(SqlString)
            self.conn.commit()
            print('Delete data successfully.')
        except mysql.connector.Error as ex:
            logging.error('Delete sql data run on ' + self.database + ' for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")

    def export_data(self,SqlString,file_type,table_name):
        try:
            if file_type.casefold() == 'json':
                logging.info('Export table ' + table_name + ' to ' + file_type +' file.')
                self.cursor.execute(SqlString)
                row_headers = [column[0] for column in self.cursor.description]
                data=self.cursor.fetchall()
                json_data = { table_name : []}
                out_file = open("employees.json", "w")
                for result in data:
                    json_data[table_name].append(dict(zip(row_headers,result)))
                json.dump(json_data, out_file,indent=4, default=str)
                out_file.close()
                print('Table convert into json file successfully.')
            elif file_type.casefold() == 'csv':
                logging.info('Export database ' + self.database + ' to ' + file_type +' file.')
                self.cursor.execute(SqlString)
                data = self.cursor.fetchall()
                column_names = [column[0] for column in self.cursor.description]
                out_file = open('employee.csv', 'w')
                myFile = csv.writer(out_file)
                myFile.writerow(column_names)
                myFile.writerows(data)
                out_file.close()
                print('Table convert into CSV file successfully.')
        except mysql.connector.Error as ex:
            logging.error('Export sql data run on ' + self.database + ' for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")

    def import_data(self,SqlString):
        try:
            logging.info('Import data on ' + self.database + ' database')
            self.cursor.execute(SqlString)
            self.conn.commit()
            print('Import data successfully.')
        except mysql.connector.Error as ex:
            logging.error('Import data run on ' + self.database + ' for query: '+str(ex))
        finally:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()
                print("MySQL connection is closed")