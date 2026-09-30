# BMI CALCULATOR PROJECT
# Python Essentials

people = []


def calculate_bmi(Weight, Height):
    return Weight / (Height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def healthy_weight_range(Height):
    low = 18.5 * (Height ** 2)
    high = 24.9 * (Height ** 2)
    return low, high


def get_number(message, minimum, maximum):
    while True:
        try:
            value = float(input(message))

            if minimum <= value <= maximum:
                return value

            print("Value must be between", minimum, "and", maximum)

        except ValueError:
            print("Please enter a valid number.")


def add_person():
    print("\n--- Add Person ---")

    name = input("Enter name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter name: ").strip()

    age = get_number("Enter age: ", 1, 120)

    print("\nChoose unit:")
    print("1. Metric (kg, cm)")
    print("2. Imperial (lb, feet/inches)")

    unit = input("Enter choice: ")

    if unit == "1":

        weight = get_number("Enter weight (kg): ", 10, 300)

        height_cm = get_number(
            "Enter height (cm): ", 50, 250
        )

        height = height_cm / 100

    elif unit == "2":

        weight_lb = get_number(
            "Enter weight (lb): ", 22, 660
        )

        feet = get_number(
            "Enter height - feet: ", 1, 8
        )

        inches = get_number(
            "Enter extra inches: ", 0, 11.9
        )

        weight = weight_lb * 0.45359237

        total_inches = feet * 12 + inches
        height = total_inches * 0.0254

    else:
        print("Invalid choice.")
        return

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    low, high = healthy_weight_range(height)

    person = {
        "name": name.title(),
        "age": int(age),
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    }

    people.append(person)

    print("\n------------------------------")
    print("        BMI RESULT")
    print("------------------------------")

    print("Name       :", person["name"])
    print("Age        :", person["age"])
    print("Weight     :", round(weight, 2), "kg")
    print("Height     :", round(height, 2), "m")
    print("BMI        :", round(bmi, 2))
    print("Category   :", category)

    print(
        "Healthy range:",
        round(low, 1),
        "-",
        round(high, 1),
        "kg"
    )

    if bmi < 18.5:
        print("Advice     : You may need to gain some weight.")

    elif bmi < 25:
        print("Advice     : Your BMI is within the normal range.")

    elif bmi < 30:
        print("Advice     : You may need to reduce some weight.")

    else:
        print("Advice     : Consider discussing your health with a professional.")

    print("------------------------------")


def view_records():

    if len(people) == 0:
        print("\nNo records available.")
        return

    print("\n========== ALL RECORDS ==========")

    for i, person in enumerate(people, start=1):

        print(
            i,
            ".",
            person["name"],
            "| Weight:",
            round(person["weight"], 1),
            "kg",
            "| Height:",
            round(person["height"], 2),
            "m",
            "| BMI:",
            round(person["bmi"], 2),
            "|",
            person["category"]
        )


def statistics():

    if len(people) == 0:
        print("\nNo records available.")
        return

    bmi_values = []

    for person in people:
        bmi_values.append(person["bmi"])

    lowest = min(bmi_values)
    highest = max(bmi_values)
    average = sum(bmi_values) / len(bmi_values)

    print("\n========== STATISTICS ==========")

    print("People recorded :", len(people))
    print("Lowest BMI      :", round(lowest, 2))
    print("Highest BMI     :", round(highest, 2))
    print("Average BMI     :", round(average, 2))

    print("\nCategories:")

    categories = {
        "Underweight": [],
        "Normal weight": [],
        "Overweight": [],
        "Obese": []
    }

    for person in people:
        categories[person["category"]].append(
            person["name"]
        )

    for category, names in categories.items():

        if len(names) > 0:
            print(category, ":", ", ".join(names))


def main():

    while True:

        print("\n================================")
        print("       BMI CALCULATOR")
        print("================================")

        print("1. Add Person")
        print("2. View All Records")
        print("3. Statistics")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_person()

        elif choice == "2":
            view_records()

        elif choice == "3":
            statistics()

        elif choice == "4":
            print("\nThank you for using BMI Calculator!")
            break

        else:
            print("\nInvalid choice. Please enter 1-4.")


main()