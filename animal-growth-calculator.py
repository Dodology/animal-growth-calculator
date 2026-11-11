# Get animal identification and growth data from the user
print("Animal Growth Calculator")
animal_type = input("Enter the type of Animal: ")
initial_weight = float(input("Enter the initial weight of the animal (in kg): "))
final_weight = float(input("Enter the final weight of the animal (in kg): "))
days = int(input("Enter the number of days: "))
feed_intake = float(input("Enter the totalfeed intake (in kg): "))
weight_gain = final_weight - initial_weight
average_daily_gain = weight_gain / days
feed_conversion_ratio = feed_intake / weight_gain
feed_efficiency = average_daily_gain / feed_intake
animal_growth_rate = (weight_gain / initial_weight) * 100
animal_data = {
    "Animal Type": animal_type,
    "Initial Weight (kg)": initial_weight,
    "Final Weight (kg)": final_weight,
    "Days": days,
    "Feed Intake (kg)": feed_intake,
    "Weight Gain (kg)": weight_gain,
    "Average Daily Gain (kg/day)": average_daily_gain,
    "Feed Conversion Ratio": feed_conversion_ratio,
    "Feed Efficiency (kg/kg)": feed_efficiency,
    "Animal Growth Rate (%)": animal_growth_rate
}
#Display the animal record
print("Animal Record:", animal_data)