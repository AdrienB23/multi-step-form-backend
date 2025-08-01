from db.db_mysql import get_connection
from pydantic import BaseModel

class AddOnsItem(BaseModel):
    id: int
    label: str
    description: str
    price_m: int
    price_y: int

def get_all_add_ons():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_add_ons")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    result = list()
    for destination_id, label, description, monthly_price, yearly_price in rows:
        result.append(AddOnsItem(id=destination_id, label=label, description=description, price_m=monthly_price, price_y=yearly_price))

    return result
