from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Connect to an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Define a 'Student' table
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)


# Create the table in your in-memory database
Base.metadata.create_all(engine)

# Insert some data into the 'Student' table
Session = sessionmaker(bind=engine)
session = Session()

student1 = Student(name='Alice', grade='A')
student2 = Student(name='Bob', grade='B')

session.add_all([student1, student2])
session.commit()

# Query the 'students' table and print each student's name and grade
students = session.query(Student).all()
for student in students:
    print(f'{student.name} is in grade {student.grade}')

# Close the session
session.close()
