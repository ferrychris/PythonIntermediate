Database is
Rules
1 table Should store 1 type of information - Student(1 table), Payment ( 1 table) 2. Avoid duplicate Data 3. Always have a primary Key

Python Database Workflow

1. Import library - (sqlite3)
2. Connect to Database - conn = sqlite3.connect("database.db")
3. Create cursor - cursor = conn.cursor()
4. Create tables
5. Perform CRUD operations (Create, Read, Update, Delete)
6. Commit changes - conn.commit()
7. Close connection - conn.close()
