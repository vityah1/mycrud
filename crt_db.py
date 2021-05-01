import sqlite3
conn = sqlite3.connect('courses_db.db')
c = conn.cursor()

def setup_database():
# Create table
    print ('Init...')
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS courses
     (id integer primary key,name text, dbegin text, dend text, cntlections integer)''')
    except:
        print ('Table exist!')
    print  ('Table check ok')
    conn.close()
    print('Do Exit...')
    exit()


if __name__=='__main__':
	setup_database()