# QA_Airbnb_Test
It's an awful one file big script which would need to be refactored

Automatic test example using Selenium + Python based on Airbnb website.

Required to run: Chrome, Python, Selenium, Chrome Webdriver (provide a path in config file)

To get Selenium: pip install Selenium

To get Chrome Webdriver download from: https://sites.google.com/a/chromium.org/chromedriver/downloads

Test 1: Save all listed offers after searching -> navigate to Become a host -> Host a home -> Go back -> Go forward -> Go back -> Save the new list of listed items. Compare. In the saved results we've length of both and whether they're ordered in the same manner.

Test 2: Save all listed offers after searching -> Refresh webpage -> Save the new list of listed items. Compare. In the saved results we've length of both and whether they're ordered in the same manner.

Results are saved into txtfile with a time of a test.

TODO: Firefox version

TODO: Investigate a rare example of a different UI loading resulting in creating another objects that use the same name, class, etc. and can disrupt the code

TODO: Implement another test based on comparing the linked we get from browser address bar directly and the one that's in the code (in progress, list of items is already being saved)

DONE TODO: Implement a check that looks over two lists to see if the items are the same but in a different order or if they're different items
