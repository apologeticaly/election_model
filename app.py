import random
import sys
import threading
from threading import Thread

results = {}

# def probability():
#     if sum(democract_electors) > sum(republican_electors):
#         print('Democrats: ' + str(sum(democract_electors)))
#         print('Republicans: ' + str(sum(republican_electors)))
    
#     if sum(democract_electors) < sum(republican_electors):
#         print('Republicans: ' + str(sum(republican_electors)))
#         print('Democrats: ' + str(sum(democract_electors)))

class State:
    def __init__(self, state, democrat_polls, republican_polls, electors):
        self.state = state
        self.electors = electors
        self.democrat_polls = democrat_polls
        self.republican_polls = republican_polls

        self.democrat_average = 0
        self.republican_average = 0

        self.winner = ''

        self.democract_electors = []
        self.republican_electors = []

        self.runall()

    def state_averages(self):
        self.democrat_average = (sum(self.democrat_polls) / len(self.democrat_polls))
        self.republican_average = (sum(self.republican_polls) / len(self.republican_polls))

        return self.democrat_average, self.republican_average

    def state_election(self):
        self.simulations = random.choices(['D', 'R'], [round(self.democrat_average), round(self.republican_average)], k=10000)

        if self.simulations.count('D') > self.simulations.count('R'):
            self.winner = 'D'

        elif self.simulations.count('R') > self.simulations.count('D'):
            self.winner = 'R'

        else:
            self.winner = 'S'

    # def state_winner(self):
    #     if self.democrat_average == self.republican_average:
    #         self.winner = 'N/A'

    #     elif self.democrat_average > self.republican_average:
    #         self.winner = 'D'
    #         democract_electors.append(self.electors)

    #     else:
    #         self.winner = 'R'
    #         republican_electors.append(self.electors)
                    
        if self.winner == 'D':
            self.democract_electors.append(self.electors)

        if self.winner == 'R':
            self.republican_electors.append(self.electors)
        
        if self.winner == 'S':
            if random.randint(0,1) >= 0.5:
                self.republican_electors.append(self.electors)
            else:
                self.democract_electors.append(self.electors)
            
        results[self.state] = self.winner 

    def runall(self):
        for _ in range(10):
            if __name__ == '__main__':    
                Thread(target = self.state_averages).start()
                Thread(target = self.state_election).start()

            if sum(self.democract_electors) > sum(self.republican_electors):
                print('Democrats: ' + str(sum(self.democract_electors)))
                print('Republicans: ' + str(sum(self.republican_electors)))
            
            if sum(self.democract_electors) < sum(self.republican_electors):
                print('Republicans: ' + str(sum(self.republican_electors)))
                print('Democrats: ' + str(sum(self.democract_electors)))


alabama = State('Alabama', [37, 38], [59, 59], 9)
alaska = State('Alaska', [38], [45], 3)
arizona = State('Arizona', [44], [47], 11)
arkansas = State('Arkansas', [32], [54], 6)
california = State('California', [56], [60], 55)
colorado = State('Colorado', [44], [41], 9)
connecticut = State('Connecticut', [50], [35], 7)
district_of_columbia = State('District of Columbia', [51], [30], 3)
delaware = State('Delaware', [51], [30], 3)
florida = State('Florida', [53], [47], 29)
georgia = State('Georgia', [44], [49], 16)
hawaii = State('Hawaii', [58], [28], 4)
idaho = State('Idaho', [27], [47], 4)
illinois = State('Illinois', [50], [37], 20)
indiana = State('Indiana', [38], [47], 11)
iowa = State('Iowa', [43], [45], 6)
kansas = State('Kansas', [38], [49], 6)
kentucky = State('Kentucky', [35], [55], 8)
louisiana = State('Louisiana', [36], [50], 8)
maine = State('Maine', [47], [40], 4)
maryland = State('Maryland', [63], [27], 10)
massachusetts = State('Massachusetts', [58], [27], 11)
michigan = State('Michigan', [48], [60], 16)
minnesota = State('Minnesota', [50], [41], 10)
mississippi = State('Mississippi', [46], [48], 6)
missouri = State('Missouri', [40], [50], 10)
montana = State('Montana', [32], [45], 3)
nebraska = State('Nebraska', [29], [56], 5)
nevada = State('Nevada', [46], [47], 6)
new_hampshire = State('New Hampshire', [45], [44], 4)
new_jersey = State('New Jersey', [51], [40], 14)
new_mexico = State('New Mexico', [48], [40], 5)
new_york = State('New York', [51], [60], 29)
north_carolina = State('North Carolina', [46], [46], 15)
north_dakota = State('North Dakota', [32], [43], 3)
ohio = State('Ohio', [43], [46], 18)
oklahoma = State('Oklahoma', [30], [60], 7)
oregon = State('Oregon', [45], [36], 7)
pennsylvania = State('Pennsylvania', [48], [44], 20)
rhode_island = State('Rhode Island', [52], [32], 4)
south_carolina = State('South Carolina', [38], [42], 9)
south_dakota = State('South Dakota', [36], [47], 3)
tennessee = State('Tennessee', [36], [48], 11)
texas = State('Texas', [39], [48], 38)
utah = State('Utah', [26], [38], 6)
vermont = State('Vermont', [48], [20], 3)
virginia = State('Virginia', [48], [44], 13)
washington = State('Washington', [50], [36], 12)
west_virginia = State('West Virginia', [28], [60], 5)
wisconsin = State('Wisconsin', [47], [40], 10)
wyoming = State('Wyoming', [20], [58], 3)

