#coding=utf-8


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
	'''
	'''

	url = 'login.aspx'

	#Action
	jd_login_button_loc = (By.LINK_TEXT, "账户登录")

	def jd_login(self):
		sleep(1)
		self.find_element(*self.jd_login_button_loc).click()

	login_username_loc = (By.ID, 'loginname')
	login_password_loc = (By.ID, 'nloginpwd')
	login_button_loc = (By.ID, 'loginsubmit')

	def login_username(self, username):
		self.find_element(*self.login_username_loc).clear()	
		self.find_element(*self.login_username_loc).send_keys(username)

	def login_password(self, password):
		self.find_element(*self.login_password_loc).clear()	
		self.find_element(*self.login_password_loc).send_keys(password)

	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	def user_login(self, username='', password=''):
		self.open()
		self.jd_login()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		sleep(1)

	error_hint_loc = (By.XPATH, "//*[@id='content']/div/div[1]/div/div[3]/div[2]/div[2]")
	user_login_success_loc = (By.XPATH, "//*[@id='ttbar-login']/div[1]/a")

	# 用户名错误提示
	def error_hint(self):
		return self.find_element(*self.error_hint_loc).text

	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text 

