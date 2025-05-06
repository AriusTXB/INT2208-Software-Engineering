import unittest
from module import simulate_login

class TestUC02AccountLogin(unittest.TestCase):
    def test_login_cases(self):
        test_cases = [
            ("TC21", "viewer@example.com", "123456", "Login successful", True),
            ("TC22", "viewer@example.com", "wrongpass", "Account locked after multiple failed attempts", False, "lock_account"),
            ("TC23", "viewer@example.com", "123456", "Login successful", True),  # Forgot handled separately
            ("TC24", "viewer@example.com", "123456", "Account not verified", False, "unverified"),
            ("TC25", "viewer@example.com", "123456", "Lỗi hệ thống, vui lòng thử lại", False, "system_error"),
            ("TC26", "", "123456", "Email is required", False),
            ("TC27", "viewer@example.com", "", "Password is required", False),
            ("TC28", "user@@example..com", "123456", "Invalid email format", False),
            ("TC29", "a"*243 + "@example.com", "123456", "Email too long", False),
            ("TC30", "viewer@example.com", "P@ssw0rd#2025", "Login successful", True),
            ("TC31", " viewer@example.com ", "123456", "Login successful", True),
            ("TC32", "VIEWER@EXAMPLE.COM", "123456", "Login successful", True),
            ("TC33", "admin' OR 1=1 --", "123456", "Suspicious input detected", False, "sql_injection"),
            ("TC34", "viewer@example.com", "Reset@2025", "Login successful after password reset", True, "reset_success"),
            ("TC35", "viewer@example.com", "123456", "Login successful", True),  # Session timeout handled elsewhere
            ("TC36", "olduser@example.com", "abc123", "Account is disabled", False, "disabled"),
            ("TC37", "viewer@example.com", "wrongpass", "Too many attempts. CAPTCHA required", False, "force_captcha"),
            ("TC38", "viewer@example.com", "123 456", "Password must not contain spaces", False),
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                simulate = case[5] if len(case) >= 6 else "success"
                result = simulate_login(case[1], case[2], simulate=simulate)
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[4])
                if result["success"]:
                    self.assertIn("message", result)
                else:
                    self.assertEqual(result["error"], case[3])

if __name__ == "__main__":
    unittest.main(verbosity=2)
