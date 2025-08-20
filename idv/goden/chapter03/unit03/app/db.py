class Database:
    def __init__(self):
        self.storage = {}

    def save_user(self, user):
        """模擬存入資料庫"""
        self.storage[user["id"]] = user
        return True
