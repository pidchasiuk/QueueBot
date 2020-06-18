import sqlite3

db_file = 'queue.db'


def create_table_queue():
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute(
                """CREATE TABLE queue_temp (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)""")
            db.commit()
            return True
        except Exception as e:
            print(e)
            return False


def del_table_queue():
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute(
                """ DROP TABLE IF EXISTS queue_temp; """)
            db.commit()
            return True
        except Exception as e:
            print(e)
            return False


def add_user(name):
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute("""INSERT INTO queue_temp (name) VALUES (?)""", (name,))
            db.commit()
        except Exception as e:
            print(f"Exception adding user, {e}")
            db.rollback()


def del_user(name):
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute("""DELETE FROM queue_temp WHERE name=?""", name)
            db.commit()
        except Exception as e:
            print(f"Exception del user, {e}")
            db.rollback()


def del_all_users():
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute("""DELETE FROM queue_temp""")
            db.commit()
        except Exception as e:
            print(f"Exception del user, {e}")
            db.rollback()


def get_id_name():
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute("""SELECT id, name FROM queue_temp ORDER BY id""")
            # print(c.fetchall())
            name = c.fetchall()
            return name
        except Exception as e:
            print(f"get_name Exception: {e}")


def get_name(id):
    with sqlite3.connect(db_file) as db:
        try:
            c = db.cursor()
            c.execute("""SELECT name FROM queue_temp WHERE id=?""", id)
            name = c.fetchone()
            return name[0]
        except Exception as e:
            print(f"get_name Exception: {e}")

