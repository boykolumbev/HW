#syzdawane na rechnici

ada = {
        'name':'Ada',
        'age':34,
        'country':'Bulgaria'
}
print(ada)
print(ada.get('town'))


user_data_LOD  = [
    {'name':'Maria' , 'score': 4},
    {'name':'Peter' , 'score': 5},
    {'name':'Ivan' , 'score': 3},
]
print(f"{user_data_LOD[2]['name']} -{user_data_LOD[2]['score']} ")
#d1 = {}   d1=dict()   prazni rechnici



# Dict metodi i operacii

#d = {'age': 34}
#d['name'] = 'Maria'
#update value by
#d['age']=99
#print(d)



#Remove element by key

d={'age':32, 'name': 'Maria'}
age=d.pop('age')
print(d)
print('age')


#Copy dicionarys


user_data={'age':32, 'name': 'Maria'}
#ne e kopie, rechnika ima 2 imena
#user_data_copy={'age':32, 'name': 'Maria'}

user_data_copy = user_data.copy()





