from config.env_default import PUBLIC_KEY
from util import encrypt_util


def get_sha256_salt_password(password, salt=PUBLIC_KEY):
    return encrypt_util.SHA256Util.sha256_salt(password, salt)
