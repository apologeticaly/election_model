import random
from states import states

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

    # print(sum(democrat_electors), sum(republican_electors))
    # print(sum(democrat_electors) + sum(republican_electors))
            

for _ in range(1000):
    democrat_electors = []
    republican_electors = []
    state_election()
    

def win_probability ():
    democrat_probability = results.count('D') / 10
    republican_probability = results.count('R') / 10
    tie_probability = results.count('T') / 10

    print('Democrat: ' + str(democrat_probability) + '%')
    print('Republican: ' + str(republican_probability) + '%')
    print('Tie: ' + str(tie_probability) + '%')

win_probability()