def get_nested_value(obj, key):
    keys = key.split('/')
    for k in keys:
        if isinstance(obj, dict) and k in obj:
            obj = obj[k]
        else:
            return None
    return obj
