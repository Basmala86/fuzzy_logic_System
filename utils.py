# utils.py

def validate_input(value, min_value, max_value, name):
    try:

        value = float(value)

        if not (min_value <= value <= max_value):
            raise ValueError(f"{name} must be between {min_value} and {max_value}.")

        return value

    except ValueError as e:

        raise ValueError(f"Invalid input for {name}: {e}")


def format_result(risk_level):
    return f"Heart Disease Risk Level: {risk_level}"


# heart_disease_assessment.py

from fuzzy_logic import compute_risk

from utils import validate_input, format_result


def main():
    try:

        age = validate_input(input("Enter age: "), 20, 80, "Age")

        sex = validate_input(input("Enter sex (0 = female, 1 = male): "), 0, 1, "Sex")

        cp = validate_input(input("Enter chest pain type (0-3): "), 0, 3, "Chest Pain")

        trestbps = validate_input(input("Enter resting blood pressure: "), 80, 200, "Blood Pressure")

        chol = validate_input(input("Enter cholesterol level: "), 100, 600, "Cholesterol")

        fbs = validate_input(input("Enter fasting blood sugar (0 = False, 1 = True): "), 0, 1, "Fasting Blood Sugar")

        restecg = validate_input(input("Enter resting ECG results (0-2): "), 0, 2, "Resting ECG")

        thalach = validate_input(input("Enter maximum heart rate achieved: "), 60, 220, "Max Heart Rate")

        exang = validate_input(input("Enter exercise-induced angina (0 = No, 1 = Yes): "), 0, 1, "Angina")

        oldpeak = validate_input(input("Enter oldpeak: "), 0, 6, "Oldpeak")

        slope = validate_input(input("Enter slope (0-2): "), 0, 2, "Slope")

        ca = validate_input(input("Enter number of major vessels (0-3): "), 0, 3, "Vessels")

        thal = validate_input(input("Enter thalassemia type (0-3): "), 0, 3, "Thalassemia")

        risk_level = compute_risk(age, sex, cp, trestbps, chol, fbs, restecg,

                                  thalach, exang, oldpeak, slope, ca, thal)

        print(format_result(risk_level))

    except ValueError as e:

        print(f"Error: {e}")


if __name__ == "__main__":
    main()

