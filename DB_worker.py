import sqlite3 as sql


class Database_worker():

    def __init__(self, base_name=':memory:'):
        self.base_name = base_name

    def open_connect(self):
        return sql.connect(self.base_name)

    def close_connect(self, con):
        con.close()


class Test_table_Worker():

    def __init__(self, table_name, connect):
        self.main_cur = self.create_cursor(connect)
        self.table_name = table_name

    @classmethod
    def create_cursor(cls, connect):
        return connect.cursor()

    def get_rows_by_factor(self, factor, count=-1, columns="*"):
        self.main_cur.execute("SELECT {0} FROM {1} WHERE factor LIKE {2}".format(columns, self.table_name, factor))
        if count <= 0:
            res = self.main_cur.fetchall()
        else:
            res = self.main_cur.fetchmany(count)
        return res

    def get_all_column_names(self):
        get_column_names = self.main_cur.execute("select * from {0} limit 1".format(self.table_name))
        col_name = [i[0] for i in get_column_names.description]
        return col_name