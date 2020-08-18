import csv
<<<<<<< HEAD
with open('states_weighted.csv', mode='r') as infile:
=======
with open('states_august_weighted.csv', mode='r') as infile:
>>>>>>> 7d5df8b66ea21f079d224bcc83d0e424da47c1b7
    reader = csv.reader(infile)
    contests = {rows[0]:rows[1:11] for rows in reader}
    del contests['State']