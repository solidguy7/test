def validate(data):
    ...

def flat(errors: dict) -> dict:
    result = {}
    def inner(errors, key=[]):
        if type(errors) is dict:
            for k, v in errors.items():
                inner(v, key + [k])
        elif type(errors) is list:
            for obj in errors:
                inner(obj, key)
        else:
            result.update({'.'.join(key): errors})
    inner(errors)
    return result

# допустим мы уже преобразовали json в python словарь json.loads
errors = {
    "last_name": "Имя должно состоять из букв",
    "birth_place": {
        "address": {
            "parts": [
                {
                    "0": {
                        "id": "Неверный идентификатор",
                    },
                },
                {
                    "1": {
                        "id": "Неверный идентификатор",
                    },
                },
            ],
        },
    },
    "groups": [
        {
            "1": "Группа workers не существует",
        },
    ],
}

flat_errors = flat(errors)
print(flat_errors)
