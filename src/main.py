from engine.session_engine import get_session
from engine.context_engine import get_context
from engine.macro_engine import get_macro
from engine.market_structure_engine import get_market_structure


def analyze():

    print("\n================ GOLDMIND ANALYSIS ================\n")

    context = get_context()
    session = get_session()
    macro = get_macro()
    structure = get_market_structure()

    print("[ CONTEXT ]")
    for k, v in context.items():
        print(f"{k:<20}: {v}")

    print()

    print("[ SESSION ]")
    for k, v in session.items():
        print(f"{k:<20}: {v}")

    print()

    print("[ MACRO ]")
    for k, v in macro.items():
        print(f"{k:<20}: {v}")

    print()

    print("[ MARKET STRUCTURE ]")
    for k, v in structure.items():
        print(f"{k:<20}: {v}")

    print("\n===================================================\n")


def main():

    while True:

        print("=" * 50)
        print("           GoldMind AI v2")
        print("=" * 50)

        print("1. Analyze XAUUSD")
        print("2. Journal")
        print("3. Review Trade")
        print("4. Exit")

        choice = input("\nSelect : ")

        if choice == "1":
            analyze()

        elif choice == "2":
            print("\nComing Soon\n")

        elif choice == "3":
            print("\nComing Soon\n")

        elif choice == "4":
            break

        else:
            print("Wrong Input")


if __name__ == "__main__":
    main()