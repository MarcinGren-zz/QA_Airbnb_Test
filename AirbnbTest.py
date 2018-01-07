#TODO Implement for Firefox
#TODO Compare webpage links from clicking the listing and from scraping using code (based on superhosts), they are different
#TODO Line 119 - UI is sometimes(rarely) different when loading the page, this results in two items having the same attributes (class, etc).
#ex. https://www.airbnb.com/rooms/341763?location=Vienna%2C%20Austria&adults=2&check_in=2018-02-05&check_out=2018-02-08
#ex2 https://www.airbnb.com/rooms/341763?location=Vienna%2C%20Austria&adults=2&check_in=2018-02-05&check_out=2018-02-08&s=2Jq5ceKr
#Why is there a difference?

#Test 1: Save all listed offers after searching -> navigate to Become a host -> Host a home -> Go back -> Go forward -> Go back -> Save the new list of listed items. Compare
#Test 2: Save all listed offers after searching -> Refresh webpage -> Save the new list of listed items. Compare

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import config



opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

class AirbnbTest():

    def testVienna(self):

        def allOffers():
            xpathAllOffers = "//a[@class='_1bxi5o0']"
            numberOfAllOffers = len(driver.find_elements(By.XPATH, xpathAllOffers))
            # TODO class changes between those two, investigate why or omit using class attribute
            if numberOfAllOffers == 0:
                xpathAllOffers = "//a[class='_15ns6vh']"
                numberOfAllOffers = len(driver.find_elements(By.XPATH, xpathAllOffers))
            listOfAllOffers = []
            for offers in list(range(numberOfAllOffers)):
                listing = driver.find_element_by_xpath("(%s//div[@class='_1rths372'])[%s]" % (xpathAllOffers, (offers + 1)))
                listOfAllOffers.append(str(listing.get_attribute("innerText")))

            return listOfAllOffers


        def allSuperhosts(element):
            # find number of superhosts
            numberOfSuperhosts = len(driver.find_elements(By.XPATH, "//span[text()='Superhost']"))
            listOfSuperhosts = []
            listOfSuperhostsLinks = []

            for superhost in list(range(numberOfSuperhosts)):
                xpathSuperhost = "//span[text()='Superhost']//parent::span//parent::div//parent::div//parent::a"
                listing = driver.find_element_by_xpath("(%s)[%s]" % (xpathSuperhost, (superhost + 1)))
                listOfSuperhostsLinks.append(listing.get_attribute("href"))

                listingName = driver.find_element_by_xpath("(%s//div[@class='_1rths372'])[%s]" % (xpathSuperhost, (superhost + 1)))
                listOfSuperhosts.append(str(listingName.get_attribute("innerText")))

            if element == "href":
                return listOfSuperhostsLinks
            elif element == "innerText":
                return  listOfSuperhosts
            else:
                print("incorrect element, use href or innerText")


        def goForwardAndBack(number=1):
            for i in range(number):
                hostButton = driver.find_element_by_xpath("//div[text()='Become a host']//parent::div//parent::button[@class='_hxsurab']")
                hostButton.click()
                hostaHomeButton = driver.find_element_by_xpath("(//li[@role='treeitem']//a)[1]")
                hostaHomeButton.click()
                time.sleep(3)
                driver.back()
                time.sleep(2)
                driver.forward()
                time.sleep(2)
                driver.back()


        def saveAllLists():
            allOffersList = allOffers()
            allSuperhostsList = allSuperhosts("innerText")
            allSuperHostLinksList = allSuperhosts("href")
            return [allOffersList, allSuperhostsList, allSuperHostLinksList]


        def testResult(try1, try2):
            result = ""
            if try1 == try2:
                result = "Test Passed!"
            else:
                result = "Test Failed!"
            return result


        def saveResults(try1, try2, testNumber):
            currentTime = time.gmtime()
            with open("AirbnbTest.txt", "a") as txtfile:
                txtfile.write(
                    "GM Time of the test: " + str(time.strftime('%a, %d %b %Y %H:%M:%S GMT', currentTime)) + "\n")
                if testNumber == 1:
                    txtfile.write(
                        "First test - compare all offers after going to another page (Become a Host Button)" + "\n")
                elif testNumber == 2:
                    txtfile.write("Second test - compare all offers after refreshing a webpage" + "\n")
                txtfile.write("Result: " + str(testResult(try1[0], try2[0]) + "\n"))
                txtfile.write("First List Length: " + str(len(try1[0])) + "\n")
                txtfile.write("Second List Length: " + str(len(try2[0])) + "\n")
                txtfile.write("First List: " + str(try1[0]) + "\n")
                txtfile.write("Second List: " + str(try2[0]) + "\n")
                txtfile.write("\n")


        baseUrl = "https://www.airbnb.com/"
        driverLocation = config.chromeWebdriverLocation
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(executable_path=driverLocation, chrome_options=opts)
        driver.implicitly_wait(10)

        driver.get(baseUrl)
        driver.maximize_window()
        time.sleep(2)

        #TODO UI Changes from time to time when we open the browser, results in another button, named the same. This button is hidden now but it's taking up 1st place.
        searchButton = driver.find_element_by_xpath("//div[@class='_b4huy9n']")
        searchButton.click()
        time.sleep(3)

        #can't use just the id as there're two of those
        textBox = driver.find_element_by_xpath("//div[@class='_1qd1muk']//div[@class='_178faes']/input[@id='GeocompleteController-via-SearchBarV2-SearchBarV2']")
        textBox.send_keys("Vienna, Austria")
        textBox.send_keys(Keys.ENTER)

        #select date, can't use class, 6 buttons are the same, try with child text 'Dates'
        datesButton = driver.find_element_by_xpath("//div[text()='Dates']//parent::button")
        datesButton.click()
        time.sleep(1)

        checkInDate = driver.find_element_by_xpath("//div/div[3]//tr[2]/td[2]/button[@type='button']")
        checkInDate.click()
        checkOutDate = driver.find_element_by_xpath("//div/div[3]//tr[2]/td[5]/button[@type='button']")
        checkOutDate.click()
        applyButton = driver.find_element_by_xpath("//button[@type='button']/span[.='Apply']")
        applyButton.click()
        time.sleep(1)

        #similar to datesButton, classes are the same
        datesButton = driver.find_element_by_xpath("//div[text()='Guests']//parent::button")
        datesButton.click()
        time.sleep(1)

        #check if - adult is disabled, add 1
        minusOneAdult = driver.find_element_by_xpath("//div[@class='_7eamzqx']//button[contains(@aria-controls,'Item-adults')]")
        minusOneAdultStatus = minusOneAdult.is_enabled()
        if minusOneAdultStatus is not True:
            addOneAdult = driver.find_element_by_xpath("//div[@class='_1a72ixey']//button[contains(@aria-controls,'Item-adults')]")
            addOneAdult.click()
            minusOneAdultStatus = minusOneAdult.is_enabled()
            if minusOneAdultStatus is True:
                applyButton = driver.find_element_by_xpath("//button[@type='button']/span[.='Apply']") #have to refresh it
                applyButton.click()
                print("Successfully added one adult and confirmed minus one adult button was disabled at first")
        else:
            applyButton = driver.find_element_by_xpath("//button[@type='button']/span[.='Apply']")  # have to refresh it
            applyButton.click()

        time.sleep(4)
        #check if the listings are the same after opening the first one and pressing back button
        #check if the listings are the same after refreshing a webpage
        firstTry = saveAllLists()
        goForwardAndBack()
        secondTry = saveAllLists()
        saveResults(firstTry, secondTry, 1)

        driver.refresh()
        thirdTry = saveAllLists()
        saveResults(secondTry, thirdTry, 2)

chrome = AirbnbTest()
chrome.testVienna()