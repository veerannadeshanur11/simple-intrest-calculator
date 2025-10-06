# Simple Interest Calculation

# Input from the user
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time (in years): "))

# Calculate Simple Interest
si = (principal * rate * time) / 100

# Display the result
print("Simple Interest =", si)
