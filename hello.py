"""DevOps Test"""


def hello(name_string: str):
    """Funcion que saluda al usuario

    Args:
        name_string (str): Nombre del usuario

    Returns:
        string: saying hello
    """
    return f"hello {name_string}"


def sum_func(*args):
    """Funcion que suma los argumentos

    Returns:
        int: retorna un string
    """
    return sum(args)


def print_dict(**kwargs) -> dict:
    """Regresa un dictionario

    Returns:
        dict: _description_
    """
    return kwargs
