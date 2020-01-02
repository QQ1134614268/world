def assert_args(phone, name, id, return_str):
    # TODO
    if phone or name or id:
        assert 1
    pass


if __name__ == '__main__':
    import sys

    phone = []
    assert phone, "123"
    assert ('linux' in sys.platform), "改代码只能在 Linux 下执行"
