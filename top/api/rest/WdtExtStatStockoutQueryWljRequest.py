'''
Created by auto_sdk on 2021.06.24
'''
from top.api.base import RestApi
class WdtExtStatStockoutQueryWljRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.is_exchange = None
		self.page_no = None
		self.page_size = None
		self.shop_no = None
		self.sid = None
		self.start_time = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.stat.stockout.query.wlj'
