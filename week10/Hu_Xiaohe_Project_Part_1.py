import os
import csv

class AbstractRecord:
	def __init__(self, name = None):
		self.name = name
	

class StockStatRecord(AbstractRecord):
	def __init__(self, name = None, company_name = None, exchange_country = None,
	price = None, exchange_rate = None, shares_outstanding = None, net_income = None, market_value_usd = None, pre_ratio = None):
		super().__init__(name)
		self.company_name = company_name
		self.exchange_country = exchange_country
		self.price = price
		self.exchange_rate = exchange_rate
		self.shares_outstanding = shares_outstanding
		self.net_income = net_income
		self.market_value_usd = market_value_usd
		self.pre_ratio = pre_ratio
	def __str__(self):
		return "Stock symbol: {}, Company name: {}, Exchange country: {}, Stock Price: {:.2f}, Exchange Rate: {:.2f}, Shares Outstanding:{:.2f}, Net Income:{:.2f}, Market Value in USD: {:.2f}, Price/Earnings Ratio: {:.2f}".format(self.name, self.company_name, self.exchange_country, self.price, self.exchange_rate, self.shares_outstanding, self.net_income, self.market_value_usd, self.pre_ratio)
		
class BaseballStatRecord(AbstractRecord):
	def __init__(self, name, salary, games, avg):
		super().__init__(name)
		self.salary = salary
		self.games = games
		self.avg = avg
	
	def __str__(self):
		return "Player name: {}, Salary: {} Games played:{}, AVG: {:.2f}".format(self.name, self.salary, self.games, self.avg)

class AbstractCSVReader:
	def __init__(self, filePath):
		self.filePath = filePath
		self.recordList = []
		self.titleList = []
	
	def row_to_record(self, row):
		raise NotImplementedError
		
	def load(self):
		# Read the csv file 
		with open(self.filePath, "r") as fileData:
			dataList = fileData.read().splitlines()
		fileData.close()
		#Get all titles of the form
		self.titleList = dataList[0].split(',')
		# Get each row's data and send to row_to_record method
		i = 1
		while i < len(dataList):
			try:
				self.row_to_record(dataList[i])
				i += 1
			except BadData:
				i += 1
				continue
			

class StockCSVReader(AbstractCSVReader):
	def __init__(self, filePath):
		super().__init__(filePath)
		self.nameIndex = 0
		self.company_nameIndex = 0
		self.exchange_countryIndex = 0
		self.priceIndex = 0
		self.exchange_rateIndex = 0
		self.shares_outstandingIndex = 0
		self.net_incomeIndex = 0
		
	def row_to_record(self, row):
		rowList = row.split(",")
		#The order of input data is:
		#1. ticker 2. exchange_country 3. company_name 4. price 5. exchange_rate 6. shares_outstanding 7. net_income
		# Get index for each title
		self.nameIndex = self.titleList.index('ticker')
		self.exchange_countryIndex = self.titleList.index('exchange_country')
		self.company_nameIndex = self.titleList.index('company_name')
		self.priceIndex = self.titleList.index('price')
		self.exchange_rateIndex = self.titleList.index('exchange_rate')
		self.shares_outstandingIndex = self.titleList.index('shares_outstanding')
		self.net_incomeIndex = self.titleList.index('net_income')
		
		#If there's missing data in the row, raise a BadData exception
		for item in rowList:
			if item == '':
				raise(BadData)
		market_value_usd  = float(rowList[self.priceIndex]) * float(rowList[self.exchange_rateIndex]) * float(rowList[self.shares_outstandingIndex])
		#If net_income divide 0 will occur, raise a BadData exception
		if float(rowList[self.net_incomeIndex]) == 0:
			raise(BadData)
		else:
			pe_ratio = float(rowList[self.priceIndex]) * float(rowList[self.shares_outstandingIndex]) / float(rowList[self.net_incomeIndex])
			stockRrecord = StockStatRecord(rowList[self.nameIndex], rowList[self.company_nameIndex], rowList[self.exchange_countryIndex], float(rowList[self.priceIndex]), float(rowList[self.exchange_rateIndex]), float(rowList[self.shares_outstandingIndex]), float(rowList[self.net_incomeIndex]), market_value_usd, pe_ratio)
			self.recordList.append(stockRrecord)		
	
	def load(self):
		super(StockCSVReader, self).load()
		return tuple(self.recordList)

class BaseballCSVReader(AbstractCSVReader):
	def __init__(self, filePath):
		super().__init__(filePath)
		self.nameIndex = 0
		self.salaryIndex = 0
		self.gamesIndex = 0
		self.avgIndex = 0
	
	def row_to_record(self, row):
		rowList = row.split(",")
		#Get index for player name, salary, G and AVG
		self.nameIndex = self.titleList.index('PLAYER')
		self.salaryIndex = self.titleList.index('SALARY')
		self.gamesIndex = self.titleList.index('G')
		self.avgIndex = self.titleList.index('AVG')
		
		#If there's missing data in the row, raise a BadData exception
		for item in rowList:
			if item == '':
				raise(BadData)
		baseballRecord = BaseballStatRecord(rowList[self.nameIndex], rowList[self.salaryIndex
		], rowList[self.gamesIndex], float(rowList[self.avgIndex]))
		self.recordList.append(baseballRecord)
	
	def load(self):
		super(BaseballCSVReader, self).load()
		return tuple(self.recordList)
		
class BadData(Exception):
	
	def __init__(self):
		print("Bad data occur!")
		
if __name__ == "__main__":
	currentPath = os.getcwd()
	# Read stock csv file and print out records
	stockCSVFile = os.path.join(currentPath, "StockValuations.csv")
	stockRecordList = StockCSVReader(stockCSVFile).load()
	for record in stockRecordList:
		print(record)
		
	print("\n")
	
	# Read baseball csv file and print out records
	baseBallCSVFile = os.path.join(currentPath, "MLB2008.csv")
	baseballRecordList = BaseballCSVReader(baseBallCSVFile).load()
	for record in baseballRecordList:
		print(record)

	
		