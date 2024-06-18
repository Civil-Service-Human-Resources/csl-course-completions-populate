import mysql.connector
import config

connection = mysql.connector.connect(
    host=config.vars["csrsDb"]["host"],
    database=config.vars["csrsDb"]["database"],
    user=config.vars["csrsDb"]["username"],
    password=config.vars["csrsDb"]["password"]
)

def get_all_organisation_ids_and_abbreviations():
    cursor = connection.cursor()
    cursor.execute("SELECT id, abbreviation FROM organisational_unit")

    rows = cursor.fetchall()

    row_values = [{
        "id": row[0],
        "abbreviation": row[1]
    } for row in rows]

    return row_values

def get_all_profession_ids_and_names():
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM profession")

    rows = cursor.fetchall()

    row_values = [{
        "id": row[0],
        "name": row[1]
    } for row in rows]

    return row_values

def get_all_grade_ids_and_code():
    cursor = connection.cursor()
    cursor.execute("SELECT id, code FROM grade")

    rows = cursor.fetchall()

    row_values = [{
        "id": row[0],
        "code": row[1]
    } for row in rows]

    return row_values