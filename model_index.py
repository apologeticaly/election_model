import random
import numpy
from contests import contests
from terminaltables import AsciiTable, SingleTable
import sys

scores = {}


def model_index():
    for key, value in contests.items():
        democrat = 'D'
        republican = 'R'
        mi_score_d = 0
        mi_score_r = 0
        polling_d = int(value[1])
        polling_r = int(value[2])
        mle_d = float(value[4])
        mle_r = float(value[5])
        favor_d = float(value[6])
        favor_r = float(value[7])
        past_five = value[8]

        if numpy.subtract(polling_d, polling_r) > 10:
            mi_score_d = mi_score_d + 25

        if numpy.subtract(polling_d, polling_r) > 5:
            mi_score_d = mi_score_d + 10
        
        if numpy.subtract(polling_d, polling_r) > 1:
            mi_score_d = mi_score_d + 5
        
        if numpy.subtract(polling_r, polling_d) > 10:
            mi_score_r = mi_score_r+ 25

        if numpy.subtract(polling_r, polling_d) > 5:
            mi_score_r = mi_score_r + 10
        
        if numpy.subtract(polling_r, polling_d) > 1:
            mi_score_r = mi_score_r + 5



        for i in past_five: 
            if i == 'D': 
                mi_score_d = mi_score_d + 5

        for i in past_five: 
            if i == 'R': 
                mi_score_r = mi_score_r + 5



        if mle_d > mle_r:
            mi_score_d = mi_score_d + 15

            if mle_d > 5:
                mi_score_d = mi_score_d + 25

            if mle_d > 10:
                mi_score_d = mi_score_d + 50

        if mle_r > mle_d:
            mi_score_r = mi_score_r + 15

            if mle_d > 5:
                mi_score_r = mi_score_r + 25

            if mle_d > 10:
                mi_score_r = mi_score_r + 50
        


        # if favor_d > favor_r:
        #     mi_score_d = mi_score_d + 10

        # if favor_r > favor_d :
        #     mi_score_r = mi_score_r + 10
    
        scores[key] = [mi_score_d, mi_score_r]
        mi_score_d = 0
        mi_score_r = 0

model_index()

table_data = []
def return_tabulated():
    for key, value in scores.items():
        table_data.append([key, value[0], value[1]])
    
    table_data.insert(0, ['STATE', 'DEMOCRAT', 'REPUBLICAN'])

    table = SingleTable(table_data)
    table.title = 'Model Index Scores'
    table.inner_row_border = True
    table.justify_columns[0] = 'right' 
    table.justify_columns[1] = 'center'
    table.justify_columns[2] = 'center'  

    print (table.table)


if __name__ == '__main__':
    if sys.argv[1] == 'v':
        return_tabulated()
    else:
        print('Use v as sysargv to print table.')