"""
example_usage.py -- Demonstrates UpsellRecommenderClient
"""
from client import UpsellRecommenderClient

def main():
    client = UpsellRecommenderClient()
    result = client.recommend(
        cart_items=[{"id": "c1", "name": "Basic Cleanser", "price": 15.0, "category": "beauty"}],
        available_catalog=[
            {"id": "a1", "name": "Premium Moisturizer", "price": 45.0, "category": "beauty"},
            {"id": "a2", "name": "Resistance Band", "price": 12.0, "category": "fitness"}
        ]
    )
    print("[Upsell Recommender Result]")
    for r in result['upsell_recommendations']:
        print(f"Rec: {r['name']} (${r['price']}) - Score: {r['recommendation_score']}")

if __name__ == "__main__":
    main()
