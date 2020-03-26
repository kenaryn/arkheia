"""Define a function specific to information display."""

def get_formatted_name(name):
    """
    Return a 3-letters acronym in upper case and longer names in PascalCase.
    Exemple: 'sql' -> 'SQL'; 'hunting' -> 'Hunting'
    """
    if len(name) == 3:
        neat_title = f"{name.upper()}"
    else:
        neat_title = f"{name.capitalize()}"
    return neat_title