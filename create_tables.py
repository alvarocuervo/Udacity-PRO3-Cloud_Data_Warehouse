import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

""" drop tables from DROP 
    queries (drop_table_queries list)
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

""" create tables from CREATE queries 
    (create_table_queries list)
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting...')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    print('Dropping tables...')
    drop_tables(cur, conn)
    print('Creating tables...')    
    create_tables(cur, conn)

    conn.close()
    print('Connection closed.')    


if __name__ == "__main__":
    main()