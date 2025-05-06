import unittest
from module import simulate_favorite_action

class TestUC09FavoriteArticles(unittest.TestCase):
    def test_favorite_article_action(self):
        test_cases = [
            ("TC112", "article001", "user123", "success", False, True, "added", "Article added to favorites"),
            ("TC113", "article001", "user123", "success", True, True, "removed", "Article removed from favorites"),
            ("TC114", "article002", "user123", "system_error", False, False, None, "Unable to save article"),
            ("TC115", "article003", "user123", "success", True, True, "removed", "Article removed from favorites"),  # toggle behavior
            ("TC116", "article004", None, "success", False, False, None, "User must be logged in to favorite articles")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_favorite_action(
                    article_id=case[1],
                    user_id=case[2],
                    simulate=case[3],
                    is_favorited=case[4]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[5])
                if result["success"]:
                    self.assertEqual(result["action"], case[6])
                    self.assertEqual(result["message"], case[7])
                else:
                    self.assertEqual(result["error"], case[7])

if __name__ == "__main__":
    unittest.main(verbosity=2)
