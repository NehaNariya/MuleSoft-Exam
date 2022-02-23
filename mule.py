#import the sqlite3 package
import sqlite3



#create a database named details
con = sqlite3.connect("details.db")
print("Database created Sucessfully")

#create a table name Movies
con.execute("create table if not exists Movies(Moviename text,actor text,actress text,director text,yearofrelease int)")
print("Table Created Successfully")

#insert table Movies 
con.execute('''insert into Movies(Moviename , actor, actress, director, yearofrelease) Values(?,?,?,?,?)''',('OM SHANTI OM', 'SHAH RUKH KHAN' , 'DEEPIKA PADUKON' , 'FARAH KHAN' , 2007));
con.commit()
print("Inserted Successfully")

#fetch the data using select query
con.execute("select * from Movies")
records = con.fetchall()
print("Fetching each row using colum name")
for row in records:
    print("Moviename" , row[0])
    print("actor" , row[1])
    print("actress" , row[2])
    print("director" , row[3])
    print("yearofrelease" , row[4])
    print('Moviename','actor','actress','director','yearofrelease')
    
print('fetch the all data successfully')
    
    

