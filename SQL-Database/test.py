from DatabaseManager import DatabaseManager

dbm = DatabaseManager(host_name='localhost',username='root',password='Gupta@007',db='employees',logger_file_name='employees.log')

dbm.insert_sql_data("""INSERT INTO employees (birth_date, first_name, last_name, gender) 
                        VALUES 
                        ('1997-04-30', 'Shivam', 'Gupta', 'M') """)