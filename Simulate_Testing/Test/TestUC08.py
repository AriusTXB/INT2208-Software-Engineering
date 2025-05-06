import unittest
from module import simulate_comment_action

class TestUC08Commenting(unittest.TestCase):
    def test_commenting_on_articles(self):
        test_cases = [
            ("TC100", "Great article!", "post", "success", True, "active", True, "Comment posted"),
            ("TC101", "This article is trash!", "post", "inappropriate", True, "active", False, "Inappropriate content"),
            ("TC102", "Updated my thoughts here.", "edit", "success", True, "active", True, "Comment updated"),
            ("TC103", "", "post", "success", True, "active", False, "Comment cannot be empty"),
            ("TC104", "Nice!!! 👏👏👏", "post", "success", True, "active", True, "Comment posted"),
            ("TC105", "a"*1001, "post", "success", True, "active", False, "Text too long"),
            ("TC106", "Will read this later", "post", "offline", True, "active", False, "No connection, comment saved locally"),
            ("TC107", "Inappropriate comment content", "report", "success", True, "active", True, "Comment reported successfully"),
            ("TC108", "Trying to comment after logout", "post", "success", False, "active", False, "User must be logged in to comment"),
            ("TC109", "I totally agree!", "post", "duplicate", True, "active", False, "Comment already exists"),
            ("TC110", "I'm suspended but still trying...", "post", "success", True, "suspended", False, "Account is suspended"),
            ("TC111", "This is f***ing dumb", "post", "profanity", True, "active", False, "Inappropriate content")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_comment_action(
                    content=case[1],
                    action=case[2],
                    simulate=case[3],
                    logged_in=case[4],
                    account_status=case[5]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[6])
                if result["success"]:
                    self.assertEqual(result["message"], case[7])
                else:
                    self.assertEqual(result["error"], case[7])

if __name__ == "__main__":
    unittest.main(verbosity=2)
