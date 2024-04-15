#!/usr/bin/python3
"""Start link class to table in database
Defines a `State` class and a `Base` class to work with `MySQLAlchemy` ORM.
This script is designed to be run as the main entry point of a Python module.
It initializes a database engine using SQLAlchemy and MySQL, based on the
provided command-line arguments. The command-line arguments are expected
to be the username, password, and database name respectively.
The script then creates all tables defined in the Base metadata
if they do not already exist in the specified database.
Usage:
    <python-version> <script_name.py> <username> <password> <database_name>
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """Initialize the database engine and
    create tables if they do not exist.
    Args:
    username (str): The username for accessing the MySQL database.
    password (str): The password for accessing the MySQL database.
    database_name (str): The name of the MySQL database to connect to.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
