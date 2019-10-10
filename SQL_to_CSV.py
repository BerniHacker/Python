# Note: this program is written to run in python 2

# This script queries the full content of a defined table of a defined MySQL
# database (with defined credentials) and stores the result of the query
# temporarily into a pandas dataframe.
# The content of the dataframe is then dumped into a file with a defined name.
# The script allows handling "large data".
# The SQL query is performed in chunks according to SQL_BATCH_SIZE.
# The dump into the CSV file is done in chunks according to PANDAS_BATCH_SIZE.
# This allows controlling the load on SQL and allows keeping the required memory
# at a low enough value.
# It is assumed that the table has a primary key called: id

import mysql.connector
import pandas as pd
import datetime as dt

# Defining the values of the global variables
# (write the data before running the script)
USER = 'dbuser'  # 'user'
PASSWORD = 'password'  # 'password'
HOST = 'dbaddress'  # 'host'
DATABASE = 'dbname'  # 'database_name'
TABLE = 'tablename'  # 'table_name'
COLUMNS = ['id',  # this is the primary key
           'column2',  # column 2
           'column3',  # column 3
           'column4',  # column 4
           'column5',  # column 5
           'column6',  # column 6
           'column7',  # column 7
           'column8',  # column 8
           'column9',  # column 9
           'column10']  # column 10
# add or delete columns as needed
FILE_NAME = '/path/filename.csv'  # 'file_name with path'
# (the extension shall be .csv)

# Global variable with pre-assigned default values
# (customize the values as needed)
LAST_ID = 0  # an integer stating which is the last id that has been copied
# in the file
SQL_BATCH_SIZE = 1000  # integer
PANDAS_BATCH_SIZE = 10000  # integer that shall be a multiple of SQL_BATCH_SIZE

# Initializing an empty dataframe
df_template = pd.DataFrame(columns=COLUMNS)
# Creating a CSV file and copying the empty dataframe with the headers
# (table column names) into it
df_template.to_csv(FILE_NAME, encoding='utf-8', index=False)


def max_id_value(db_user, db_password, db_host, database_name, db_table):
    # This function performs a query to the table of the database and returns
    # the max value of the id.

    # Connecting to the database
    conn = mysql.connector.connect(user=db_user,
                                   password=db_password,
                                   host=db_host,
                                   database=database_name)

    # Fetching the max id
    cursor = conn.cursor()
    sql = "SELECT MAX(id) FROM " + db_table
    cursor.execute(sql)
    # Storing the result of the SQL query
    max_id_list = cursor.fetchall()  # this is a one element list of (one) tuple
    conn.commit()
    # Extracting the actual value and printing it
    max_id = max_id_list[0][0]
    print "Currently, the highest id value of the", db_table, \
          "table is:", max_id, "\n"

    # Closing the connection to the database
    conn.close()

    return max_id


def db_query(db_user, db_password, db_host, database_name, db_table, table_col, last_id,  SQL_batch_size, Pandas_batch_size):
    # This function performs a query to the database and returns an amount of
    # entries defined by Pandas_batch_size in dataframe format.
    # The function returns also the highest value of the id contained
    # in the dataframe and the amount of  processed entries.
    # The input parameter last_id is the value of last handled id.

    # Connecting to the database
    conn = mysql.connector.connect(user=db_user,
                                   password=db_password,
                                   host=db_host,
                                   database=database_name)

    # Initializing a dataframe to contain the result of the SQL queries
    # to the database and a variable that contains the value of the maximum id
    result = pd.DataFrame(columns=table_col)
    max_id_df = 0

    # Executing the queries to fetch the data
    # Initializing the loop variables
    i = 0  # this variable controls the Pandas batch size
    r = last_id + 1  # this variable controls the value of the id
    print "****************************************\n"
    print "Copying to the dataframe ..."
    while i < Pandas_batch_size:
        # Fetching the full content of the rows in chunks according to
        # SQL_BATCH_SIZE
        cursor = conn.cursor()
        sql = "SELECT * FROM " + db_table + \
              " WHERE id >= %s AND id < %s + %s"
        cursor.execute(sql, (r, r, SQL_batch_size))
        # Storing the result of the SQL query
        result_list = cursor.fetchall()  # this is a list of tuples
        conn.commit()
        # Incrementing the loop variables
        i += SQL_batch_size
        r += SQL_batch_size
        # If the result of the SQL query is not empty, store it in dataframe
        # format
        ind = range(len(result_list))
        if len(result_list) != 0:
            result_df = pd.DataFrame(result_list, columns=table_col, index=ind)
            # Add the content of the dataframe to the final result
            result = result.append(result_df, ignore_index=True)
            print i, "id values have been processed"
            # Fetching the max value of the id from the dataframe
            max_id_df = result['id'].max()

    # Printing the number of entries of the dataframe
    proc_entries = len(result.index)
    print "\nA total of", proc_entries, "entries have been added to "\
          "the dataframe.\n"

    # Closing the connection to the database
    conn.close()

    return result, max_id_df, proc_entries


def dataframe_storage(dataframe, file_name):
    # This function takes a dataframe and stores it into a file.

    # Opening the file in append mode
    with open(file_name, 'a') as csv_file:
        # Appending the dataframe named dataframe into the csv file
        # (header=False is used to avoid copying the column names over and over)
        dataframe.to_csv(csv_file, encoding='utf-8', index=False, header=False)
    print "The dataframe has been saved into the CSV file:", file_name, "\n"


# Welcome message
print "\nThis script queries all the entries of the", TABLE, "table in "\
      "the \n", DATABASE, "database, stores them temporarily into a pandas "\
      "dataframe and \nthen dumps the content of the dataframe into the "\
      "file", FILE_NAME, ".\n"\
      "Both the SQL query and the dump into the CSV file are done in chunks.\n"

# Storing and printing the script start time
start_time = dt.datetime.utcnow()
print "Script start time (UTC):", start_time, "\n"

# Calling the functions
# Retreving the highest value of the id in the table from the database
max_id = max_id_value(USER, PASSWORD, HOST, DATABASE, TABLE)
# Initializing a loop variable indicating the last handled id value
last_id_value = LAST_ID
# Initializing a variable indicating the amount of processed entries
process_entries = 0
while last_id_value < max_id:
    # Performing the query the the Audit Trail database
    db_query_result = db_query(USER, PASSWORD, HOST, DATABASE, TABLE, COLUMNS, last_id_value, SQL_BATCH_SIZE, PANDAS_BATCH_SIZE)
    # Extracting the content of the dataframe
    result_dataframe = db_query_result[0]
    # Extracting the value of the last handled id
    max_id_dataframe = db_query_result[1]
    # Updating the amount of processed entries
    process_entries += db_query_result[2]
    # Appending the content of the dataframe into a CSV file
    dataframe_storage(result_dataframe, FILE_NAME)
    # Updating the loop variable
    last_id_value = max_id_dataframe
    print "Last handled id:", last_id_value, "\n"
    print "Total amount of entries added to the file so far:", \
          process_entries, "\n"

# Storing the script end time
end_time = dt.datetime.utcnow()
# Printing the total amount of handles entries, the script end time and
# the script duration
print "****************************************\n"
print "Total amount of entries added to the file:", process_entries, "\n"
print "Script end time (UTC):", end_time
print "Script duration:", end_time - start_time, "\n"