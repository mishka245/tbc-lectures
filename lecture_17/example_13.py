def main():
    name = [
      "Mikheil",
    "Nino",
        "Ani",
        "Lazare",
        "Demetre",
        "Eka"
    ]
    salary = [
        "54",
        "10$",
        "100.10$",
        100.0,
        "100.0 $",
        " 150.0$ ",

    ]

    salary = list(map(str, salary))
    print(salary)

    salary = list(map(lambda s: s.replace(" ", ""), salary))
    print(salary)

    salary = list(map(lambda s: s.replace("$", ""), salary))
    print(salary)

    salary = list(map(lambda s: float(s), salary))
    print(salary)

    max_salary = max(salary)
    print(max_salary)
    max_salary_index = salary.index(max_salary)
    print(name[max_salary_index])


if __name__ == "__main__":
    main()
