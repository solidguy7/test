def validate(data):
    ...

def flat(errors: dict) -> dict:
    out = {}
    def inner(obj, keys="[", value="]["):
        if type(obj) is dict:
            for k in obj:
                inner(obj[k], keys + repr(k) + value)
        elif type(obj) is list:
            for num, item in enumerate(obj):
                inner(item, keys + repr(num) + value)
        else:
            out.update({keys[:-1]: obj})
    inner(errors)
    return out

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
