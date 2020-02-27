import random
from contests import contests
from terminaltables import AsciiTable, SingleTable
from model_index import scores
import sys
import csv
from termcolor import colored
from itertools import zip_longest

results = []

democrat_electors = []
republican_electors = []

democrat_states = []
republican_states = []

def state_election():
    for key, value in contests.items():

        democratic_average = value[1]
        republican_average = value[2]

        model_index_d = scores[key][0]
        model_index_r = scores[key][1]

        simulation = random.choices(['D', 'R'], [(int(democratic_average) + model_index_d), (int(republican_average) + model_index_r)])
        
        if 'D' in simulation:
            democrat_electors.append(int(value[0]))
            democrat_states.append(key)

        if 'R' in simulation:
            republican_electors.append(int(value[0]))
            republican_states.append(key)

    if sum(democrat_electors) > sum(republican_electors):
        results.append('D')

    if sum(democrat_electors) == sum(republican_electors):
        results.append('T')
    
    if sum(democrat_electors) < sum(republican_electors):
        results.append('R')
    
def win_probability ():
    democrat_probability = results.count('D') / 100
    republican_probability = results.count('R') / 100
    tie_probability = results.count('T') / 100

    table_data = [
    [colored('DEMOCRAT', 'white', 'on_blue'), colored('REPUBLICAN', 'white', 'on_red'), 'TIE', 'TOTAL'],
    [str(democrat_probability) + '%', str(republican_probability) + '%', str(tie_probability) + '%',
        str(democrat_probability + republican_probability + tie_probability) + '%']
    ]
    table = SingleTable(table_data)
    table.title = 'GE Chances [k=10000]'
    table.justify_columns[0] = 'center' 
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'center'  

    print (table.table)

if __name__ == '__main__':
    try:

        if sys.argv[1] == 'single':
            state_election()
            se_table_data = [
            [colored('DEMOCRAT', 'white', 'on_blue'), colored('REPUBLICAN', 'white', 'on_red'), 'TOTAL'],
            [str(sum(democrat_electors)), str(sum(republican_electors)), str(sum(democrat_electors) + sum(republican_electors))]
            ]
            se_table = SingleTable(se_table_data)
            se_table.title = 'GE Simulation'
            se_table.justify_columns[0] = 'center' 
            se_table.justify_columns[1] = 'center'
            se_table.justify_columns[2] = 'center' 
            print (se_table.table)

        if sys.argv[1] == 'states':
            state_election()
            se_table_data = [
            [colored('DEMOCRAT', 'white', 'on_blue'), colored('REPUBLICAN', 'white', 'on_red'), 'TOTAL'],
            ['\n'.join([str(i) for i in democrat_states]), '\n'.join([str(i) for i in republican_states]), str(len(democrat_states) + len(republican_states))],
            [sum(democrat_electors), sum(republican_electors), (sum(democrat_electors)+ sum(republican_electors))]
            ]
            se_table = SingleTable(se_table_data)
            se_table.title = 'GE Simulation'
            se_table.inner_row_border = True
            se_table.justify_columns[0] = 'center' 
            se_table.justify_columns[1] = 'center'
            se_table.justify_columns[2] = 'center' 
            print(se_table.table)

        elif sys.argv[1] == 'csv':
            state_election()
            with open('results.csv', 'w') as csvfile:
                filewriter = csv.writer(csvfile,
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["State", "Party"])
                for i in democrat_states:
                    filewriter.writerow([i,"D"])

                for i in republican_states:
                    filewriter.writerow([i,"R"])
                
                filewriter.writerow([sum(democrat_electors), sum(republican_electors)])
            print('File outputed as output.csv')

            
    except:
        for _ in range(10000):
            democrat_electors = []
            republican_electors = []
            state_election()
        win_probability()

        # print(democrat_states)
        # print(republican_states)