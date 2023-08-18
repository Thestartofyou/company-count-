import random

# Sample company data with initial LinkedIn follower counts
companies = [
    {"name": "Company A", "followers": 1000},
    {"name": "Company B", "followers": 500},
    {"name": "Company C", "followers": 2000},
]

# Simulate company growth by 10%
for company in companies:
    initial_followers = company["followers"]
    growth_rate = 0.10  # 10% growth
    growth_amount = int(initial_followers * growth_rate)
    new_followers = initial_followers + growth_amount

    print(f"{company['name']} has grown to {new_followers} followers.")

print("Simulation complete.")
