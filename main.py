from fastapi import FastAPI
import sqlite3

app = FastAPI()


def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/students/gpafrom/{start_gpa}")
def get_by_gpa(start_gpa: float):
    conn = get_db_connection()
    students = conn.execute('SELECT name FROM Students WHERE gpa >= ?', (start_gpa,)).fetchall()
    conn.close()
    
    names = [student['name'] for student in students]
    return {"number": len(names), "names": names}


@app.get("/students/startyear/{year}")
def get_by_year(year: int):
    conn = get_db_connection()
    students = conn.execute('SELECT name FROM Students WHERE start_year = ?', (year,)).fetchall()
    conn.close()
    
    names = [student['name'] for student in students]
    return {"start_year": year, "number": len(names), "names": names}


@app.get("/students/yearrange/")
def get_by_year_range(from_year: int, to_year: int):
    conn = get_db_connection()
    students = conn.execute('SELECT name FROM Students WHERE start_year BETWEEN ? AND ?', (from_year, to_year)).fetchall()
    conn.close()
    
    names = [student['name'] for student in students]
    return {"number": len(names), "names": names}
