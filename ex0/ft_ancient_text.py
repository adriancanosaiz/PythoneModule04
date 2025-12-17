def read_file(path: str) -> str:
    file = open(path, "r")
    content = file.read()
    file.close()
    return content


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    path = "../data-generator-tools/ancient_fragment.txt"
    filename = path.split("/")[-1]

    print("Accessing Storage Vault:", filename)

    try:
        content = read_file(path)
    except FileNotFoundError:
        print("Connection not established.\n")
        return

    print("Connection established...")
    print("\nRECOVERED DATA:")

    content = content.replace("[", "{[}").replace("]", "{]}")

    print(content)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
