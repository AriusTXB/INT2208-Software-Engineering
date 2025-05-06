import unittest
from module import NewsArticle

class TestUC05NewsPosting(unittest.TestCase):
    def test_article_submission(self):
        test_cases = [
            ("TC65", "My First Article", "This is great content", "user1", "success", True, "Pending Approval"),
            ("TC66", "Breaking News", "Some content", "user2", "success", False, "Duplicate article"),
            ("TC67", "Rejected Article", "Not good", "user3", "rejected", False, "Article rejected by admin: Inappropriate content"),
            ("TC68", "My Draft", "Idle content", "user4", "timeout", False, "Inactivity timeout, auto-logout triggered"),
            ("TC69", "", "Some real content", "user5", "success", False, "Title is required"),
            ("TC70", "Real Title", "", "user6", "success", False, "Content is required"),
            ("TC71", "A"*256, "Valid content", "user7", "success", False, "Title too long"),
            ("TC72", "Test HTML", "<script>alert(1)</script>", "user8", "success", False, "Disallowed HTML tags detected"),
            ("TC73", "😊✨ Tiêu đề", "Valid nội dung", "user9", "success", True, "Pending Approval"),
            ("TC74", "New Unique Title", "This is a copied article content", "user10", "success", False, "Duplicate content"),
            ("TC75", "Recovered", "Draft content", "user11", "success", True, "Pending Approval"),  
            ("TC76", "Rich Text", "Copied from Google Docs", "user12", "success", True, "Pending Approval"),
            ("TC77", "Image Upload", "Text + .tiff image", "user13", "unsupported_image", False, "Image format not supported"),
            ("TC78", "Offline Article", "Valid content", "user14", "offline", False, "No connection, article queued for later"),
            ("TC79", "Retry Article", "Updated version", "user15", "success", True, "Pending Approval"),
            ("TC80", "Edited by Admin", "Admin reviewed", "user16", "admin_edit", True, "Article submitted with admin modifications"),
            ("TC81", "Bad Language", "Damn this sucks!", "user17", "profane", False, "Content contains profanity")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                article = NewsArticle(title=case[1], content=case[2], author_id=case[3], simulate=case[4])
                result = article.submit()
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[5])
                if result["success"]:
                    self.assertIn(case[6], result.values())
                else:
                    self.assertEqual(result["error"], case[6])

if __name__ == "__main__":
    unittest.main(verbosity=2)
