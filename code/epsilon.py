#encoding=utf-8
import sys
import MySQLdb
import random

execfile("core.py")

con = MySQLdb.connect(host="1.1.6.7", user="user", passwd="passwd", db="db", charset="utf8")
cursor = con.cursor()
#sql = "select * from journal_read_score_step2"
sql = "select * from journal_read_score_step2 limit 100"
cursor.execute(sql)
results = cursor.fetchall()
last_bookid = ""
kv = {}
# record[0]: book_id
# record[1]: user_id
'''
kv['02300097'] = ['186845', '174048']
kv['02300098'] = ['186846', '174041']
'''
for record in results:
        if last_bookid == "":
                last_bookid = str(record[0])
                kv[last_bookid] = []
                kv[last_bookid].append(str(record[1]))
        elif last_bookid == str(record[0]):
                kv[last_bookid].append(str(record[1]))
        else:
                last_bookid = str(record[0])
                kv[last_bookid] = []
                kv[last_bookid].append(str(record[1]))

for key,value in kv.items():
        print(key, value)
'''
random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
random.shuffle(means)
arms = map(lambda (mu): BernoulliArm(mu), means)
print("Best arm is " + str(ind_max(means)))

f = open("standard_results.tsv", "w")

for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
  algo = EpsilonGreedy(epsilon, [], [])
  algo.initialize(n_arms)
  results = test_algorithm(algo, arms, 50, 25)
  for i in range(len(results[0])):
      f.write(str(epsilon) + "\t")
      f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")
f.close()
'''
