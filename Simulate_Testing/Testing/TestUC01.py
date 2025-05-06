import unittest
from module import simulate_registration

class TestUC01AccountRegistration(unittest.TestCase):
    def test_validate_registration_cases(self):
        test_cases = [
            ("TC01", "Bao Tran", "viewer@example.com", "123456", "Viewer", "Đăng ký thành công", True),
            ("TC02", "", "abc@example.com", "abc123", "Viewer", "Tên không được để trống", False),
            ("TC03", "User", "user@@mail..com", "abc123", "Viewer", "Email không hợp lệ", False),
            ("TC04", "User", "abc@example.com", "123", "Viewer", "Mật khẩu quá ngắn", False),
            ("TC05", "User", "abc@example.com", "abc123", "admin123", "Vai trò không hợp lệ", False),
            ("TC06", "User", "abc@example.com", "123456", "Viewer", "Đăng ký thành công", True),
            ("TC07", "User", "abc@example.com", "12345", "Viewer", "Mật khẩu quá ngắn", False),
            ("TC08", "User", "a"*242 + "@example.com", "abc123", "Viewer", "Đăng ký thành công", True),
            ("TC09", "User", "a"*243 + "@example.com", "abc123", "Viewer", "Email quá dài", False),
            ("TC10", "", "user@example.com", "abc123", "Viewer", "Tên không được để trống", False),
            ("TC11", "a"*256, "user@example.com", "abc123", "Viewer", "Tên quá dài", False),
            ("TC12", "Tran@2024!", "user@example.com", "abc123", "Viewer", "Đăng ký thành công", True),
            ("TC13", "  Tran  ", "  viewer@example.com ", "123456", "Viewer", "Đăng ký thành công", True),
            ("TC14", "User", "user@example.com", "P@ss#123", "Viewer", "Đăng ký thành công", True),
            ("TC15", "User", "người.dùng@example.com", "abc123", "Viewer", "Đăng ký thành công", True),
            ("TC16", "User", "Viewer@Example.Com", "abc123", "Viewer", "Đăng ký thành công", True),
            ("TC17", "User", "user..name@example.com", "abc123", "Viewer", "Email không hợp lệ", False),
            ("TC18", "     ", "abc@example.com", "123456", "Viewer", "Tên không được để trống", False),
            ("TC19", "User", "viewer@example.com", "abc123", "Viewer", "Email đã được sử dụng", False, "duplicate"),
            ("TC20", "User", "abc@example.com", "abc123", "Viewer", "Email chưa xác nhận trong 24 giờ", False, "no_confirm")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                simulate = case[7] if len(case) == 8 else "success"
                result = simulate_registration(case[1], case[2], case[3], case[4], simulate=simulate)
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[6])
                if not result["success"]:
                    self.assertEqual(result["error"], case[5])
                else:
                    self.assertIn("user_id", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)


# load từ file excel
#     def setUpClass(cls):
#         workbook = openpyxl.load_workbook('test_cases.xlsx')
#         sheet = workbook.active

#         cls.test_cases = []
#         for row in sheet.iter_rows(min_row=2, values_only=True):
#             cls.test_cases.append(row)

#     def test_validate_registration_cases(self):
#         for case in self.test_cases:
#             with self.subTest(case=case[0]):
#                 simulate = case[7] if len(case) > 7 and case[7] else "success"
#                 result = simulate_registration(case[1], case[2], case[3], case[4], simulate=simulate)
#                 print(f"{case[0]} =>", result)
#                 expected_success = case[6] in ["True", True]
#                 self.assertEqual(result["success"], expected_success)
#                 if not expected_success:
#                     self.assertEqual(result["error"], case[5])
#                 else:
#                     self.assertIn("user_id", result)