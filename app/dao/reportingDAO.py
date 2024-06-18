import psycopg2
from psycopg2 import sql
from config import vars

connection = psycopg2.connect(
    dbname=vars["reportingDb"]["database"],
    user=vars["reportingDb"]["username"],
    password=vars["reportingDb"]["password"],
    host=vars["reportingDb"]["host"],
    port=vars["reportingDb"]["port"]
)

def select_all():
    cursor = connection.cursor()

    cursor.execute("""SELECT * 
                FROM course_completion_events""")

    rows = cursor.fetchall()
    return rows

def get_all_completion_events():
    cursor = connection.cursor()

    cursor.execute("""SELECT 
                event_id, organisation_id, profession_id, grade_id, 
                organisation_abbreviation, profession_name, grade_code 
                FROM course_completion_events""")

    rows = cursor.fetchall()

    row_values = [{
        "eventId": row[0],
        "organisationId": row[1],
        "professionId": row[2],
        "gradeId": row[3],
        "organisation_abbreviation": row[4],
        "profession_name": row[5],
        "grade_code": row[6]
    } for row in rows]

    cursor.close()

    return row_values

def set_row_value_for_event_id(row_name, row_value, event_id):
    cursor = connection.cursor()
    query = sql.SQL(f"UPDATE course_completion_events SET {row_name}=%s WHERE event_id=%s")
    cursor.execute(query, (row_value, event_id))
    connection.commit()
    cursor.close()