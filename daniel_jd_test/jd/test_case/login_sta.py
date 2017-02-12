#coding=utf-8


from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login


class loginTest(myunit.MyTest):
	'''京东登录页面测试'''

	def user_login_verify(self, username='', password=''):
		login(self.driver).user_login(username, password)


	def test_login1(self):
		'''帐户名和密码为空'''
		self.user_login_verify()
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"请输入账户名和密码")
		function.insert_image(self.driver, 'empty_username&password.jpg')

	def test_login2(self):
		'''仅密码为空'''
		self.user_login_verify(username="daniel_lawliet@qq.com")
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"请输入密码")
		function.insert_image(self.driver, 'empty_password.jpg')

	def test_login3(self):
		'''仅帐户名为空'''
		self.user_login_verify(password="12345677")
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"请输入账户名")
		function.insert_image(self.driver, 'empty_username.jpg')

	def test_login4(self):
		'''帐户名不存在'''
		rakk = random.choice('dasjkfhalfjkshf')
		passk = 'kk' + rakk
		self.user_login_verify(username='daniel_lawliet@qq.com', password=passk)
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"账户名不存在，请重新输入")
		function.insert_image(self.driver, 'No_account.jpg')

	def test_login5(self):
		'''帐户名和密码不匹配'''
		rakk = random.choice('dasjkfhalfjkshf')
		passk = 'kk' + rakk
		self.user_login_verify(username='18701450456', password=passk)
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"账户名与密码不匹配，请重新输入")
		function.insert_image(self.driver, 'Wrong.jpg')

	def test_login6(self):
		'''边界值测试'''
		self.user_login_verify(username=20*'y', password="")
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"账户名不存在，请重新输入")
		function.insert_image(self.driver, 'Wrong.jpg')

	def test_login7(self):
		'''特殊字符测试'''
		self.user_login_verify(username='@#$%^&*()?/', password="")
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"账户名不存在，请重新输入")
		function.insert_image(self.driver, 'Wrong.jpg')

	def test_login8(self):
		'''正确登录'''
		self.user_login_verify(username="daniel_lawliet@qq.com", password="correctpassword")
		po = login(self.driver)
		self.assertEqual(po.user_login_success(), "csgogoing")
		function.insert_image(self.driver, 'True.jpg')

if __name__ == '__main__':
	unittest.main()

