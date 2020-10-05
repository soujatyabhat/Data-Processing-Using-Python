import pandas as pd

With open(r'C:\Users\USER\Desktop\Play data with Python\4.1 Python basic data statistics\ml-100k\u.data', 'r') as f:
    data = pd.read_table(f, header=None)
    data.columns = ['user id','item id','rating','timestamp']

 With open(r'C:\Users\USER\Desktop\Play data with Python\4.1 Python basic data statistics\ml-100k\u.user', 'r') as f:
    user = pd.read_table(f, header=None)
    list = []
    for i in range(len(user.values)):
        names = user.values[i][0].split('|')
        list.append(names)
    user = pd.DataFrame(list)
    user.columns =['user id', 'age', 'gender', 'occupation', 'ip code']
    user['user id'] = pd.to_numeric(user['user id'], errors='coerce')

avgrating = pd.pivot_table(data, values='rating', index = 'user id', aggfunc='mean')
new = pd.merge(avgrating, user, how='inner', on = 'user id')
std = pd.pivot_table(new, values='rating', index = 'gender', aggfunc='std')
print(std)
