from passlib.context import CryptContext


password_context = CryptContext(
    schemes=["bcrypt"]
)

def generate_pass_hash(password: str) -> str:
    """
    hashing password

    Args:
        password (str): password from user

    Returns:
        str: hasshed password
    """
    return password_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    """
    verifing password

    Args:
        password (str): password from user
        hash (str): password hash frrom db

    Returns:
        bool: True or False
    """
    return password_context.verify(password, hash)
