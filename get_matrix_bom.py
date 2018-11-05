import pandas as pd 
import os 

#This function returns a full filename i.e. with extension csv.
def csvize(filename):
    return filename + '.csv'

#This fouction will print a message for those item cannot be broken down.  In future probaly they need to collected and trigger a todo action.
def not_found(pn):
    print(pn, 'can not be broken down.')


#This function returns a data frame, with the child quantity times parent item quantity.
def expand(c, p):
    df = pd.read_csv(csvize(c))
    df['quantity'] *= float(p[p['child'] == c]['quantity'])
    return df

matrix_bom = pd.DataFrame(columns = ['parent', 'child', 'quantity', 'level'])
query = pd.read_csv('query.csv')

for item in query['child']:

    if csvize(item) in os.listdir():
        parent = expand(item, query)

        matrix_bom_single =pd.DataFrame(columns = ['child', 'quantity', 'level'])
        level = 1
        parent['level'] = level

        while not parent.empty:

            level += 1
    
            matrix_bom_single =pd.concat([matrix_bom_single, parent], ignore_index = True, sort = True)
            child = [expand(i, parent) for i in parent['child'] if csvize(i) in os.listdir()]
        
            if child:
                child = pd.concat(child, ignore_index = True)
                child['level'] = level
                parent = child
        
            else:
                break

        matrix_bom_single['parent'] = item

        matrix_bom = pd.concat([matrix_bom, matrix_bom_single], ignore_index = True, sort = True) 
        
    else:
        not_found(item)

matrix_bom.to_csv('query_matrix_bom.csv', index = None, columns = ['parent', 'child', 'level', 'quantity'])
