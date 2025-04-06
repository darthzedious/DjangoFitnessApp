def calculate_bmr(gender: str, weight: float, height: float, age: int) -> float or None:
    """
    Mifflin-St Jeor equation for calculating the Basal Metabolic Rate (BMR).
    """
    if gender == "Male":
        return 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif gender == "Female":
        return 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    return None


def calculate_amr(bmr: float, activity_level: str) -> float:
    """Calculate the Active Metabolic Rate (AMR) based on activity level."""
    activity_multiplier = {
        "Sedentary": 1.2,
        "Light activity": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very active": 1.9,
    }
    return bmr * activity_multiplier.get(activity_level, 1.2)


def calculate_goal_calories(amr: float, goal_type: str) -> int:
    """Calculate the daily calorie intake based on the goal the user has."""
    goal_adjustments = {
        "Maintain": 0,
        "Mild Loss": -250,
        "Loss": -500,
        "Extreme Loss": -1000,
        "Mild Gain": 250,
        "Gain": 500,
        "Extreme Gain": 1000,
    }
    return int(amr + goal_adjustments.get(goal_type, 0))


def calculate_daily_macros(calories: int, goal_type: str):
    """ Calculate the daily macros based on the goal the user has.
    For example to maintain his weight the macro balance needs to be 45% Carbs, 30% Protein and 25% Fats
    from his daily calories.
    1g Protein has 4 kcal; 1g Carbs has 4 kcal; 1g Fats has 9 kcal;
    """
    macro_ratios = {
        "Maintain": (0.45, 0.30, 0.25),
        "Mild Loss": (0.35, 0.40, 0.25),
        "Loss": (0.35, 0.40, 0.25),
        "Extreme Loss": (0.35, 0.40, 0.25),
        "Mild Gain": (0.50, 0.30, 0.20),
        "Gain": (0.50, 0.30, 0.20),
        "Extreme Gain": (0.50, 0.30, 0.20),
    }

    carbs_ratio, protein_ratio, fats_ratio = macro_ratios.get(goal_type, macro_ratios.get("Maintain", (0.45, 0.30, 0.25)))

    carbs = (calories * carbs_ratio) / 4
    protein = (calories * protein_ratio) / 4
    fats = (calories * fats_ratio) / 9

    return carbs, protein, fats
