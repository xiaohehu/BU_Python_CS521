import sqlite3
import os
from contextlib import closing
from collections import Counter
from collections import deque

# Abstract class for record
class AbstractRecord:
	def __init__(self, name = None):
		self.name = name
	
# Class of Stocks Stat class
class StockStatRecord(AbstractRecord):
	def __init__(self, company_name = None, name = None, exchange_country = None,
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
		
# Class of Baseball Stat Record
class BaseballStatRecord(AbstractRecord):
	def __init__(self, name, games, avg, salary):
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
			except BadData:
				pass
			finally:
				i += 1	

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
			stockRrecord = StockStatRecord(rowList[self.company_nameIndex], rowList[self.nameIndex], rowList[self.exchange_countryIndex], float(rowList[self.priceIndex]), float(rowList[self.exchange_rateIndex]), float(rowList[self.shares_outstandingIndex]), float(rowList[self.net_incomeIndex]), market_value_usd, pe_ratio)
			self.recordList.append(stockRrecord)		
	
	def load(self):
		super().load()
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
		baseballRecord = BaseballStatRecord(rowList[self.nameIndex], rowList[self.gamesIndex], float(rowList[self.avgIndex]), rowList[self.salaryIndex])
		self.recordList.append(baseballRecord)
	
	def load(self):
		super().load()
		return tuple(self.recordList)

class BadData(Exception):
	
	def __init__(self):
		print("Bad data occur!")
		

class AbstractDAO:
	def __init__(self, db_name = None):
		self.db_name = db_name
	
	def insert_records(self, records):
		raise NotImplementedError
	
	def select_all(self):
		raise NotImplementedError
		
	def connect(self):
		conn = sqlite3.connect(self.db_name)
		return conn
# Create class baseball stats DAO	
class BaseballStatsDAO(AbstractDAO):
	
	def __init__(self, db_name = None):
		super().__init__(db_name)
		
	def insert_records(self, records):
		if not isinstance(records, BaseballStatRecord):
			print("Input record must be an instance of BaseballStatRecord!")
			return
		
		connection = self.connect()
		cur = connection.cursor()
		name = records.name
		number_games_played = records.games
		avg = records.avg
		salary = records.salary
		cur.execute("INSERT INTO baseball_stats VALUES ( ?, ? , ? , ?)", (name, number_games_played, avg, salary))
		connection.commit()
		connection.close()
	
	def select_all(self):
		collection = deque()
		connection = self.connect()
		cur = connection.cursor()
		colleciton = deque()
		cur.execute("SELECT player_name, games_played, average, salary FROM baseball_stats;")
		
		rows = cur.fetchall()
		# Add BaseballStat to the deque
		for row in rows:
			baseball = BaseballStatRecord(row[0], row[1], row[2], row[3])
			collection.append(baseball)
			
		connection.commit()
		connection.close()
		return collection
	
	def connect(self):
			return super().connect()

# Create class StockStatsDAO			
class StockStatsDAO(AbstractDAO):
	
	def __init__(self, db_name = None):
		super().__init__(db_name)
		
	def insert_records(self, records):
		if not isinstance(records, StockStatRecord):
			print("Input record must be an instance of StockStatRecord!")
			return
		
		connection = self.connect()
		cur = connection.cursor()
		company_name = records.company_name
		ticker = records.name
		country = records.exchange_country
		price = records.price
		exchange_rate = records.exchange_rate
		shares_outstanding = records.shares_outstanding
		net_income = records.net_income
		market_value = records.market_value_usd
		pre_ratio = records.pre_ratio
		cur.execute("INSERT INTO stock_stats VALUES ( ?, ? , ? , ?, ?, ?, ?, ?, ?)", (company_name, ticker, country, price, exchange_rate, shares_outstanding, net_income, market_value, pre_ratio))
		connection.commit()
		connection.close()
	
	def select_all(self):
		collection = deque()
		connection = self.connect()
		cur = connection.cursor()
		colleciton = deque()
		cur.execute("SELECT company_name, ticker, country, price, exchange_rate, shares_outstanding, net_income, market_value, pe_ratio FROM stock_stats;")
		
		rows = cur.fetchall()
		# Add each StockStat to deque
		for row in rows:
			stock = StockStatRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
			collection.append(stock)
			
		connection.commit()
		connection.close()
		return collection
	
	def connect(self):
		return super().connect()
		
if __name__ == "__main__":
	currentPath = os.getcwd()
	# Read stock csv file and print out records
	stockCSVFile = os.path.join(currentPath, "StockValuations.csv")
	stockRecordList = StockCSVReader(stockCSVFile).load()

	# Read baseball csv file and print out records
	baseBallCSVFile = os.path.join(currentPath, "MLB2008.csv")
	baseballRecordList = BaseballCSVReader(baseBallCSVFile).load()
	
	stockDBInstance = StockStatsDAO("stocks.db")
	baseballDBInstance = BaseballStatsDAO("baseball.db")
	
	# Add data to database
	for stockRecord in stockRecordList:
		stockDBInstance.insert_records(stockRecord)
		
	for baseballRecord in baseballRecordList:
		baseballDBInstance.insert_records(baseballRecord) 
	
	
	
	stockDeque = stockDBInstance.select_all()
	stockDict = {}
	for stockStat in stockDeque:
		if stockStat.exchange_country in stockDict:
			stockDict[stockStat.exchange_country] += 1
		else:
			stockDict[stockStat.exchange_country] = 1
	print(stockDict)
	
	baseballDeque = baseballDBInstance.select_all()
	baseballDict = {}
	avg_salary = 0
	sum_salary = 0
	for baseballStat in baseballDeque:
		baseballDict[round(baseballStat.avg, 3)] = format(baseballStat.salary, '.2f')
		
	for key in baseballDict:
		sum_salary += float(baseballDict[key])
	print(baseballDict)
	print('\n')
	avg_salary = sum_salary / len(baseballDict)
	print('The average salary is: {:.2f}'.format(avg_salary))			
