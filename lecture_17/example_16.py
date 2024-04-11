def main():
    salary = [
        "54",
        "10$",
        "100.10$",
        100.0,
        "100.0 $",
        " 150.0$ ",

    ]

    step_1 = map(str, salary)

    step_2 = map(lambda s: s.replace(" ", ""), step_1)

    step_3 = map(lambda s: s.replace("$", ""), step_2)

    last_step = map(lambda s: float(s), step_3)

    for s in last_step:
        print(s)


if __name__ == "__main__":
    main()
