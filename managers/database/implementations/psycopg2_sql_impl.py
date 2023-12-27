from typing import List
import psycopg2
from managers.database.db_manager import DatabaseManager
from models.landlord import Landlord
from decouple import config

class PsycopgDBManagerImpl(DatabaseManager):
    def __init__(self): 
        self.connection = psycopg2.connect(
            dbname=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            port=config('DB_PORT')
        )

    def insert_landlord(self, landlord: Landlord) -> Landlord:
        cur = self.connection.cursor()
        cur.execute("""INSERT INTO landlord(
            first_name, last_name, email, phone_number, mobile_number, company_name, picture)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone_number)s, %(mobile_number)s, %(company_name)s, %(picture)s) RETURNING id """,
            {'first_name': landlord.first_name, 'last_name': landlord.last_name, 'email': landlord.email, 'phone_number': landlord.phone_number, 'mobile_number': landlord.mobile_number,
            'company_name': landlord.company_name, 'picture': landlord.picture})
        self.connection.commit()
        id = cur.fetchone()[0]
        landlord.id = id
        cur.close()
        return landlord