from util import EncryptUtil


def get_password(password):
    return password


def get_sha256_salt_password(password, salt="zero"):
    return EncryptUtil.SHA256Util.sha256_salt(password, salt)


if __name__ == '__main__':
    data_str = get_sha256_salt_password("abc32554")
    print(data_str)
