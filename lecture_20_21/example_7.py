pow_cache = {}


def pow(x, n):
    key = f"{x}-{n}"
    if key in pow_cache:
        print("Cache hit")
        return pow_cache[key]
    print(f"Calculating {x} ^ {n}")
    result = x ** n
    pow_cache[key] = result
    return result


def main():
    print("Cache:", pow_cache)
    print(pow(2, 4))
    print("Cache:", pow_cache)
    print(pow(2, 4))
    print("Cache:", pow_cache)
    print(pow(2, 4))
    print("Cache:", pow_cache)
    print(pow(2, 10))
    print("Cache:", pow_cache)
    print(pow(2, 10))
    print("Cache:", pow_cache)


if __name__ == "__main__":
    main()
