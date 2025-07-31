from db.db_mysql import get_connection
from pydantic import BaseModel

class PlanItem(BaseModel):
    id: int
    name: str
    price_m: int
    price_y: int

def get_all_plans():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM t_plan")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    result = list()
    for destination_id, name, monthly_price, yearly_price in rows:
        result.append(PlanItem(id=destination_id, name=name, price_m=monthly_price, price_y=yearly_price))

    return result
