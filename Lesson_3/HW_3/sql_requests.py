import time

create_clients_table_command = """
        CREATE TABLE IF NOT EXISTS clients (
	id integer PRIMARY KEY AUTOINCREMENT,
	user_name text NOT NULL,
	password text NOT NULL
);
"""

create_history_clients_table_command = """
        CREATE TABLE IF NOT EXISTS history_clients (
	id integer PRIMARY KEY AUTOINCREMENT,
	user_id text NOT NULL,
	enter_time datetime,
	ip_addr text, 
	FOREIGN KEY (user_id) REFERENCES clients (id)
);
"""

# data_seeding_clients_table_command = """
#     INSERT INTO clients (user_name, password)
#     VALUES ('Client_1', 'pass_1');
# """

# data_seeding_clients_table_command = """
#     INSERT INTO clients (user_name, password)
#     VALUES ('Client_1', 'pass_1');
#     VALUES ('Client_2', 'pass_2');
#     VALUES ('Client_3', 'pass_3');
# """

data_for_client_seeding = [('Client_1', 'pass_1'), ('Client_2', 'pass_2'), ('Client_3', 'pass_3')]

data_seeding_clients_table_command = """
    INSERT INTO clients (user_name, password)
    VALUES ('?', '?');
"""

data_for_history_client_seeding = [('1', time.time(), '127.0.0.1'),
                                   ('2', time.time(), '126.0.0.1'),
                                   ('3', time.time(), '125.0.0.1')]

data_seeding_history_clients_table_command = """
    INSERT INTO history_clients (user_id, enter_time, ip_addr)
    VALUES ('?', '?', '?');
"""

# data_seeding_history_clients_table_command = """
#     INSERT INTO history_clients (user_id, enter_time, ip_addr)
#     VALUES ('1', datetime('now'), '127.0.0.1');
#     # VALUES ('2', datetime('now'), '126.0.0.1');
#     # VALUES ('3', datetime('now'), '125.0.0.1');
# """