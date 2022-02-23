#import the sqlite3 package
import sqlite3

try:
    # create a database named favmovies
    con=sqlite3.connect("favmovies.db")
    
    # create a table name Movies
    con.execute("create table if not exists Movies (movie_nm text,leadactor text,actress text, year integer, director_nm text)")

    print("Table Created Successfully...")

except:
    print("Error in Database Creation...")


moviename=input("Enter Movie Name:")
leadactorname=input("Enter Lead Actor Name:")
actressname=input("Enter Actress Name:")
year=input("Enter Releas Year:")
directorname=input("Enter Director Name:")

# Data insert Query

con.execute("insert into Movies values(?,?,?,?,?)",(moviename,leadactorname,actressname,year,directorname))

# Data Fetch Query
result= con.execute("select * from Movies")
for i in result:
    print(i)