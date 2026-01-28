from mcp_server.server import MCPServer

def print_table(title, rows):
    if not rows:
        print("No hay resultados.\n")
        return

    headers = rows[0].keys()
    col_widths = {
        h: max(len(str(h)), max(len(str(row[h])) for row in rows))
        for h in headers
    }

    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

    header_row = " | ".join(f"{h.upper():<{col_widths[h]}}" for h in headers)
    print(header_row)
    print("-" * len(header_row))

    for row in rows:
        print(" | ".join(f"{str(row[h]):<{col_widths[h]}}" for h in headers))

    print("=" * 70 + "\n")


server = MCPServer()

questions = [
    (
        "¿Cuáles son las películas más alquiladas?",
        """
        SELECT f.title AS pelicula, COUNT(r.rental_id) AS alquileres
        FROM film f
        JOIN inventory i ON f.film_id = i.film_id
        JOIN rental r ON i.inventory_id = r.inventory_id
        GROUP BY f.title
        ORDER BY alquileres DESC
        LIMIT 5;
        """
    ),
    (
        "¿Qué categorías generan más ingresos?",
        """
        SELECT c.name AS categoria, SUM(p.amount) AS ingresos
        FROM category c
        JOIN film_category fc ON c.category_id = fc.category_id
        JOIN inventory i ON fc.film_id = i.film_id
        JOIN rental r ON i.inventory_id = r.inventory_id
        JOIN payment p ON r.rental_id = p.rental_id
        GROUP BY c.name
        ORDER BY ingresos DESC;
        """
    ),
    (
        "¿Quiénes son los clientes más activos?",
        """
        SELECT cu.first_name || ' ' || cu.last_name AS cliente,
               COUNT(r.rental_id) AS alquileres
        FROM customer cu
        JOIN rental r ON cu.customer_id = r.customer_id
        GROUP BY cliente
        ORDER BY alquileres DESC
        LIMIT 5;
        """
    ),
    (
        "¿Qué actores aparecen en más películas?",
        """
        SELECT a.first_name || ' ' || a.last_name AS actor,
               COUNT(fa.film_id) AS peliculas
        FROM actor a
        JOIN film_actor fa ON a.actor_id = fa.actor_id
        GROUP BY actor
        ORDER BY peliculas DESC
        LIMIT 5;
        """
    ),
    (
        "¿Cuáles son las películas más caras para alquilar?",
        """
        SELECT title AS pelicula, rental_rate AS precio
        FROM film
        ORDER BY precio DESC
        LIMIT 5;
        """
    )
]

print("\n" + "#" * 70)
print(" ASISTENTE INTELIGENTE DE CONSULTAS - PAGILA (MCP)")
print("#" * 70)

for question, query in questions:
    print(f"\n🟦 PREGUNTA DEL USUARIO:")
    print(f"➡️  {question}")

    results = server.handle_request("run_safe_query", query=query)
    print_table("Respuesta del sistema", results)

print("😊  Fin de la demostración")
