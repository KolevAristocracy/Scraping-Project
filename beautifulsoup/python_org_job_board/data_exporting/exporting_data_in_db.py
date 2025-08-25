import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DatabaseManager:

    def __init__(self, db_name, user, password, host='127.0.0.1', port='5432'):

        print(f'Initializing database connection to {db_name} at {host}:{port}...')

        # Establish a connection to the PostgreSQL database
        self.connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        # Set autocommit to avoid manual transaction management
        self.connection.autocommit = True
        # Create a cursor object that interacts with the database
        self.cursor = self.connection.cursor()
        print('Database connection established.')


    def create_table(self, table_sql):
        try:
            print('Attempting to create table ...')
            # Execute the SQL command to create the table
            self.cursor.execute(table_sql)
            print('Table created or already exists.')
        except psycopg2.Error as e:
            # Print an error message if the table creation fails
            print(f'Error creating table: {e}')

    def insert_csv(self, table_name, csv_file):
        try:
            print(f'Loading data from {csv_file} into {table_name}...')
            # Use COPY to quickly load a large amount of data from a CSV file into the table
            with open(csv_file, 'r') as f:
                self.cursor.copy_expert(
                    "COPY oop_data (title, location, job_type, posted, category, link)"
                       " FROM STDIN WITH CSV HEADER "
                       "DELIMITER ','", f)
                print('Data loaded successfully')
        except Exception as e:
            # Print error message if data loading fails
            print(f'Error loading data: {e}')

    def fetch_all(self, query):
        try:
            print(f'Executing query: {query}')
            # Execute the provided query
            self.cursor.execute(query)

            # Fetch all results and return them as a list of tuples
            results = self.cursor.fetchall()
            print(f'Retrieved {len(results)} rows.')
            return results

        except psycopg2.Error as e:
            # Print error message if the query execution fails
            print(f'Error fetching data: {e}')
            return None

    def close(self):
        print('Closing database connection...')
        # Close the connection to free up resources
        self.connection.close()
        print('Database connection closed.')

def main():
    # Initialize the DatabaseManager with credentials from environment variables
    db = DatabaseManager(
        db_name='web_scraping_db',
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    # Define the SQL command to create the jobs table if it doesn't exist
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS oop_data(
            id INTEGER GENERATED ALWAYS AS IDENTITY,
            title varchar(100) UNIQUE,
            location varchar(100),
            job_type varchar(100),
            posted date, 
            category varchar(100),
            link varchar(100)
        );
    '''

    db.create_table(create_table_sql)
    # Load data from the CSV file into the database table
    db.insert_csv('oop_data', '../scraper_oop/oop_data.csv')
    print('Fetched data:')
    # Fetch and print all data from the jobs table
    for row in db.fetch_all('SELECT * FROM oop_data;'):
        print(row)
    # Close database connection
    db.close()

# Run the main function if this file is executed directly
if __name__ == '__main__':
    main()
