# personalized-upsell-recommender-skill

> **GenPark AI Agent Skill** -- Shopping cart upsell recommender.

## Quick Start

```python
from client import UpsellRecommenderClient
client = UpsellRecommenderClient()
res = client.recommend([{"id": "1", "category": "beauty"}], [{"id": "2", "category": "beauty", "price": 50}])
print(res["upsell_recommendations"])
```
