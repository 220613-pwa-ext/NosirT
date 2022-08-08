import psycopg
from model.reimbs import Reimb


class ReimbDao:

    def get_reimbs (self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from ers_reimbursement")

                reimb_info = cur.fetchone()

                if reimb_info is None:
                    return None
                else:
                    reimb_id = reimb_info[0]
                    reimb_amount = reimb_info[1]
                    submitted = reimb_info[2]
                    resolved = reimb_info[3]
                    status = reimb_info[4]
                    type = reimb_info[5]
                    description = reimb_info[6]
                    recepit = reimb_info[7]
                    reimb_author = reimb_info[8]
                    reimb_resolver = reimb_info[9]

                    return Reimb(reimb_id, reimb_amount, submitted, resolved,status, type, description, recepit, reimb_author, reimb_resolver)


    def get_reimb_by_employee_id(self, u_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursement WHERE reimb_author = (%s)", (u_id,))

                reimbs_list = []
                reimb_info = cur.fetchall()
                if reimb_info is None:
                    return None
                else:
                    for row in reimb_info:
                        reimbs_list.append(Reimb(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                    return reimbs_list

    def get_reimb_by_manager_id(self, u_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursement WHERE reimb_resolver= %s", (u_id,))

                reimbs_list = []
                reimb_info = cur.fetchall()
                if reimb_info is None:
                    return None
                else:
                    for row in reimb_info:
                        reimbs_list.append(Reimb(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                    return reimbs_list

    def update_reimb_by_id(self, reimb_id, stat):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="nosir") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE ers_reimbursement SET status = %s WHERE reimb_id = %s RETURNING *", (stat, reimb_id))

                update_reimb_stat = cur.fetchone()
                if update_reimb_stat is None:
                    return None
                else:
                    conn.commit()
                    return Reimb(update_reimb_stat[0],update_reimb_stat[1], update_reimb_stat[2], update_reimb_stat[3], update_reimb_stat[4], update_reimb_stat[5], update_reimb_stat[6],
                                 update_reimb_stat[7], update_reimb_stat[8], update_reimb_stat[9])

