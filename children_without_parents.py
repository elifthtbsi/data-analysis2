import csv

count=0

with open('children.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        children_id=line[0]
        parent_id=line[2]

        if parent_id=="[]":
            count+=1

with open("children_without_parents.csv", 'w') as export:
    headers=["number_of_children_wo_parents"]
    writer=csv.DictWriter(export, fieldnames=headers)
    writer.writeheader()

    temp_dict={"number_of_children_wo_parents": count}
    writer.writerow(temp_dict)
