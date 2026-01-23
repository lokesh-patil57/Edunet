# Lambda function to check leap year
is_leap_year = lambda year: (
    (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
)

# Example usage
year = 2024
if is_leap_year(year):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")