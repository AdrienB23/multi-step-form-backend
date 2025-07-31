import json
from typing import Union
from db.db_mysql import get_connection
from pydantic import BaseModel

class TextItem(BaseModel):
    id: str
    content: Union[str, list]

def get_all_texts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT text_id, content FROM t_text")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    result = {}
    for text_id, content in rows:
        try:
            result[text_id] = json.loads(content)
        except json.JSONDecodeError:
            result[text_id] = content

    return result
