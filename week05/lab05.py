"""Lab 05: Functions and error handling.

Small helpers for processing lists of user dictionaries while handling
missing and invalid values gracefully.
"""


def _is_numeric(value):
    """Return True if value is an int or float (booleans excluded)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid.

    Users without an "age" key, or whose age is not numeric (for example
    the string "unknown"), are ignored.

    Args:
        users: A list of user dictionaries.

    Returns:
        The average of all valid ages as a float, or 0.0 if there are none.
    """
    ages = [user.get("age") for user in users if _is_numeric(user.get("age"))]
    try:
        return float(sum(ages) / len(ages))
    except ZeroDivisionError:
        return 0.0


def get_active_user_emails(users):
    """Return email addresses belonging to active users.

    A user's email is included only when "is_active" is truthy and the
    "email" key exists.

    Args:
        users: A list of user dictionaries.

    Returns:
        A list of email addresses, or an empty list if none qualify.
    """
    return [
        user["email"]
        for user in users
        if user.get("is_active") and "email" in user
    ]
