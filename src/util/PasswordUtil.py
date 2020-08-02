from util import EncryptUtil


def get_password(password):
    return password


def get_sha256_salt_password(password, salt="zero"):
    return EncryptUtil.SHA256Util.sha256_salt(salt, password)


if __name__ == '__main__':
    data_str = get_sha256_salt_password("123456")
    print(data_str)
