'''
Created by auto_sdk on 2020.05.28
'''
from top.api.base import RestApi
class WdtApiGoodsStockChangeQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.limit = None
		self.shop_no = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.api.goods.stock.change.query'
