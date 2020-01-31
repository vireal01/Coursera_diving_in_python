def to_json(filename):
    import json

    def decorator(func):
        def wrapped(*args):
            result = func(*args)
            with open(filename, "w") as f_obj:
                json.dump(result, f_obj)
            return result
        return wrapped
    return decorator


@to_json('numbers.json')
def get_data():
    return {
        'data': 42
    }


get_data()
