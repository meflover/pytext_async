import sqlite3 as sq
class DatabaseSQL:
    def __init__(self):
        self.database = "storage/form.db"
   
    def get(self, user_id):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            query = f'SELECT text FROM users WHERE tg_id = ?'
            result = cur.execute(query, (user_id,)).fetchone()
            return result[0] if result else None

    def putin(self, user_id, text):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            exists = cur.execute('SELECT 1 FROM users WHERE tg_id = ?', (user_id,)).fetchone()
            if exists:
                cur.execute(f'UPDATE users SET text = ? WHERE tg_id = ?', (text, user_id))
            else:
                cur.execute(
                    '''INSERT INTO users 
                    (tg_id, text)
                    VALUES (?, ?)''',
                    (user_id, text)
                )
            con.commit()

DSQL = DatabaseSQL()