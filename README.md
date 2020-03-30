# Getting Started with Selenium Gauge and Python

This is an example for getting started with Gauge, Selenium, and CrossBrowserTesting's hub. 

<br>

## Install Gauge

For this example, we used brew to install Gauge on macOS:

`brew install gauge`

<br>

## Download Template Gauge Project

In this example, we started with a project template provided by Gauge:

`gauge init python_selenium`

You can also clone this repository to use this template.

These are the changes we made to the gauge python_selenium template:

<br>

## Change driver.py to point to CBT Hub

In step_impl -> utils, you will find a driver.py file. In order to connect to CrossBrowserTesting, you will need to point to our hub.

This is also where you should enter your CBT credentials along with the capabilities for the device/browser configuration you want to test.

You can generate the desired capabilities for your test using our capabilities configurator: https://app.crossbrowsertesting.com/selenium/run

```
from getgauge.python import before_suite, after_suite
from selenium import webdriver

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

```
<br>

## Add your Test Spec and Step Implementations

We are adding the following step implementations to specs -> example.spec:

```
# Getting Started with Gauge

## Let's log in
* Go to login form at "http://crossbrowsertesting.github.io/login-form.html"
* Enter username "tester@crossbrowsertesting.com"
* Enter password "test123"
* Click log in button
* Verify that we see logged in message "You are now logged in!"
```

So that our test knows how to run those steps, we will also need to add the step implementations for this test under step_impl -> get_started.py

```
from getgauge.python import step
from step_impl.utils.driver import Driver

@step("Go to login form at <url>")
def go_to_login_form_at(arg1):
  Driver.driver.get(arg1)


@step("Enter username <arg1>")
def enter_username(arg1):
  Driver.driver.find_element_by_name('username').send_keys(arg1)

@step("Enter password <arg1>")
def enter_password(arg1):
  Driver.driver.find_element_by_name('password').send_keys(arg1)

@step("Click log in button")
def click_log_in_button():
  Driver.driver.find_element_by_css_selector('body > div > div > div > div > form > div.form-actions > button').click()
  Driver.driver.implicitly_wait(20)


@step("Verify that we see logged in message <arg1>")
def verify_that_we_see_logged_in_message(arg1):
    assert Driver.driver.find_element_by_id('logged-in').text == arg1
```
<br>

## Run Your Test

Now you can run your Selenium Gauge Python test on CrossBrowserTesting:

`gauge run specs`