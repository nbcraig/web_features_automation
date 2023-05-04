# web_features_automation
## Test automation of web features found at "https://the-internet.herokuapp.com"
### To run this project locally, follow these steps:
 * Make sure these are installed to your computer:
   * Python
   * Git
 * In your terminal, run:
   > git clone https://github.com/nbcraig/web_features_automation/
 * Open your project folder in the terminal make sure you activate the virtual environment(optional) and run:
   > pip install -r requirements.txt
 * Finally, run this command:
   > pytest
  
### Features:
  * Tests are wrote in Python with the Selenium and Pytest libraries
  * A HTML report with is made each time tests are ran
  * Covered tests cases:
    * Valid login and logout
    * Add/Remove succesfully elements from a page(state modification)
    * Context menu
