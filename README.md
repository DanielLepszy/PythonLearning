# - - Python Learning - - 
***
## Folder structure :
1. **tasks**  - excercises from ***'Python Code Challenges'*** tutorial
2. **UI_test_aut** - user interface test automation ( functional nad layout tests )



### Download dependencies :
    $ pipenv install
<br>

### Run tests from root repo and set report :
 - #### **Functional test :**
        $ pytest -v -s -m"functional"
 - #### **Layout test :**
        $ pytest -v -s -m"layout"
 - #### **Tests based on *' Data Test Driven '* approach :**
        $ pytest -v -s -m"layout"
<br>

### Allure report:
 - #### Choose report location:
         $ --alluredir=test/report
   **Therefore your command should looks like example below:**
   
         $ pytest -v -s -m"functional" --alluredir=test/report
 - #### Open Allure Report:
         $ allure serve test/report