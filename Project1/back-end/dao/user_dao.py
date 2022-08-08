import psycopg

from model.user import User

class UserDao:

    def get_user_by_username_password(self, username, password):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from ers_users WHERE username = %s AND p_word = %s", (username, password))

                user_information = cur.fetchone()

                if user_information is None:
                    return None
                else:
                    u_id = user_information[0]
                    username = user_information[1]
                    password = user_information[2]
                    first_name = user_information[3]
                    last_name = user_information[4]
                    email = user_information[5]
                    gender = user_information[6]
                    phone_number = user_information[7]
                    role = user_information[8]

                    return User(u_id, username, password, first_name, last_name, gender, email, phone_number, role)

    def get_user_by_username(self,username):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from ers_users WHERE username = %s", (username,))

                user_information = cur.fetchone()

                if user_information is None:
                    return None

                username = user_information[0]
                password = user_information[1]
                first_name = user_information[2]
                last_name = user_information[3]
                gender = user_information[4]
                email = user_information[5]
                phone_number = user_information[6]
                role = user_information[7]

                return User(None, username, password, first_name, last_name, gender, email, phone_number, role)

    def add_user(self, user_obj):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO ers_users VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (user_obj.username, user_obj.password, user_obj.first_name, user_obj.last_name, user_obj.gender,
                                                                                       user_obj.email, user_obj.phone_number, user_obj.role))

                user_inserted = cur.fetchone()
                if user_inserted is None:
                    return None
                else:
                    return User(None, user_inserted[0], user_inserted[1], user_inserted[2], user_inserted[3], user_inserted[4], user_inserted[5], user_inserted[6], user_inserted[7])

