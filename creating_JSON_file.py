from faker import Faker
import random
import json
Faker.seed(0)
fake = Faker('pl_PL')

data ={}
data['people'] = []
faker = Faker()

for i in range(0,101):
    data['people'].append({
    'first_name':f'{fake.first_name()}',
    'last_name': f'{fake.last_name()}',
    'pesel': f'{fake.pesel()}'
    
})
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
