from class_ import TelegramUser
from storage.sql import DSQL
class SessionStore:
    def __init__(self):
        self.users = {}
    def short_init(self, user_id: int) -> TelegramUser:
        if user_id not in self.users:
            self.users[user_id] = TelegramUser(user_id)
        self.users[user_id].text = DSQL.get(user_id)
        return self.users[user_id]     
session = SessionStore()