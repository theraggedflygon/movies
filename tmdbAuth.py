def get_token():
    with open("token.txt") as file:
        token = file.read()

    return token


def get_headers():
    token = get_token()
    return {
        "Authorization": "Bearer {}".format(token),
        'Content-Type': 'application/json;charset=utf-8'
    }