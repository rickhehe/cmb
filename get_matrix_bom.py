import pandas as pd 
import os 

def csvize(filename):
    return filename + '.csv'

parent = 'a0'
df_parent = pd.read_csv(csvize(parent))

matrix_bom = pd.DataFrame(columns = ['child', 'quantity', 'level'])

level = 0
while not df_parent.empty:
    matrix_bom = matrix_bom.append(df_parent)
    matrix_bom.level = level
    print(matrix_bom)
    df_child = pd.DataFrame(columns = ['child', 'quantity'])
    
    for i in df_parent.child:
        if csvize(i) in os.listdir(): 
            df = pd.read_csv(csvize(i)) 
            df.quantity *= float(df_parent[df_parent.child == i].quantity)
            df_child = df_child.append(df)
            print(i)
            print(df_child)
            print()
    level += 1
    matrix_bom.append(df_child)
    df_parent = df_child
print(matrix_bom)
