import sqlite3, re

from utils import myLog


def do_sql_cmd(sql=""):
    conn = sqlite3.connect("courses_db.db")
    c = conn.cursor()
    sql = sql.strip()
    if re.search(r"^insert|^update|^delete", sql, re.I):
        try:
            res = c.execute(sql)
            conn.commit()
            return {"rowcount": c.rowcount, "data": "ok"}
        except Exception as e:
            myLog(f"""def do_sql_cmd: error exec sql:\n{e}\n{sql}""", 1)
            return {"rowcount": -1, "data": e}
    elif re.search(r"^select|^width", sql, re.I):
        try:
            res = c.execute(sql).fetchall()
            return {"rowcount": len(res), "data": res}
        except Exception as e:
            myLog(f"""def do_sql_cmd: error exec sql:\n{e}\n{sql}""")
            return {"rowcount": -1, "data": f"""{e}\n{sql} """}
    else:
        myLog(f"""not valid sql\n{sql}""")
        return {"rowcount": -1, "data": "unknown query"}
