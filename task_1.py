import json
import argparse

parser = argparse.ArgumentParser(description='reading JSON file and creating binary tree')
parser.add_argument('filename')
args = parser.parse_args()

class Graph:
    def __init__(self, first_name = None , last_name = None, pesel =None):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
    def __str__(self):
        return '{} {} {}'.format(self.first_name,self.last_name,self.pesel)
        

with open(args.filename) as json_file:
    dat_imp = json.load(json_file)
    person = []
    for p in dat_imp['people']:
        person.append(Graph(p['first_name'],(p['last_name']),p['pesel']))
        

node = []
for node in person:
    print(node)
    
