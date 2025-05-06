import unittest
from module import simulate_recommendations

class TestUC16ArticleRecommendations(unittest.TestCase):
    def test_TC150_personalized_recommendations(self):
        result = simulate_recommendations(user_id="user1", has_history=True)
        print("TC150 =>", result)
        self.assertTrue(result["success"])
        self.assertIn("AI and You", result["recommendations"])

    def test_TC151_trending_for_new_user(self):
        result = simulate_recommendations(user_id="guest", has_history=False)
        print("TC151 =>", result)
        self.assertTrue(result["success"])
        self.assertIn("Top Trending: Climate", result["recommendations"])

    def test_TC152_recommendation_system_error(self):
        result = simulate_recommendations(simulate="system_error")
        print("TC152 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "Recommendation system error")

    def test_TC153_no_articles_available(self):
        result = simulate_recommendations(has_articles=False)
        print("TC153 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "No recommendations available")

    def test_TC154_multiple_recommendations_on_see_more(self):
        result = simulate_recommendations(user_id="user1", has_history=True, see_more=True)
        print("TC154 =>", result)
        self.assertTrue(result["success"])
        self.assertGreaterEqual(len(result["recommendations"]), 5)
        self.assertIn("More on AI", result["recommendations"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
