
def do_login(username: str, password: str):
    if username != "goden":
        raise ValueError("Username is wrong!")
    if password != "1234":
        raise ValueError("Password is wrong!")

    return "Login successfully!"