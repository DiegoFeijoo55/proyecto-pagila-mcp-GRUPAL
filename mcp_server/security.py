import re


class QuerySecurity:
    FORBIDDEN_KEYWORDS = [
        "insert", "update", "delete", "drop", "alter",
        "truncate", "create", "grant", "revoke"
    ]

    @staticmethod
    def validate_query(query: str):
        if not query:
            raise ValueError("La consulta está vacía")

        normalized = query.strip().lower()

        # Solo SELECT
        if not normalized.startswith("select"):
            raise ValueError("Solo se permiten consultas SELECT")

        # Bloquear múltiples sentencias
        if ";" in normalized[:-1]:
            raise ValueError("No se permiten múltiples sentencias")

        # Bloquear palabras peligrosas
        for keyword in QuerySecurity.FORBIDDEN_KEYWORDS:
            pattern = rf"\b{keyword}\b"
            if re.search(pattern, normalized):
                raise ValueError(f"Palabra prohibida detectada: {keyword}")

        # Longitud máxima
        if len(normalized) > 1000:
            raise ValueError("Consulta demasiado larga")

        return True
