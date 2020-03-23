# Getting Started with Gauge

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, start Selenium Standalone Server (read http://webdriver.io/guide.html) and run
	npm test

## Let's log in
* Go to login form at "http://crossbrowsertesting.github.io/login-form.html"
* Enter username "tester@crossbrowsertesting.com"
* Enter password "test123"
* Click log in button
* Verify that we see logged in message "You are now logged in!"