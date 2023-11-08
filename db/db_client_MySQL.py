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

#librerías
# pip install fastapi[all]
# pip install sqlalchemy
# pip install mysql
# pip install mysql-connector-python-rf
# pip install uvicorn[standard]