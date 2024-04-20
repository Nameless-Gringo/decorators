from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def access_control(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') == ADMIN_USERNAME:
            result = func(*args, **kwargs)
            return result
        else:
            print(UNKNOWN_COMMAND)
    return wrapper


def write_to_file(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('games_result', 'a') as g:
            g.write(result)
        return result
    return wrapper
