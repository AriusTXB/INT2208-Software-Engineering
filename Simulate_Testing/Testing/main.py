import unittest

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_files = [
        "TestUC01", "TestUC02", "TestUC03", "TestUC04", "TestUC05",
        "TestUC06", "TestUC07", "TestUC08", "TestUC09", "TestUC10",
        "TestUC11", "TestUC12", "TestUC13", "TestUC14", "TestUC15", "TestUC16"
    ]

    for test_file in test_files:
        module = __import__(test_file)
        suite.addTests(loader.loadTestsFromModule(module))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()
