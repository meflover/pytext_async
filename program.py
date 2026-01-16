from aiogram.types import Message
from handlers.safesend import *
from session import session
from storage.sql import DSQL

class Editor:
    def __init__(self):
        self.pointers = [".", ",", "!", "?", ":", ";"]
        self.up_pointers = [".", "!", "?"]

    def commands_(self, user_text, text):
        parts = text.split()
        if not parts:
            return

        cmd = parts[0].lower()

        if cmd == "удали" and len(parts) >= 2:
            user_text = user_text.replace(parts[1], "")
            user_text = self.clear(user_text)
        elif cmd == "убери" and parts[1].lower() == "знаки":
            for p in self.pointers:
                user_text = user_text.replace(f"{p}", "")
                user_text = self.clear(user_text)
        elif cmd == "отзеркаль":
            user_text = "".join(reversed(user_text))
        elif cmd == "замени" and len(parts) >= 3:
            old = parts[1]
            new = parts[3] if len(parts) >= 4 and parts[2].lower() == "на" else parts[2]
            user_text = user_text.replace(old, new)
            
        else:
            user_text = self.clear(text)
        return user_text
    def clear(self, text):
        if not text:
            return text

        text = " ".join(text.split())

        for p in self.pointers:
            text = text.replace(f" {p}", p)

        chars = list(text.lower())
        chars[0] = chars[0].upper()

        for i in range(len(chars) - 2):
            if chars[i] in self.up_pointers and chars[i+1] == ' ':
                chars[i+2] = chars[i+2].upper()

        return "".join(chars)

    @staticmethod
    async def commands(message: Message):
        parts = message.text.split(maxsplit=1)
        if parts[0] == '/start':
            user_id = message.from_user.id
            if user_id in session.users:
                del session.users[user_id]
            user = session.short_init(user_id)
            await reply(message.reply, "Пришлите ваш текст!")
    @staticmethod
    async def message(message: Message):
        user = session.short_init(message.from_user.id)
        if user.text != None:
            user.text = program.commands_(user.text, message.text)
        elif user.text == None:
            user.text = program.clear(message.text)
        DSQL.putin(user.id, user.text)
        await answer(user.id, user.text)

program = Editor()