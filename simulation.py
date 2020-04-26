import random
import sys
import csv
from contests import contests
from terminaltables import AsciiTable, SingleTable
from model_index import scores
from termcolor import colored
from itertools import zip_longest

results = []

democrat_ec = []
republican_ec = []

def state_election():
    for key, value in contests.items():

        democratic_average = value[2]
        republican_average = value[3]

        model_index_d = scores[key][0]
        model_index_r = scores[key][1]

        temp = []

        for _ in range (100000):
            simulation = random.choices(['D', 'R', 'T'], [(int(democratic_average) + model_index_d), (int(republican_average) + model_index_r), 1])
        
            if 'D' in simulation:
                temp.append('D')

            if 'R' in simulation:
                temp.append('R')

            if 'T' in simulation:
                temp.append('T')

        if temp.count('D') > temp.count('R'):
            party = 0

            margin = round((temp.count('D') / 1000), 2) - round((temp.count('R') / 1000), 2)
            if margin > 15:
                party = 1
            elif margin > 7.5:
                party = 2
            elif margin > 0:
                party = 3
            # print(margin, party)
            
            results.append({key: [value[0], value[1], str(party), str(round((temp.count('D')/1000), 2)) + '%', str(round((temp.count('R')/1000), 2)) + '%', str(round((temp.count('T')/1000), 2)) + '%', 'Biden +' + str(round((temp.count('D')/1000) - (temp.count('R')/1000), 2)) + '%','D']})
            democrat_ec.append(int(value[1]))

        if temp.count('R') > temp.count('D'):
            party = 0

            margin = round((temp.count('R') / 1000), 2) - round((temp.count('D') / 1000), 2)
            if margin > 15:
                party = 6
            elif margin > 7.5:
                party = 5
            elif margin > 0:
                party = 4
            # print(margin, party)
            results.append({key: [value[0], value[1], str(party), str(round((temp.count('D')/1000), 2)) + '%', str(round((temp.count('R')/1000), 2)) + '%', str(round((temp.count('T')/1000), 2)) + '%', 'Trump +' + str(round((temp.count('R')/1000) - (temp.count('D')/1000), 2)) + '%','R']})
            republican_ec.append(int(value[1]))



def run():
    state_election()
    for index in range(len(results)):
        print(results[index])


def output():
    state_election()
    for index in range(len(results)):
        print(results[index])
    print(sum(democrat_ec), sum(republican_ec))
    with open('results.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile,
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["id", "name", "ec", "party", "democrat", "republican", "third", "margin", "winner"])
        for index in range(len(results)):
            for key, value in results[index].items():
                filewriter.writerow([value[0], key, value[1], value[2], value[3], value[4], value[5], value[6], value[7]])

    print('File outputed as output.csv')

output()
    
# def win_probability ():
#     democrat_probability = results.count('D') / 100
#     republican_probability = results.count('R') / 100
#     tie_probability = results.count('T') / 100

#     table_data = [
#     [colored('DEMOCRAT', 'white', 'on_blue'), colored('REPUBLICAN', 'white', 'on_red'), 'TIE', 'TOTAL'],
#     [str(democrat_probability) + '%', str(republican_probability) + '%', str(tie_probability) + '%',
#         str(democrat_probability + republican_probability + tie_probability) + '%']
#     ]
#     table = SingleTable(table_data)
#     table.title = 'GE Chances [k=10000]'
#     table.justify_columns[0] = 'center' 
#     table.justify_columns[1] = 'center'
#     table.justify_columns[2] = 'center'  

#     print (table.table)

# if __name__ == '__main__':
#     try:

#         if sys.argv[1] == 'single':
#             state_election()
#             se_table_data = [
#             [colored('DEMOCRAT', 'white', 'on_blue'), colored('REPUBLICAN', 'white', 'on_red'), 'TOTAL'],
#             [str(sum(democrat_electors)), str(sum(republican_electors)), str(sum(democrat_electors) + sum(republican_electors))]
#             ]
#             se_table = SingleTable(se_table_data)
#             se_table.title = 'GE Simulation'
#             se_table.justify_columns[0] = 'center' 
#             se_table.justify_columns[1] = 'center'
#             se_table.justify_columns[2] = 'center' 
#             print (se_table.table)

#         if sys.argv[1] == 'states':
#             state_election()
#             se_table_data = [
#             [colored('DEMOCRAT', 'white', 'on_blue'), colored('REPUBLICAN', 'white', 'on_red'), 'TOTAL'],
#             ['\n'.join([str(i) for i in democrat_states]), '\n'.join([str(i) for i in republican_states]), str(len(democrat_states) + len(republican_states))],
#             [sum(democrat_electors), sum(republican_electors), (sum(democrat_electors)+ sum(republican_electors))]
#             ]
#             se_table = SingleTable(se_table_data)
#             se_table.title = 'GE Simulation'
#             se_table.inner_row_border = True
#             se_table.justify_columns[0] = 'center' 
#             se_table.justify_columns[1] = 'center'
#             se_table.justify_columns[2] = 'center' 
#             print(se_table.table)

#         elif sys.argv[1] == 'csv':
#             state_election()
#             with open('results.csv', 'w') as csvfile:
#                 filewriter = csv.writer(csvfile,
#                                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                 filewriter.writerow(["State", "Party"])
#                 for i in democrat_states:
#                     filewriter.writerow([i,"D"])

#                 for i in republican_states:
#                     filewriter.writerow([i,"R"])
                
#                 filewriter.writerow([sum(democrat_electors), sum(republican_electors)])
#             print('File outputed as output.csv')

            
#     except:
#         for _ in range(10000):
#             democrat_electors = []
#             republican_electors = []
#             state_election()
#         win_probability()

#         # print(democrat_states)
#         # print(republican_states)