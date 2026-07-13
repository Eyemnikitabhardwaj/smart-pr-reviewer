def get_all_users(database):
    query = """
    SELECT *
    FROM users
    ORDER BY id
    """
    return database.execute(query)


def divide_numbers(a, b):
    return a / b


def calculate_total(items):
    total = 0

    for item in items:
        total += item

    return total 