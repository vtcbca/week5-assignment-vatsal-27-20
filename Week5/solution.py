#python program create csv file student.csv(sid,sname,city,contact)
import csv
field=['Sid','Sname','City','Contact']
rows=[[101,'OM','Surat',9877566745],
      [102,'Sai','Vyara',9874568765],
      [103,'Ram','Bardoli',6756453456],
      [104,'Krishna','Bardoli',7867564534],
      [105,'Sita','Vyara',7867564567]]
filename="c:\\sqlite3\\csv\\student.csv"
#insert record through user input
l=[]
for i in range(5):
    no=int(input("Enter id:"))
    name=input("Enter name:")
    city=input("Enter city:")
    contact=int(input("Enter contact number:"))
    t=(no,name,city,contact)
    l.append(t)
with open(filename,'w',newline='')as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)
    csvwriter.writerows(l)
# Reading dat from csv file.
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for record in csvreader:
        print(record)
print("Total no.of rows:%d"%(csvreader.line_num))
