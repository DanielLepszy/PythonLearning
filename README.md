# - - Python Learning - - 
***
## Folder structure:
1. **tasks**  - excercises from ***'Python Code Challenges'*** tutorial
2. **UI_test_aut** - user interface test automation ( functional nad layout tests )


<br>

### Download dependencies:
    $ pipenv install
### Run tests and set report:
 - #### **Functional test:**
        $ pytest -v -s -m"functional" --alluredir=test/report
 - #### **Layout test:**
        $ pytest -v -s -m"layout" --alluredir=test/report
### Open allure tests report:
    $ allure serve test/report