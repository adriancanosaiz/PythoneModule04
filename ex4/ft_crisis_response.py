def access_archive(path: str) -> None:
    print("\nCRISIS ALERT: Attempting access to'" + path + "'" + "...")

    try:
        with open(path, "r") as file:
            content = file.read()
            print("SUCCESS: Archive recovered -``" + content.strip() + "''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    access_archive("../data-generator-tools/lost_archive.txt")
    access_archive("../data-generator-tools/classified_vault.txt")
    access_archive("../data-generator-tools/standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
