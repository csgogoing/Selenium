#coding=utf-8

class Page(object):
	'''

	'''

	jd_url = "https://passport.jd.com/new/"

	def __init__(self, selenium_driver, base_url=jd_url, parent=None):
		self.driver = selenium_driver
		self.base_url = base_url
		self.timeout = 30
		self.parent = parent

	def _open(self, url):
		url = self.base_url + url
		self.driver.get(url)
		assert self.on_page(), 'didnt land on this %s' % url

	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def open(self):
		self._open(self.url)

	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)


	def script(self):
		return self.driver.execute_script(src)
