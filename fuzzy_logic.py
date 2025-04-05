import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
chol = ctrl.Antecedent(np.arange(100, 601, 1), 'chol')
trestbps = ctrl.Antecedent(np.arange(80, 201, 1), 'trestbps')
thalach = ctrl.Antecedent(np.arange(60, 221, 1), 'thalach')
oldpeak = ctrl.Antecedent(np.arange(0, 7, 0.1), 'oldpeak')
slope = ctrl.Antecedent(np.arange(0, 3, 1), 'slope')

risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')

# Membership functions
age['young'] = fuzz.trimf(age.universe, [20, 20, 40])
age['middle'] = fuzz.trimf(age.universe, [30, 45, 60])
age['old'] = fuzz.trimf(age.universe, [50, 80, 80])

chol['low'] = fuzz.trimf(chol.universe, [100, 100, 200])
chol['medium'] = fuzz.trimf(chol.universe, [150, 250, 350])
chol['high'] = fuzz.trimf(chol.universe, [300, 600, 600])

trestbps['low'] = fuzz.trimf(trestbps.universe, [80, 80, 120])
trestbps['normal'] = fuzz.trimf(trestbps.universe, [100, 130, 160])
trestbps['high'] = fuzz.trimf(trestbps.universe, [140, 200, 200])

thalach['low'] = fuzz.trimf(thalach.universe, [60, 60, 120])
thalach['normal'] = fuzz.trimf(thalach.universe, [100, 140, 180])
thalach['high'] = fuzz.trimf(thalach.universe, [160, 220, 220])

oldpeak['low'] = fuzz.trimf(oldpeak.universe, [0, 0, 1.5])
oldpeak['medium'] = fuzz.trimf(oldpeak.universe, [1, 2.5, 4])
oldpeak['high'] = fuzz.trimf(oldpeak.universe, [3.5, 6, 6])

slope['up'] = fuzz.trimf(slope.universe, [0, 0, 1])
slope['flat'] = fuzz.trimf(slope.universe, [0, 1, 2])
slope['down'] = fuzz.trimf(slope.universe, [1, 2, 2])

risk['low'] = fuzz.trimf(risk.universe, [0, 0, 40])
risk['medium'] = fuzz.trimf(risk.universe, [30, 50, 70])
risk['high'] = fuzz.trimf(risk.universe, [60, 100, 100])

# Define rules
rules = [
    ctrl.Rule(chol['high'] & trestbps['high'], risk['high']),
    ctrl.Rule(age['old'] & thalach['low'], risk['high']),
    ctrl.Rule(age['young'] & thalach['high'], risk['low']),
    ctrl.Rule(oldpeak['high'] & slope['down'], risk['high']),
    ctrl.Rule(age['middle'] & thalach['normal'], risk['medium']),
]

# Build and simulate system
system = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(system)


# ====== User Input ======
def get_input(prompt, min_val, max_val):
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a number.")


print("\n--- Heart Disease Risk Assessment ---")
sim.input['age'] = get_input("Enter age (20-80): ", 20, 80)
sim.input['chol'] = get_input("Enter cholesterol level (100-600): ", 100, 600)
sim.input['trestbps'] = get_input("Enter blood pressure (80-200): ", 80, 200)
sim.input['thalach'] = get_input("Enter max heart rate (60-220): ", 60, 220)
sim.input['oldpeak'] = get_input("Enter oldpeak (0-6): ", 0, 6)
sim.input['slope'] = get_input("Enter slope (0=up, 1=flat, 2=down): ", 0, 2)

# Compute and show result
sim.compute()
risk_score = sim.output['risk']

print(f"\nYour Heart Disease Risk Score: {risk_score:.2f}")
if risk_score < 40:
    print("=> Risk Level: LOW")
elif risk_score < 70:
    print("=> Risk Level: MEDIUM")
else:
    print("=> Risk Level: HIGH")