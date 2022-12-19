import util.file_util


class AppConfig:
    pass


if __name__ == '__main__':
    print(util.file_util.FileUtil.from_yaml("yaml_env_default.yaml"))
