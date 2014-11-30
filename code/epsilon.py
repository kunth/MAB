#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import random

execfile("core.py")

con = MySQLdb.connect(host="", user="", passwd="", db="", charset="utf8")
cursor = con.cursor()
#sql = "select * from journal_read_score_step2"
sql = "select * from journal_read_score"
cursor.execute(sql)
results = cursor.fetchall()
last_bookid = ""
kv = {}
kcv = {} #simple key, complex value
# record[3]: book_id
# record[2]: user_id
# record[-2]: score
'''
kv['02300097'] = ['186845', '174048']
kv['02300098'] = ['186846', '174041']

kcv['0230097'] = [{'186845':0.08}, {'174048':1.0}]
'''

for record in results:
        score = float(record[-2])
        user_id = str(record[2])
        book_id = str(record[3])
        if last_bookid == "":
                last_bookid = book_id
                kv[last_bookid] = [user_id]
                v = {}
                v[user_id] = score
                kcv[last_bookid] = [v]
        elif last_bookid == book_id:
                kv[last_bookid].append(user_id)
                v = {}
                v[user_id] = score
                kcv[last_bookid].append(v)
        else:
                last_bookid = book_id

                kv[last_bookid] = [user_id]
                v = {}
                v[user_id] = score
                kcv[last_bookid] = [v]

f = open("mail_list_simple.txt", "w")
sys.stdout = f

dictByUser = {}
# dictByUser = {'userid':[bookid, bookid, ...], 'userid':[bookid, bookid], ...}

for key,value in kv.items():
        #print(key, value)
        # if a book is viewed by less than 3 person, it would be filtered in this test.
        if len(value) < 3:
                continue
        max_val = max(value)
        max_index = value.index(max_val)
        idx = max_index
        eps = 0.3
        # explore
        if random.random < eps:
                idx = random.randint(0, len(value)-1)

        if value[idx] in dictByUser:
                dictByUser[value[idx]].append(key)
        else:
                dictByUser[value[idx]] = [key]


for key,value in dictByUser.items():
        #sorted(value, reverse = True)
        # make sure that the number of the mail that every user receives is less than 5
        #print (key, value[:5])
        print (key, value[:10])
