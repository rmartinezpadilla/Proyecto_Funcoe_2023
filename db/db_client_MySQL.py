import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'db': 'db_funcoe',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)