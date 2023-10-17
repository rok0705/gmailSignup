import pytest

if __name__ == "__main__":
    # execute All test cases.
    retcode = pytest.main()

    # execute performance related test cases only.
    #retcode = pytest.main(["-k","test_performance.py"])

    # execute functional test cases only.
    #retcode = pytest.main(["-k", "test_functional.py"])
