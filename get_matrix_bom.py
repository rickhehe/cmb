import pandas as pd 
import os 

#This function returns a full filename i.e. with extension csv.
def csvize(filename):
    return filename + '.csv'

#It
def expand(c, p):
    df = pd.read_csv(csvize(c))
    df['quantity'] *= float(p[p['child'] == c]['quantity'])
    return df

matrix_bom = pd.DataFrame(columns = ['child', 'quantity', 'level'])

level = 1
parent = pd.read_csv(csvize('a0'))
parent['level'] = level

while not parent.empty:

    level += 1

    matrix_bom =pd.concat([matrix_bom, parent])
    child = [df(i, parent) for i in parent['child'] if csvize(i) in os.listdir()]

    if child:
        child = pd.concat(child, ignore_index = True)
        child['level'] = level
        parent = child
    else:
        break
