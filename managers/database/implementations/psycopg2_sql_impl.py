from typing import List
import psycopg2
from models.property import Property
from managers.database.db_manager import DatabaseManager
from models.landlord import Landlord
from decouple import config


class PsycopgDBManagerImpl(DatabaseManager):
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=config("DB_NAME"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            port=config("DB_PORT"),
        )

    def insert_landlord(self, landlord: Landlord) -> Landlord:
        cur = self.connection.cursor()
        cur.execute(
            """INSERT INTO landlord(
            first_name, last_name, email, phone_number, company_number, company_name, picture)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone_number)s, %(company_number)s, %(company_name)s, %(picture)s) RETURNING id """,
            {
                "first_name": landlord.first_name,
                "last_name": landlord.last_name,
                "email": landlord.email,
                "phone_number": landlord.phone_number,
                "company_number": landlord.company_number,
                "company_name": landlord.company_name,
                "picture": landlord.picture,
            },
        )
        self.connection.commit()
        id = cur.fetchone()[0]
        landlord.id = id
        cur.close()
        return landlord
    

    def add_property(self, property: Property) -> Property:
        cur = self.connection.cursor()
        try:
            if property.host.id:
                host_id = property.host.id
            else:
                cur.execute(
                """INSERT INTO host(name, phone_number, email) VALUES (%(name)s, %(phone_number)s, %(email)s) RETURNING id""",
                {
                    "name": property.host.name,
                    "phone_number": property.host.phone_number,
                    "email": property.host.email,
                },
            )
                host_id = cur.fetchone()[0]
            property.host.id = host_id
            cur.execute(
                """INSERT INTO properties(
                name, country, state, city, address, capacity, unavailable_days, description, price, host_id, landlord_id, property_type_id)
                VALUES (%(name)s, %(country)s, %(state)s, %(city)s, %(address)s, %(capacity)s, %(unavailable_days)s,%(description)s, %(price)s, %(host_id)s, %(landlord_id)s, %(property_type_id)s) RETURNING id""",
                {
                    "name": property.name,
                    "country": property.country,
                    "state": property.state,
                    "city": property.city,
                    "address": property.address,
                    "capacity": property.capacity,
                    "unavailable_days": property.unavailable_days,
                    "description": property.description,
                    "price": property.price,
                    "host_id": host_id,
                    "landlord_id": property.landlord_id,
                    "property_type_id": property.property_type.id,
                },
            )
            property_id = cur.fetchone()[0]
            property.id = property_id

            for fee in property.fees:
                cur.execute(
                    """INSERT INTO fees(name, description, price, property_id) VALUES (%(name)s, %(description)s, %(price)s, %(property_id)s)""",
                    {
                        "name": fee.name,
                        "description": fee.description,
                        "price": fee.price,
                        "property_id": property_id,
                    },
                )
            for distribution in property.distributions:
                cur.execute(
                    """ INSERT INTO property_distributions(property_id, distribution_id, quantity) VALUES (%(property_id)s, %(distribution_id)s,%(quantity)s)""",
                    {
                        "property_id": property_id,
                        "distribution_id": distribution.id,
                        "quantity": distribution.quantity,
                    },
                )
            for feature in property.features:
                cur.execute(
                    """ INSERT INTO properties_has_features(properties_id, features_id) VALUES (%(properties_id)s, %(features_id)s)""",
                    {
                        "properties_id": property_id,
                        "features_id": feature.id,
                    },
                )
            self.connection.commit()
            property.id=property_id
            return property
        except Exception as error:
            print(f"Error: {error}")
            self.connection.rollback()
            raise
        finally:
            cur.close()