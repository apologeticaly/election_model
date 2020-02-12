import random
from states import states
from terminaltables import AsciiTable, SingleTable
import sys

results = []

democrat_electors = []
republican_electors = []

democrat_states = []
republican_states = []

def state_election():
    for key, value in states.items():

        democratic_average = value[0]
        republican_average = value[1]

        simulation = random.choices(['D', 'R'], [democratic_average, republican_average])
        
        if 'D' in simulation:
            democrat_electors.append(value[2])
            democrat_states.append(key)

        if 'R' in simulation:
            republican_electors.append(value[2])
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
    ['DEMOCRAT', 'REPUBLICAN', 'TIE'],
    [str(democrat_probability) + '%', str(republican_probability) + '%', str(tie_probability) + '%']
    ]
    table = SingleTable(table_data)
    table.title = 'GE Chances [k=10000]'
    table.justify_columns[0] = 'center' 
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'center'  

    print (table.table)

if __name__ == '__main__':
    if sys.argv[1] == 'k':
        for _ in range(10000):
            democrat_electors = []
            republican_electors = []
            state_election()
        win_probability()

    if sys.argv[1] == 's':
        state_election()
        se_table_data = [
        ['DEMOCRAT', 'REPUBLICAN', 'TOTAL'],
        [str(sum(democrat_electors)), str(sum(republican_electors)), str(sum(democrat_electors) + sum(republican_electors))]
        ]
        se_table = SingleTable(se_table_data)
        se_table.title = 'GE Simulation'
        se_table.justify_columns[0] = 'center' 
        se_table.justify_columns[1] = 'center'
        se_table.justify_columns[2] = 'center' 
        print (se_table.table)

        print(democrat_states)
        print(republican_states)