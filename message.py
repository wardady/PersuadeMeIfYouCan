class temp_msg:
    def __init__(self, chat_id, text):
        self.chat = chat(chat_id)
        self.text = text


class chat:
    def __init__(self, id):
        self.id = id
