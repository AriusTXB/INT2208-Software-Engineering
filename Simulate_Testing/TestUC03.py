import unittest
from module import simulate_account_deletion

class TestUC03AccountDeletion(unittest.TestCase):
    def test_account_deletion(self):
        test_cases = [
            ("TC38", True, True, "success", False, True, "Tài khoản đã được xóa vĩnh viễn"),
            ("TC39", True, False, "success", False, False, "Please confirm deletion"),
            ("TC40", True, True, "system_error", False, False, "Lỗi hệ thống, vui lòng thử lại"),
            ("TC41", False, True, "success", False, False, "Unauthorized"),
            ("TC42", True, False, "success", False, False, "Please confirm deletion"),
            ("TC43", True, True, "success", False, True, "Tài khoản đã được xóa vĩnh viễn"),  # double-click = same result
            ("TC44", True, False, "success", False, False, "Please confirm deletion"),
            ("TC45", True, True, "network_lost", False, False, "Mất kết nối mạng, hãy thử lại"),
            ("TC46", True, True, "success", True, False, "Vui lòng hủy gói đăng ký trước khi xóa tài khoản"),
            ("TC47", True, True, "expired_session", False, False, "Phiên làm việc đã hết hạn")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_account_deletion(
                    logged_in=case[1],
                    confirmation=case[2],
                    simulate=case[3],
                    has_active_subscription=case[4]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[5])
                if result["success"]:
                    self.assertIn("message", result)
                    self.assertEqual(result["message"], case[6])
                else:
                    self.assertEqual(result["error"], case[6])

if __name__ == "__main__":
    unittest.main(verbosity=2)
