from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course
from sqlalchemy.ext.serializer import loads, dumps

import decimal
from datetime import datetime, timedelta
data = {"amount": 99,
        "end_date": "2021-06-11",
        "title": "Space"}

# if all(item in ["title", "start_date", "end_date", "amount"] for item in data.keys()):
print(all(item in data.keys() for item in ["title", "start_date", "end_date", "amount"]))

{
        "amount": 30,
        "end_date": "2021-05-18T09:20:38.887746",
        "id": 3,
        "start_date": "2021-05-04T09:20:38.888581",
        "title": "Art"
    }