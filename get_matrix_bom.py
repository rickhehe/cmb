import pandas as pd 
import os 

#This function returns a full filename i.e. with extension csv.
def csvize(filename):
    return filename + '.csv'

#This function returns a data frame.
def expand(c, p):
    df = pd.read_csv(csvize(c))
    df['quantity'] *= float(p[p['child'] == c]['quantity'])
    return df

query = pd.read_csv('query.csv')
for i in query['child']:
    if csvize(i) in os.listdir():
        expand(i, query)

matrix_bom_single = pd.DataFrame(columns = ['child', 'quantity', 'level'])

parent = pd.read_csv(csvize('a0'))
level = 1
parent['level'] = level

while not parent.empty:

    level += 1

    matrix_bom_single =pd.concat([matrix_bom_single, parent], ignore_index = True)
    child = [expand(i, parent) for i in parent['child'] if csvize(i) in os.listdir()]

    if child:
        child = pd.concat(child, ignore_index = True)
        child['level'] = level
        parent = child

    else:
        break
matrix_bom_single['parent'] = 'a0'
print(matrix_bom_single)
