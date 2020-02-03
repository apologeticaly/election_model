import random
import sys

electors = {
    'Alabama': 9,
    'Alaska': 3,
    'Arizona': 11,
    'Arkansas': 6,
    'California': 55,
    'Colorado': 9,
    'Connecticut': 7,
    'District of Columbia': 3,
    'Delaware': 3,
    'Florida': 29,
    'Georgia': 16,
    'Hawaii': 4,
    'Idaho': 4,
    'Illinois': 20,
    'Indiana': 11,
    'Iowa': 6,
    'Kansas': 6,
    'Kentucky': 8,
    'Louisiana': 8,
    'Maine': 4,
    'Maryland': 10,
    'Massachusetts': 11,
    'Michigan': 16,
    'Minnesota': 10,
    'Mississippi': 6,
    'Missouri': 10,
    'Montana': 3,
    'Nebraska': 5,
    'Nevada': 6,
    'New Hampshire': 4,
    'New Jersey': 14,
    'New Mexico': 5,
    'New York': 29,
    'North Carolina': 15,
    'North Dakota': 3,
    'Ohio': 18,
    'Oklahoma': 7,
    'Oregon': 7,
    'Pennsylvania': 20,
    'Rhode Island': 4,
    'South Carolina': 9,
    'South Dakota': 3,
    'Tennessee': 11,
    'Texas': 38,
    'Utah': 6,
    'Vermont': 3,
    'Virginia': 13,
    'Washington': 12,
    'West Virginia': 5,
    'Wisconsin': 10,
    'Wyoming': 3
    }

class State:
    def __init__(self, democrat_polls, republican_polls):
        self.democrat_polls = democrat_polls
        self.republican_polls = republican_polls

        self.democrat_average = 0
        self.republican_average = 0

    def state_averages(self):
        self.democrat_average = (sum(self.democrat_polls) / len(self.democrat_polls))
        self.republican_average = (sum(self.republican_polls) / len(self.republican_polls))

        return self.democrat_average, self.republican_average

    def state_winner(self):
        if self.democrat_average > self.republican_average:
            self.winner = 'Democrat'
        else:
            self.winner = ' Republican'

        return self.winner

alabama = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
alaska = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
arizona = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
arkansas = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
california = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
colorado = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
connecticut = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
district_of_columbia = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
delaware = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
florida = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
georgia = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
hawaii = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
idaho = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
illinois = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
indiana = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
iowa = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
kansas = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
kentucky = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
louisiana = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
maine = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
maryland = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
massachusetts = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
michigan = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
minnesota = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
mississippi = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
missouri = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
montana = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
nebraska = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
nevada = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
new_hampshire = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
new_jersey = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
new_mexico = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
new_york = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
north_carolina = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
north_dakota = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
ohio = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
oklahoma = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
oregon = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
pennsylvania = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
rhode_island = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
south_carolina = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
south_dakota = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
tennessee = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
texas = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
utah = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
vermont = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
virginia = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
washington = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
west_virginia = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
wisconsin = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])
wyoming = State([42, 24, 42, 55, 23], [23, 33, 31, 12, 12])


print(alabama.state_averages())
print(alabama.state_winner())