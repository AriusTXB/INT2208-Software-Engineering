import unittest
from module import simulate_ai_summary

class TestUC07AINewsSummarization(unittest.TestCase):
    def test_ai_summarization(self):
        test_cases = [
            ("TC92", "This is a well-written article about AI and society." * 5, True, False, "success", True, "This is a summarized version of the article"),
            ("TC93", "Some valid article content", True, False, "overload", False, "Please try again later"),
            ("TC94", "Another article text", True, False, "failure", False, "System error"),
            ("TC95", "Deleted article content", True, True, "success", False, "Article not found"),
            ("TC96", "", True, False, "success", False, "Cannot summarize empty article"),
            ("TC97", "A" * 20001, True, False, "success", True, "Summary generated for long article"),
            ("TC98", "Image Image Video", True, False, "success", False, "Not enough text to summarize"),
            ("TC99", "Useful article content about politics", False, False, "success", False, "Please log in to use summarization")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_ai_summary(
                    article_content=case[1],
                    logged_in=case[2],
                    is_deleted=case[3],
                    simulate=case[4]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[5])
                if result["success"]:
                    self.assertIn(case[6], result["summary"])
                else:
                    self.assertEqual(result["error"], case[6])

if __name__ == "__main__":
    unittest.main(verbosity=2)
