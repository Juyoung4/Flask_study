from dataclasses import dataclass
from datetime import datetime
from . import db

from werkzeug.security import check_password_hash, generate_password_hash

def registers(username, passwd = None):
    if db.get_db().execute(
        "select id FROM users WHERE username = ?", (username, )
    ).fetchone() is not None: # 중복 검사
        return False
    
    db.get_db().execute(
        "insert into users (username, passwd) values (?, ?)", (username, generate_password_hash(passwd), )
    )
    db.get_db().commit() # insert는 commit() 꼭!

    return True


def logins(username, passwd):
    cur = db.get_db().execute(
        "select * FROM users WHERE username = ?", (username, )
    ).fetchone()

    if cur is not None:
        if check_password_hash(passwd, cur['passwd']):
            return True
        else:
            return False
    return False