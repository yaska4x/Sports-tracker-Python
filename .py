import csv
from collections import defaultdict
from datetime import date

FILE_NAME = "sports_data.csv"


def add_activity():
    sport = input("Enter sport name: ").title()
    duration = int(input("Enter duration (minutes): "))
    activity_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if activity_date == "":
        activity_date = date.today().isoformat()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sport, duration, activity_date])

    print("Activity added!\n")


def view_activities():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Activities ---")
            for row in reader:
                print(f"Sport: {row[0]}, Time: {row[1]} min, Date: {row[2]}")
            print()
    except FileNotFoundError:
        print("No activities found.\n")


def view_stats():
    totals = defaultdict(int)

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for sport, duration, _ in reader:
                totals[sport] += int(duration)

        print("\n--- Total Time Per Sport ---")
        for sport, total in totals.items():
            print(f"{sport}: {total} minutes")
        print()

    except FileNotFoundError:
        print("No data available.\n")


def main():
    while True:
        print("Sports Tracker")
        print("1. Add activity")
        print("2. View activities")
        print("3. View statistics")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_activity()
        elif choice == "2":
            view_activities()
        elif choice == "3":
            view_stats()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
