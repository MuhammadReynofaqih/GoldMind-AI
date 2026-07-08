def main():
    print("=" * 40)
    print(" GoldMind AI v2")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("1. Analyze XAUUSD")
        print("2. Trading Journal")
        print("3. Review Trade")
        print("4. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            print("Analyze module (Coming Soon)")
        elif choice == "2":
            print("Journal module (Coming Soon)")
        elif choice == "3":
            print("Review module (Coming Soon)")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()