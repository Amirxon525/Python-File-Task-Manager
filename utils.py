from hashlib import sha256

def is_valid_username(username: str) -> bool:
    return username.isalpha()



def is_valid_password(password: str) -> bool:
    return len(password) >= 8

def is_same_password(password: str, confirm: str) -> bool:
    return password == confirm





def laod_users() -> list[dict]:
    with open('data/users.txt') as f:
        users = []
        for line in f.readlines():
            username, password = line[:-1].split(', ')
            users.append({
                'username': username,
                'password': password
            })

    return users

def add_user(username: str, password: str):
    with open("data/users.txt", "a") as f:
        f.write(f"{username}, {password}\n")

def make_password(password: str) -> str:
    hashed_password = sha256(password.encode()).hexdigest()
    return hashed_password


def is_username(username: str) -> bool:
    users = laod_users()
    return username in list(map(lambda user: user['username'], users))

def get_user(username: str, password: str) -> dict:
    users = laod_users()
    hashed_password = make_password(password)

    for user in users:
        if user['username'] == username and user['password'] == hashed_password:
            return user
    
   
    return None