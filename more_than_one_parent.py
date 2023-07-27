import csv

count=0

with open ('children.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        parent_id=line[2]

        if parent_id[-1]!=']':
            count+=1


with open("more_than_one_parents.csv", 'w') as export:
    headers=["number_of_children_w_multiple_parents"]
    writer=csv.DictWriter(export, fieldnames=headers)
    writer.writeheader()

    temp_dict={"number_of_children_w_multiple_parents": count}
    writer.writerow(temp_dict)











