from session import session
from program import program 
from storage.sql import DSQL
from config import local_id

user = session.short_init(local_id)

while True:
    text = input("TEXT: ")
    if user.text != None:
        user.text = program.commands(user.text, text)
    elif user.text == None:
        user.text = program.clear(text)

    DSQL.putin(user.id, user.text)
    print("RESULT:",user.text)