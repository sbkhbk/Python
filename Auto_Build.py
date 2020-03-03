from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AutoJenkins:
    def __init__(self, user, password, reposit_build, branch_build, vers_build, send_alerts_to):
        self.user = user
        self.password = password
        capabilities = {
            'browserName': 'chrome',
            'chromeOptions': {
                'useAutomationExtension': False,
                'forceDevToolsScreenshot': True,
                'args': ['--start-maximized', '--disable-infobars']
            }
        }
        self.driver = webdriver.Chrome(
            executable_path="C:\\Development_Avecto\\chromedriver_win32\\chromedriver.exe", desired_capabilities=capabilities)
        self.reposit_build = reposit_build
        self.branch_build = branch_build
        self.vers_build = vers_build
        self.send_alerts_to = send_alerts_to

    def closebrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://jenkins url")
        time.sleep(2)
        usr_txtbox = driver.find_element_by_id("j_username")
        usr_txtbox.send_keys(self.user)

        pass_txtbox = driver.find_element_by_id("j_password")
        pass_txtbox.clear()
        pass_txtbox.send_keys(self.password)

        driver.find_element_by_id("Submit").click()
        time.sleep(2)


sbk_builds = AutoJenkins("username", "password",
                         "reponame", "branchname", "version", "emailid")
sbk_builds.login()
