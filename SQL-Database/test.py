from DatabaseManager import DatabaseManager

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    " `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    " `birth_date` date NOT NULL,"
    " `first_name` varchar(14) NOT NULL,"
    " `last_name` varchar(16) NOT NULL,"
    " `gender` enum('M','F') NOT NULL,"
    " `hire_date` date NOT NULL,"
    " PRIMARY KEY (`emp_no`)"
    ") ")
TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    " `dept_no` char(4) NOT NULL,"
    " `dept_name` varchar(40) NOT NULL,"
    " PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ")
TABLES['salaries'] = (
    "CREATE TABLE `salaries` ("
    " `emp_no` int(11) NOT NULL,"
    " `salary` int(11) NOT NULL,"
    " `from_date` date NOT NULL,"
    " `to_date` date NOT NULL,"
    " PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    " CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ")
TABLES['dept_emp'] = (
    "CREATE TABLE `dept_emp` ("
    " `emp_no` int(11) NOT NULL,"
    " `dept_no` char(4) NOT NULL,"
    " `from_date` date NOT NULL,"
    " `to_date` date NOT NULL,"
    " PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    " KEY `dept_no` (`dept_no`),"
    " CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    " CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    " REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ")
TABLES['dept_manager'] = (
    " CREATE TABLE `dept_manager` ("
    " `dept_no` char(4) NOT NULL,"
    " `emp_no` int(11) NOT NULL,"
    " `from_date` date NOT NULL,"
    " `to_date` date NOT NULL,"
    " PRIMARY KEY (`emp_no`,`dept_no`),"
    " KEY `emp_no` (`emp_no`),"
    " KEY `dept_no` (`dept_no`),"
    " CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    " CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    " REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ")
TABLES['titles'] = (
    "CREATE TABLE `titles` ("
    " `emp_no` int(11) NOT NULL,"
    " `title` varchar(50) NOT NULL,"
    " `from_date` date NOT NULL,"
    " `to_date` date DEFAULT NULL,"
    " PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    " CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
    " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ")
dbm = DatabaseManager(host_name='localhost',username='root',password='Gupta@007',db='employees',logger_file_name='test.log')

# dbm.create_table(TABLES['employees'])

# dbm.insert_sql_data("""INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date) 
#                         VALUES 
#                         ('1996-10-30', 'Rohit', 'Gupta', 'M', '2020-03-05'),
#                         ('1995-09-21', 'Gaurav', 'Gupta', 'M', '2018-05-10'),
#                         ('1997-01-30', 'Shraddha', 'Srivastava', 'F', '2020-04-15'),
#                         ('1997-05-31', 'Priya', 'Pandey', 'F', '2020-01-30'),
#                         ('1995-11-06', 'Himanshu', 'Singh', 'M', '2019-07-12'),
#                         ('1997-02-27', 'Divyendu', 'Yadav', 'M', '2019-02-20'),
#                         ('1996-12-09', 'Pankhuri', 'Mahrotra', 'F', '2019-08-13') """)

dbm.export_data('select * from employees', 'csv')