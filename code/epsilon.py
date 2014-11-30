#encoding=utf-8
import sys
import MySQLdb
import random

execfile("core.py")

con = MySQLdb.connect(host="1.1.6.7", user="user", passwd="passwd", db="db", charset="utf8")
cursor = con.cursor()
#sql = "select * from journal_read_score_step2"
sql = "select * from journal_read_score_step2"
cursor.execute(sql)
results = cursor.fetchall()
last_bookid = ""
kv = {}
kcv = {} #simple key, complex value
# record[0]: book_id
# record[1]: user_id
'''
kv['02300097'] = ['186845', '174048']
kv['02300098'] = ['186846', '174041']

kcv['0230097'] = [{'186845':0.08}, {'174048':1.0}]
'''

for record in results:
        if last_bookid == "":
                last_bookid = str(record[0])
                kv[last_bookid] = []
                kcv[last_bookid] = []

                kv[last_bookid].append(str(record[1]))
                v = {}
                v[str(record[1])] = float(str(record[-2]))
                kcv[last_bookid].append(v)
        elif last_bookid == str(record[0]):
                kv[last_bookid].append(str(record[1]))
                v = {}
                v[str(record[1])] = float(str(record[-2]))
                kcv[last_bookid].append(v)
        else:
                last_bookid = str(record[0])
                kv[last_bookid] = []
                kcv[last_bookid] = []

                kv[last_bookid].append(str(record[1]))
                v = {}
                v[str(record[1])] = float(str(record[-2]))
                kcv[last_bookid].append(v)

f = open("mail_list.txt", "w")
sys.stdout = f

dictByUser = {}
# dictByUser = {'userid':[bookid, bookid, ...], 'userid':[bookid, bookid], ...}

for key,value in kv.items():
        #f.write(key +  value);
        #print(key, value)
        #v = value
        max_val = max(value)
        max_index = value.index(max_val)
        idx = max_index
        eps = 0.3
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
        print (key, value)

