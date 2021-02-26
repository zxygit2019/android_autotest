import unittest
case_path = "D:\\tool\\android_auto\\src\\testcase\\testcase"

def all_case():
    dis = unittest.TestLoader()
    discover = dis.discover(start_dir=case_path, pattern="test_MI6.py", top_level_dir=None)
    print(discover)
    return discover