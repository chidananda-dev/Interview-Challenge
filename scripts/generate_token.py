from jose import jwt

SECRET_KEY = "supersecret"  # match the one in .env
ALGORITHM = "HS256"

def generate_token(username: str):
    token = jwt.encode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)
    return token

if __name__ == "__main__":
    print("Sample token for user 'test-user':")
    print(generate_token("test-user"))
