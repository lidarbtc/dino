from flask import session

def login():
    if 'user' in session:
        return True
    return False