"""
en fazla parent'ı olan çocukları verir
"""

import csv
number_of_parents={}
number_of_lines=0

children=[]

with open('children.csv', 'r') as f:
    reader=csv.reader(f)
    for line in reader:
        number_of_lines+=1
   
with open('children.csv', 'r') as f:
    reader=csv.reader(f)
    rows=list(reader)
    for i in range(number_of_lines):
        number_of_parents[rows[i][0]]=len(rows[i])


max_keys=[key for key, value in number_of_parents.items() if value==max(number_of_parents.values())]

with open('most_parents.csv', 'w') as export:
    header=['children_with_most_parents']
    writer=csv.DictWriter(export, fieldnames=header)
    writer.writeheader()

    for i in range(len(max_keys)):

        temp_dict={'children_with_most_parents':0}
        temp_dict['children_with_most_parents']=max_keys[i]
        writer.writerow(temp_dict)
