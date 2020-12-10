import sqlite3
import bcrypt

def add_points(username='hagay', points_to_add= 10):
    print('adding points')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    quary = '''UPDATE users SET points = points + {}
    WHERE username = '{}';'''
    cursor.execute(quary.format(points_to_add, username))
    conn.commit()
    conn.close()
    return


add_points()

print(dir(bcrypt))

bcrypt.checkpw(b'123', b'1')

