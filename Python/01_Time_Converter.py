def convert_minutes(minutes):
    hrs = minutes // 60
    mins = minutes % 60
    return f"{hrs}hr{'s' if hrs > 1 else ''} {mins}minutes"

print(convert_minutes(int(input("Enter minutes: "))))