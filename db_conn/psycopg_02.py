import psycopg2
import credentials

connection = credentials.connection

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a query to list all tables in the database
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

# Fetch all results and print them
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()
