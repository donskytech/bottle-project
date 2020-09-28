#!/usr/bin/env python3

"""
    Author: donsky
    For: www.donskytech.com
    Purpose: Create a REST Server Interface using Bottle for future IOT Projects
"""

from bottle import route, run, request, get, response
import sqlite3
import json
from pathlib import Path

#NOTE: CHANGE THIS TO WHERE YOU DOWNLOAD YOUR GIT REPO
db_folder = Path("D:/git/database-project/StudentDB.db")

@get('/student/isauthorized')
def message():

    rf_id_code = request.query.rf_id_code
    print(f"Received the following query parameter rf_id_code :: {rf_id_code}")

    conn = sqlite3.connect(db_folder)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM STUDENTS WHERE RF_ID_CODE=?", (rf_id_code,))
    result = cursor.fetchall()
    cursor.close()

    #Set Response Header to JSON
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'

    if(result):
        message_result = {"is_authorized" : "true"}
    else:
        message_result = {"is_authorized": "false"}
    return json.dumps(message_result)



run(host='localhost', port=8080, debug=True)