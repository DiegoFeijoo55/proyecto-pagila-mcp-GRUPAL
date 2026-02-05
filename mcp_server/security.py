FORBIDDEN = ["insert", "update", "delete", "drop", "alter", "create", ";", "--"]

def validate_query(query: str):
    q = query.lower()
    for word in FORBIDDEN:
        if word in q:
            raise ValueError("Consulta no permitida por seguridad")
