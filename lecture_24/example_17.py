import random
import time

SEARCH_ITERATIONS = 100_000

db_s = set()
db_l = list()


def get_random_identifier():
    return random.randint(1000000, 1000000000000)


def fill_dbs(n):
    for _ in range(n):
        identifier = get_random_identifier()
        if identifier not in db_s:
            db_s.add(identifier)
            db_l.append(identifier)


def my_search(db):
    start = time.time()

    for _ in range(SEARCH_ITERATIONS):
        result = get_random_identifier() in db

    end = time.time()

    return end - start


def main():
    fill_dbs(100_000)
    assert len(db_l) == len(db_s), "Database len mismatch"
    print("Databases filled up")

    # print("Search in list took", my_search(db_l))
    print("Search in set took", my_search(db_s))


if __name__ == "__main__":
    main()
