import pandas as pd 
import os 

def csvize(filename):
    return filename + '.csv'

parent = 'a0'
df_parent = pd.read_csv(csvize(parent))

matrix_bom = pd.DataFrame(columns = ['child', 'quantity'])
while not df_parent.empty:
    matrix_bom = matrix_bom.append(df_parent)
    df_child = pd.DataFrame(columns = ['child', 'quantity'])
    
    for i in df_parent.child:
        if i + '.csv' in os.listdir(): 
            df = pd.read_csv(i + '.csv') 
            df.quantity *= float(df_parent[df_parent.child == i].quantity)
            df_child = df_child.append(df)
    matrix_bom = matrix_bom.append(df_child)
    df_parent = df_child
print(matrix_bom)
