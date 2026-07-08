"""
personalized-upsell-recommender-skill: Client SDK
Recommends upsell items from a catalog based on category compatibility.
"""
from __future__ import annotations
from typing import Optional


class UpsellRecommenderClient:
    """
    SDK for order value optimization through upselling.
    """

    def recommend(
        self,
        cart_items: list[dict],
        available_catalog: list[dict],
    ) -> dict:
        cart_cats = {item.get("category", "").lower() for item in cart_items}
        recs = []

        for p in available_catalog:
            pid = p.get("id", "")
            cat = p.get("category", "").lower()
            price = float(p.get("price", 0.0))
            
            # Avoid recommending items already in the cart
            if any(item.get("id") == pid for item in cart_items):
                continue
                
            score = 0
            if cat in cart_cats:
                # Complementary logic: same category but higher end, or accessory
                score += 50
            else:
                score += 20
                
            recs.append({
                "product_id": pid,
                "name": p.get("name", "Product"),
                "price": price,
                "recommendation_score": score
            })

        recs.sort(key=lambda x: x["recommendation_score"], reverse=True)

        return {
            "upsell_recommendations": recs[:3]
        }
