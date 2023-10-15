=======================Gmail sign-up QA automated test cases README=======================

**SETUP**
1. Download or pull project into your workspace.
   
3. Open the project in IDE.

5. Run main program. By default, program will execute all existing test cases.
   
Run "python .\main.py"

To run only functional test cases, comment out line#5 and 8 and un-comment line#11.

    #retcode = pytest.main()
    #retcode = pytest.main(["-k","test_performance.py"])
    retcode = pytest.main(["-k", "test_functional.py"])

Run "python .\main.py"

To run only performance test cases, comment out line#5 and #8 and un-comment line#8.

    #retcode = pytest.main()
    retcode = pytest.main(["-k","test_performance.py"])
    #retcode = pytest.main(["-k", "test_functional.py"])

Run "python .\main.py"




**List of test cases**

1. Functional test cases.

```   
def test_createAccount_openURL(): Verify if a web browser can open the initial sign-up page URL.
  assert validate_mainURL() == 0
def test_createAccount_FieldValidation(): Verify if a user can types valid first name and last name in the input boxes and click the next button, the page properly routes to birthday/gender page or not.
  assert createAccount_nameFieldValidation() == 0
def test_createAccount_errorValidation_length(): Verify if a user types longer than supported first name length, the expected error message pops up or not.
  assert createAccount_errorValidation_length() == 0
def test_createAccount_errorValidation_specialChar(): Verify if a user types invalid character in first name field, if server responses with a proper error message to the user or not.
  assert createAccount_errorValidation_specialChar() == 0
def test_createAccount_errorValidation_emptyName(): Verify if a user leaves first name box as empty and click the next button, if server response with a proper error message to the user or not.
  assert createAccount_errorValidation_emptyName() == 0
def test_createAccount_help(): Verify if a user clicks 'help' button from footer, a new tab routes to help page properly or not.
  assert createAccount_help() == 0
def test_createAccount_privacy(): Verify if a user clicks 'privacy' button from footer, a new tab routes to help page properly or not.
  assert createAccount_privacy() == 0
def test_createAccount_language(): Verify if a user changes language from dropdown from footer, page properly refreshes with the expected language form or not.
  assert createAccount_language() == 0
def test_birthdayGender_FieldValidation(): Verify if a user enters an invalid value in day box, if server responses with an expected error message or not.
  assert birthdayGender_FieldValidation() == 0
def test_birthdayGender_Validation(): Verify if a user fills in all birthday and gender boxes with valid values and click next button, if server routes to the next page.
  assert birthdayGender_Validation() == 0
def test_createusername_Validation(): (details are below.)
  assert createusername_Validation() == 0

Case A: Choose your Gmail address
a. if a user chose a valid gmail address and click next button, the page routes to create password page.
b. if a user enters mismatch passwords in passwd boxes, if server prompts a mismatch error message to the user.
c. if a user clicks 'show password' checkmark box, passwords are human readable instead of stars.
d. if a user clicks next button after fill in valid and matching passwords, the page routes to the next page.
Case B: How you'll sign in
a. if a user enters email address and click next button, server routes to the email verify page.
```

2. Performance test cases.
```
def test_is_gmail_backend_down(): if a user is unable to connect to the main sign up page within 10 seconds, consider server is down or hung.
  assert is_gmail_backend_down() == 0
def test_multiple_clients(): if multiple users connect to server concurrently (e.g. 10), if server responses to 'all' concurrent users and tabs. 
  assert multiple_clients_openURL() == 0
```

