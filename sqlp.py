from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from operator import or_


# DEFINE THE ENGINE (CONNECTION OBJECT)

# IT'S FOR DEFAULT DATABASE SQLITE

# sqlalchemy2.0

#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine('sqlite:///foot.db', echo=True)  

# FOR MYSQL USER
#engine = create_engine('mysql+pymysql://root:pass@localhost:4444/foot', echo=True)


# Create session object 
Session = sessionmaker(bind=engine)
session = Session()

base = declarative_base()

class Student(base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# migrate table
base.metadata.create_all(engine)

# create instance of class and insert data
student1=Student(name='Prakash',age=25,grade='A')
student2=Student(name='Rahul',  age=25,grade='B')

# add multiple record
session.add_all([student1,student2])
# commit
session.commit()

# read data 
students= session.query(Student)
for student in students:
    print(student.name,'|',student.age,'|',student.grade)

# order by
#st1=session.query(Student).order_by(Student.name)
#for i in st1:
#   print(i.name)
#st2=session.query(Student).filter(Student.name=='Prakash').first()
#print(st2.name,st2.age)

#st3=session.query(Student).filter(or_(Student.name=='Prakash', Student.name=='Rahul'))
#for j in st3:
#    print(st2.name,st2.age)

# update data 
st4=session.query(Student).filter(Student.name=='prakash').first()
Student.name='Satish'
Student.age=25
Student.grade='C'
session.commit()
print(Student.name,'|',Student.age,'|',Student.grade)



