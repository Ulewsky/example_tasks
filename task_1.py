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
pesels = []
answer = []
for node in person:
    pesels.append(int(node.pesel))
    answer.append([node.first_name,node.last_name,node.pesel])

print("List of persons in the JSON file: ",answer)#Elements of the file
#Creating binary tree
class Tree:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val
    def insert(self, val):
        if val < self.val:
            if self.l is None:
                self.l = Tree(val)
            else:
                self.l.insert(val)
        elif val > self.val:
            if self.r is None:
                self.r = Tree(val)
            else:
                self.r.insert(val)
            
    def build_tree(self):
        if self.l:
            self.l.build_tree()
        print(self.val)
        if self.r:
            self.r.build_tree()

root =[]
root = Tree(pesels[0])

for i in range(1,len(pesels)):
    root.insert(pesels[i])
#Finding person with exact pesel number    
answer2 = []
z = []
m = 0
root.build_tree()
x = input("Do you want to find someone? ")
if x == 'No':
    print("Ok, thanks ")
elif x =='Yes':
    number = int(input("Write pesel number of that person "))
    for z in person:
        if number == int(z.pesel):
            m = 1
            answer2.append([z.first_name,z.last_name,z.pesel])
            break
    if m == 1:
        print(answer2)
    elif m == 0:
        print('Pesel {} not found'.format(number))
            
else:
    print('Wrong answer, write Yes or No')
