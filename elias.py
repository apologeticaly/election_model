import random
import PySimpleGUI as sg
from states import states
from terminaltables import AsciiTable, SingleTable

results = []
democrat_electors = []
republican_electors = []

democrat_states = []
republican_states = []

def state_election():
    for key, value in states.items():

        democratic_average = value[0] / 10
        republican_average = value[1] / 10

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


            

for _ in range(10000):
    democrat_electors = []
    republican_electors = []
    state_election()
    


democrat_probability = results.count('D') / 100
republican_probability = results.count('R') / 100
tie_probability = results.count('T') / 100

table_data = [
    ['DEMOCRAT', 'REPUBLICAN', 'TIE'],
    [str(democrat_probability) + '%', str(republican_probability) + '%', str(tie_probability) + '%']
    ]
table = SingleTable(table_data)
table.title = 'General Election Chances'
table.justify_columns[0] = 'center' 
table.justify_columns[1] = 'center'
table.justify_columns[2] = 'center'  


sg.theme('SystemDefaultForReal')
layout = [  [sg.Text('General Election Chances')],
            [sg.Text('', key='table', size=(37, 5))],
            [sg.Button('          Calculate!          ', key='calc', tooltip='Click here to begin.')] ]
            
window = sg.Window('Election', layout)
while True:
    event, values = window.read()
    if event is None:	# if user closes window
        break
    if event in ('calc'):
        window.Element('table').Update(table.table)

window.close()