def write_file(path: str, content: str) -> None:
    file = open(path, "w")
    file.write(content)
    file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename = "new_discovery.txt"

    print("Initializing new storage unit:", filename)
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")

    data = (
        "{[}ENTRY 001{]} New quantum algorithm discovered\n"
        "{[}ENTRY 002{]} Efficiency increased by 347 %\n"
        "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"
    )

    print(data)

    write_file(filename, data)

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive '" + filename + "' ready for long-term preservation.")


if __name__ == "__main__":
    main()
