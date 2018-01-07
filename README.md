# QA_Airbnb_Test
Automatic test example using Selenium + Python based on Airbnb website.

Required to run: Chrome, Python, Selenium, Chrome Webdriver (linked in a code)

Test 1: Save all listed offers after searching -> navigate to Become a host -> Host a home -> Go back -> Go forward -> Go back -> Save the new list of listed items. Compare

Test 2: Save all listed offers after searching -> Refresh webpage -> Save the new list of listed items. Compare

Results are saved into txtfile with a time of a test.

TODO: Firefox version

TODO: Investigate a rare example of a different UI loading resulting in creating another objects that use the same name, class, etc. and can disrupt the code

TODO: Implement another test based on comparing the linked we get from browser address bar directly and the one that's in the code
