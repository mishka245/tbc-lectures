def print_full_name(first_name, last_name, reverse=False):
    print(f"reverse {reverse}")
    if reverse:
        print(f"{last_name} {first_name}")
    else:
        print(f"{first_name} {last_name}")

if __name__ == "__main__":
    print_full_name("John", "Doe")
    print_full_name("John", "Doe", True)
