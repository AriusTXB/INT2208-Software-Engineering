import unittest
from module import Report

class TestUC15ReportArticles(unittest.TestCase):
    def setUp(self):
        # Reset trạng thái lưu trữ report mỗi khi test
        Report.existing_reports.clear()

    def test_TC145_report_article_success(self):
        result = Report.submit_report("user1", "article1", "Spam")
        print("TC145 =>", result)
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Report submitted successfully")

    def test_TC146_report_system_error(self):
        result = Report.submit_report("user2", "article2", "Hate speech", simulate="system_error")
        print("TC146 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "System error, please try again later")

    def test_TC147_report_without_reason(self):
        result = Report.submit_report("user3", "article3", "")
        print("TC147 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "Please select a reason")

    def test_TC148_report_duplicate_article(self):
        Report.submit_report("user4", "article4", "Fake news")  # First submission
        result = Report.submit_report("user4", "article4", "Duplicate attempt")
        print("TC148 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "Article already reported")

    def test_TC149_report_long_reason(self):
        long_reason = "x" * 501
        result = Report.submit_report("user5", "article5", long_reason)
        print("TC149 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "Reason too long")

if __name__ == "__main__":
    unittest.main(verbosity=2)
