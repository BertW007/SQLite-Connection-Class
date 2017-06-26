'''
Created on 26 Haz 2017

@author: erdem
'''

from SQLiteConnection.database import SqlClass


myClass = SqlClass()

insert = myClass.Insert("INSERT INTO example(Name,Mail,Password) VALUES (?,?,?)", ('Denziel Washington','denzelwashington@gmail.com','denzel'))
print("Last Insert ID:",insert)
    
getRow = myClass.GetRow("SELECT * FROM example WHERE ID = ?", ('1'))
print(getRow["ID"],"Row Mail:",getRow["Mail"])

getOne = myClass.GetOne("SELECT Count(*) FROM example")
print("Count Row:",getOne)

affectRow = myClass.Exec("UPDATE example SET Name = ? WHERE ID = ?",('Denzel Washington','1'))
print("Affected Row:",affectRow)

getAll = myClass.Get("SELECT * FROM example")
for row in getAll:
    print(row["ID"],". Row:",row["Name"])