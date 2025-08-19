# Function to calculate discount
def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    If the discount is 20% or higher, it applies the discount.
    Otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and get the result
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
