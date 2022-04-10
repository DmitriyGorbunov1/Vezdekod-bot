import sqlite3

class DB():
    def __DB_connect(self):
        self.db_con = sqlite3.connect('VK_bot.db', check_same_thread=False)
        self.cursor = self.db_con.cursor()


    def __init__(self):
        self.__DB_connect()
        try:
            create_table_query1 = '''CREATE TABLE IF NOT EXISTS vk_bot_users (
                                user_id INTEGER PRIMARY KEY UNIQUE,
                                likes INTEGER,
                                dizlikes INTEGER);'''

            create_table_query2 = '''CREATE TABLE IF NOT EXISTS vk_bot_likes (
                                id INTEGER PRIMARY KEY UNIQUE,
                                likes INTEGER,
                                dizlikes INTEGER);'''

            self.cursor.execute(create_table_query1)
            self.cursor.execute(create_table_query2)

            self.db_con.commit()
            self.cursor.close() 
        
        finally:
            self.db_con.close()
    

    def __id_exist(self, user_id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT user_id FROM vk_bot_users WHERE user_id = {user_id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res != None
        finally:
            self.db_con.close()


    def get_likes_user(self, user_id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT likes FROM vk_bot_users WHERE user_id = {user_id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res
        finally:
            self.db_con.close()


    def get_dizlikes_user(self, user_id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT dizlikes FROM vk_bot_users WHERE user_id = {user_id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res
        finally:
            self.db_con.close()



    def get_likes_all(self):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT likes FROM vk_bot_likes WHERE id = {1}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res
        finally:
            self.db_con.close()


    def get_dizlikes_all(self):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT dizlikes FROM vk_bot_likes WHERE id = {1}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res
        finally:
            self.db_con.close()


    def __update_likes_all(self):
        try:
            res = self.get_likes_all()
            likes = res[0]
            likes += 1
            update_query = f"UPDATE vk_bot_likes SET likes = {likes} WHERE id = {1}"
            self.__DB_connect()
            self.cursor.execute(update_query)
            self.db_con.commit()
            self.cursor.close()
            del res
            del likes
        finally:
            self.db_con.close()


    def __update_dizlikes_all(self):
        try:
            res = self.get_dizlikes_all()
            dizlikes = res[0]
            dizlikes += 1
            update_query = f"UPDATE vk_bot_likes SET dizlikes = {dizlikes} WHERE id = {1}"
            self.__DB_connect()
            self.cursor.execute(update_query)
            self.db_con.commit()
            self.cursor.close()
            del res
            del dizlikes
        finally:
            self.db_con.close()


    def update_likes(self, user_id):
        try:
            if self.__id_exist(user_id):
                res = self.get_likes_user(user_id)
                likes = res[0]
                likes += 1
                self.__update_likes_all()
                update_query = f"UPDATE vk_bot_users SET likes = {likes} WHERE user_id = {user_id}"
                self.__DB_connect()
                self.cursor.execute(update_query)
                self.db_con.commit()
                self.cursor.close()
                del res
                del likes
            else:
                self.__insert_data(user_id, 1)
        finally:
            self.db_con.close()


    def update_dizlikes(self, user_id):
        try:
            if self.__id_exist(user_id):
                res = self.get_dizlikes_user(user_id)
                dizlikes = res[0]
                dizlikes += 1
                self.__update_dizlikes_all()
                update_query = f"UPDATE vk_bot_users SET dizlikes = {dizlikes} WHERE user_id = {user_id}"
                self.__DB_connect()
                self.cursor.execute(update_query)
                self.db_con.commit()
                self.cursor.close()
                del res
                del dizlikes
            else:
                self.__insert_data(user_id, 0, 1)
        finally:
            self.db_con.close()

    # def __update_data(self, user_id, grade_mode):
    #     self.__DB_connect()
    #     try:
    #         if grade_mode == "LIKE":
    #             self.__update_likes(user_id)
    #         elif grade_mode == "DIZ":
    #             self.__update_dizlikes(user_id)
    #         print("dt upt")
    #         self.db_con.commit()
    #         self.cursor.close()

    #     finally:
    #         self.db_con.close()
    #         print("upd dt con close")

    

    def __insert_data(self, user_id, likes=0, dizlikes=0):
        try:
            insert_query = "INSERT INTO vk_bot_users VALUES (?, ?, ?)"
            self.__DB_connect()
            self.cursor.execute(insert_query, (user_id, likes, dizlikes))
            self.db_con.commit()
            self.cursor.close()
        finally:
            self.db_con.close()


    