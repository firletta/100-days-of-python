# decorators.py
from functools import wraps

def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def make_emphasis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return wrapper

def make_underlined(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper