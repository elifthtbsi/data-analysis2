"""
son 1 ayda create edilen çocuk sayısı
"""

import csv
from datetime import datetime, timedelta

today=datetime.today().date()
one_month_ago=today-timedelta(days=30)

school={}
count=0

with open("schools.csv", 'r') as f:
    reader=csv.reader(f)
    for line in reader:
        school_id=line[0]
        date=line[3].split(" ")[0]
        date=date.split("-")

        for i in range(len(date)):
            if i==0:
                year=date[i]
            elif i==1:
                month=date[i]
            elif i==2:
                day=date[i]
                new_date=day+'/'+month+'/'+year
                date_obj=datetime.strptime(new_date, "%d/%m/%Y").date()
                if one_month_ago<date_obj<today:
                    school[school_id]=date_obj

with open('children.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        school_id=line[1]
        if school_id in school:
            count+=1

with open('last_one_month.csv', 'w') as export:
    headers=['number_of_children_created_last_month']
    writer=csv.DictWriter(export, fieldnames=headers)
    writer.writeheader()

    temp_dict={'number_of_children_created_last_month':count}
    writer.writerow(temp_dict)




        


        
