#!/usr/bin/env python
import csv
from selenium import webdriver
from requests_html import HTMLSession

class CSVReaderWeb():

    csvPath = 'ticketfly_urls.csv'

    def calc_total_urls(self):
        total = 0

        with open(str(self.csvPath)) as csvfile:
            urlReader = csv.reader(csvfile)
            for row in urlReader:
                total = total + 1
        return total

    def compare_url(self,baseurl, current):
        if str(baseurl) == str(current):
            print(baseurl, " is equal to ", current)
        else:
            print(baseurl, " --> DO NOT MATCH with current URL: ", current)

    def csv_iterator_web(self):
        count = 1
        total = self.calc_total_urls()
        with open(self.csvPath) as csvfile:
            urlReader = csv.reader(csvfile)

            for row in urlReader:
                baseUrl = str(row[0])
                expected = str(row[1])
                print("Source and Target URLs are: ", row, " || Site #",count, "of ", total, " sites")
                count = count + 1
                driver = webdriver.Firefox()
                driver.implicitly_wait(10)
                session = HTMLSession()

                ######
                r = session.get(str(baseUrl))

                if r:
                    driver.get(baseUrl)
                else:
                    print("STOPPED BECAUSE ERROR CODE: ", r)
                    print("*" * 100)
                    driver.close()
                    continue
                ######


                current = driver.current_url
                print ("Current URL is: ", current)

                #compare URLs are equal
                self.compare_url(expected,current)
                print("*" * 100)

                #Check that BUY Ticket button is visible
                # try:
                #     buy_button = driver.find_element_by_xpath("//div[@id='root']/div//div[@role='region']//div[@class='eds-structure__main-mask']/div[@class='eds-structure__fixed-bottom-bar-layout-wrapper']/div[@class='eds-fixed-bottom-bar-layout']/div[@class='eds-fixed-bottom-bar-layout__content']/div[@class='eds-structure__main-container']/main[@class='eds-structure__main']//div[@class='eds-l-mar-bot-8']//section[@class='eds-carousel']/div[@class='eds-show-up-sw']/div/div[@class='eds-base-carousel']/div[@class='eds-align--center-vertical eds-align--space-around']/div[@class='eds-align--center-horizontal']//div[@class='featured-events-carousel-info']/div/div[2]//a[contains(text(),'BUY TICKETS')]")
                #     if buy_button.is_displayed():
                #         print("Buy Tickets for " + baseUrl + " is visible")
                #         print("*" * 100)
                #     else:
                #         print("Buy Tickets for " + baseUrl + " is NOT visible")
                #         print("*" * 100)
                # except:
                #     print("NO BUTTON FOUND")
                #     print("*"*100)
                #     driver.close()
                #     continue

                #close window
                driver.close()


reader = CSVReaderWeb()
reader.csv_iterator_web()