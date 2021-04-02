"""
File for working with DB
"""
import sqlite3
import sys
import icecream as ic
from sql_requests import create_clients_table_command, create_history_clients_table_command, \
    data_seeding_clients_table_command, data_seeding_history_clients_table_command, data_for_client_seeding, \
    data_for_history_client_seeding


class BaseDB:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
        except Exception as e:
            print('print from create_connection', e)
            sys.exit(1)


class CreateBD(BaseDB):
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_clients_table(conn, command):
        try:
            c = conn.cursor()
            c.execute(command)
        except Exception as e:
            print('print from create_clients_table_command', e)

    def create_history_clients_table(conn, command):
        try:
            c = conn.cursor()
            c.execute(command)
        except Exception as e:
            print('print from create_history_clients_table_command', e)


class DataSeeding(BaseDB):
    def __init__(self, db_file):
        super().__init__(db_file)

    def clients_data_seeding(conn, command, data):
        data = data_for_client_seeding
        try:
            c = conn.cursor()
            c.executemany(command, data)
        except Exception as e:
            print('print from data_seeding_clients_table_command', e)

    def history_clients_data_seeding(conn, command, data):
        data = data_for_history_client_seeding
        try:
            c = conn.cursor()
            c.executemany(command, data)
        except Exception as e:
            print('print from data_seeding_history_clients_table_command', e)


if __name__ == '__main__':
    BaseDB('messenger_db')
    CreateBD.create_clients_table(BaseDB('messenger_db').conn, create_clients_table_command)
    CreateBD.create_history_clients_table(BaseDB('messenger_db').conn, create_history_clients_table_command)
    DataSeeding.clients_data_seeding(BaseDB('messenger_db').conn, data_seeding_clients_table_command,
                                     data_for_client_seeding)
    DataSeeding.history_clients_data_seeding(BaseDB('messenger_db').conn, data_seeding_clients_table_command,
                                             data_for_history_client_seeding)
