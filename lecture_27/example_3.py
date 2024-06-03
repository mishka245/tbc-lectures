class CONFIG:
    DATA_DIR = "/dir/to/data"
    DB_CONNECTION_STRING = "remote server address"


class LOCAL_CONFIG(CONFIG):
    DB_CONNECTION_STRING = "localhost"


def main():
    # print(CONFIG.DATA_DIR)

    print(LOCAL_CONFIG.DB_CONNECTION_STRING)
    print(LOCAL_CONFIG.DATA_DIR)


if __name__ == "__main__":
    main()
