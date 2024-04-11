def main():
    names = [
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

    data = []
    for i in range(len(names)):
        name_and_salary = [names[i], salary[i]]
        data.append(name_and_salary)

    print(data)

    max_salary_guy = max(data, key=lambda l: l[1])
    # max_salary_guy = max(data)
    print(max_salary_guy)


if __name__ == "__main__":
    main()
