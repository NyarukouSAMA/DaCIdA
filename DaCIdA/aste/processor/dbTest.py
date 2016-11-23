import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('../database/ASTE.db')

    cur = con.cursor()
    sql_script = """
        SELECT mi.code_string FROM module_info as mi
            WHERE mi.module_id = {0}
        """.format('1')
    cur.execute(sql_script)

    data = cur.fetchone()[0]

    if data:
        print(data)
    else:
        print('None')

except lite.Error as e:
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()