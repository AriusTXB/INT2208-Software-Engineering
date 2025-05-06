import unittest
from module import simulate_subscription_payment

class TestUC04PremiumSubscription(unittest.TestCase):
    def test_subscription_payments(self):
        test_cases = [
            ("TC48", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123 Street"}, "success", False, False, True, "Premium subscription activated"),
            ("TC49", {"card_number": "0000000000000000", "cvv": "000", "exp": "12/25", "billing_address": "123"}, "system_error", False, False, False, "System error, please try again or contact support"),
            ("TC50", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "system_error", False, False, False, "System error, please try again or contact support"),
            ("TC51", {"card_number": "", "cvv": "", "exp": "", "billing_address": ""}, "success", False, False, False, "Card info required"),
            ("TC52", {"card_number": "1234abcd!@#", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "success", False, False, False, "Invalid card number format"),
            ("TC53", {"card_number": "123456", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "success", False, False, False, "Card number too short"),
            ("TC54", {"card_number": "4111111111111111", "cvv": "AB!", "exp": "12/25", "billing_address": "123"}, "success", False, False, False, "Invalid CVV"),
            ("TC55", {"card_number": "4111111111111111", "cvv": "123", "exp": "01/22", "billing_address": "123"}, "success", False, False, False, "Card expired"),
            ("TC56", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "network_lost", False, False, False, "Connection lost, try again"),
            ("TC57", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "success", False, False, True, "Premium subscription activated"),  # double click = same result
            ("TC58", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "success", True, False, False, "Already subscribed"),
            ("TC59", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "cancelled", False, False, False, "Payment was cancelled"),
            ("TC60", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "success", False, True, False, "Trial only once"),
            ("TC61", {"card_number": "378282246310005", "cvv": "1234", "exp": "12/25", "billing_address": "123"}, "unsupported_card", False, False, False, "Card not accepted"),
            ("TC62", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": "123"}, "invalid_currency", False, False, False, "Currency not supported"),
            ("TC63", {"card_number": "", "cvv": "", "exp": "", "billing_address": ""}, "success", False, False, False, "Card info required"),
            ("TC64", {"card_number": "4111111111111111", "cvv": "123", "exp": "12/25", "billing_address": ""}, "success", False, False, False, "Card info required"),
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_subscription_payment(
                    card_info=case[1],
                    simulate=case[2],
                    is_already_premium=case[3],
                    is_trial_user=case[4]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[5])
                if result["success"]:
                    self.assertEqual(result["message"], case[6])
                else:
                    self.assertEqual(result["error"], case[6])

if __name__ == "__main__":
    unittest.main(verbosity=2)
