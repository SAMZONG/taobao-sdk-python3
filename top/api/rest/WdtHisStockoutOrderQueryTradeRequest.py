'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtHisStockoutOrderQueryTradeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.shop_no = None
		self.sid = None
		self.src_order_no = None
		self.src_tid = None
		self.start_time = None
		self.status = None
		self.stockout_no = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.his.stockout.order.query.trade'
