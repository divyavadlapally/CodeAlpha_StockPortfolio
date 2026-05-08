# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400
}

total_investment = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue
    
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Invalid quantity. Enter a number.")
        continue
    
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    
    print(f"Added {stock}: {quantity} shares → ${investment}")

print("\n💰 Total Investment Value: $", total_investment)

# Optional: Save to file
save = input("\nDo you want to save result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment: ${total_investment}")
    print("✅ Saved to portfolio.txt")