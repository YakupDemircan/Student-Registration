from sqlite3 import connect, Connection

'''
Student Table

- Columns:
	- id, 			int, autoincrement, primary key
	- name,     text
	- surname,	text
	- no,				int
	- classId		int foreign key -> Class Table <id>
'''

'''
Class methods

private  -> only being called from class methods
public   -> being called everywhere
'''

'''
	Singleton Pattern:

	If connection is not opened, make connection and return connection
	else return previous connection.
'''
class SqliteConnection:
	def __new__(cls, path) -> Connection:
		if not hasattr(cls, 'connection'):
			print('Is connecting...')
			cls.connection = connect(path)

		return cls.connection


'''
	Student Entity Class
'''
class StudentEntity:
	def __init__(self, name, surname, no, stClass):
		self.name = name
		self.surname = surname
		self.no = no
		self.stClass = stClass

	def fullName(self) -> str:
		return f'{self.name} {self.surname}'

'''
	All Student entity operations are managed by this repository
'''
class StudentRepository:
	def __init__(self, connection: Connection):
		self.conn = connection
		self.cursor = connection.cursor()

	def insert(self, studentData: StudentEntity):
		insertStudent = f'insert into student (name, surname, no, class) values ("{studentData.name}", "{studentData.surname}", {studentData.no}, {studentData.stClass})'

		self.cursor.execute(insertStudent)
		self.conn.commit()

	def delete(self, id: int):
		delete = f"delete from student where id={id}"

		self.cursor.execute(delete)
		self.conn.commit()
		


sconn = SqliteConnection("student_information.db") # new class instance
repo = StudentRepository(sconn)

sObject = StudentEntity('yakup2', 'demircan', 123, 8)

print('inserting', sObject.fullName(), ' ... ')
repo.insert(sObject)


