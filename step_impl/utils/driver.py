from getgauge.python import before_suite, after_suite
from selenium import webdriver
import requests

class Driver(object):
    driver = None

    @before_suite
    
    def init(self):
        self.username = "YOUR_CBT_USERNAME" #replace with your CBT username
        self.authkey  = "YOUR_CBT_AUTHKEY" #replace with your CBT authkey

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)

        self.test_result = None

        caps = {}
        
        caps['name'] = 'Gauge Test'
        caps['build'] = '1.0'
        caps['browserName'] = 'Chrome'
        caps['version'] = '80x64'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'
        caps['record_video'] = 'true'
        caps['record_network'] = 'false'

        # start the remote browser on our server
        Driver.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )


    @after_suite
    def close():
        Driver.driver.quit()