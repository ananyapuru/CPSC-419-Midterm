#!/usr/bin/env python

# -----------------------------------------------------------------------
# database.py
# Author: Bob Dondero, modified by Ananya Purushottam
# -----------------------------------------------------------------------

from sqlite3 import connect
from contextlib import closing
from objects import Object
import random

# -----------------------------------------------------------------------

_DATABASE_URL = 'file:lux.sqlite?mode=ro'

def get_all_ids():

    allobjects = []

    with connect(_DATABASE_URL, uri=True) as connection:

        with closing(connection.cursor()) as cursor:
            
            query_str = 'SELECT objects.id '
            query_str += "FROM objects "
            cursor.execute(query_str, [])

            row = cursor.fetchone()
            while row is not None:
                allobjects.append(str(row[0]))
                row = cursor.fetchone()

    return allobjects

ID = get_all_ids()

def search():

    objects = []

    with connect(_DATABASE_URL, uri=True) as connection:

        with closing(connection.cursor()) as cursor:

            query_str = '''
            SELECT objects.id, objects.label, GROUP_CONCAT(DISTINCT agents.name || ' (' || productions.part || ')')
            AS agent_names, objects.date
            FROM objects INNER JOIN productions on objects.id = productions.obj_id
            INNER JOIN agents on productions.agt_id = agents.id
	        WHERE objects.id = ?
            GROUP BY objects.id
            '''

            valid_id = False

            while not valid_id:
                # Generate a random ID within the range
                # random_id = random.randint(min_id, max_id)
                random_id = random.choice(ID)

                # Check if the random ID exists in the objects table
                cursor.execute(
                    "SELECT id FROM objects WHERE id = ?", (random_id,))
                result = cursor.fetchone()

                # execute query if ID exists
                if result is not None:
                    valid_id = True
                    cursor.execute(query_str, (random_id,))
                    # data = cursor.fetchall()
                    # print(data)

                    # Currently fetches id, label, date: CHANGE THIS
                    row = cursor.fetchone()
                    # print("row", row)
                    while row is not None:
                        obj = Object((row[0]), str(row[1]),
                                     str(row[3]), str(row[2]))
                        objects.append(obj)
                        row = cursor.fetchone()
                else:
                    # search for valid ID
                    continue

    return objects

# print(search())
