class Editor:
    def __init__(self):
        self.pointers = [".", ",", "!", "?", ":", ";"]
        self.up_pointers = [".", "!", "?"]

    def commands(self, user_text, text):
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
program = Editor()