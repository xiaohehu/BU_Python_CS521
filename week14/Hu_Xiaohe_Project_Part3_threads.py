import queue
import threading

stocks_rows = queue.Queue()
stocks_records = queue.Queue()


class BadData(Exception):
	def __init__(self):
		print("Bad data occur!")


class Runnable:
	def __call__(self, *args, **kwargs):
		while True:
			try:
				row = stocks_rows.get(timeout = 1)
			except:
				break
			else:
				print("{worker_id} working hard!!".format(worker_id=id(self)))
				rowList = row.split(",")
				try:
					for item in rowList:
						if item == '':
							raise BadData
				except BadData:
					pass
				else:
					stocks_records.put(row)


class FastStocksCSVReader:
	def __init__(self, file):
		self.file = file

	def load(self):
		with open(self.file, "r") as csvFile:
			csvDic = {}
			rowList = csvFile.read().splitlines()
			#tileList = rowList[0].split(",")
			i = 1
			for row in rowList[1:]:
				csvDic[i] = row
				stocks_rows.put(row)
				i += 1
		csvFile.close()
		threads = []
		for i in range(4):
			new_thread = threading.Thread(target=Runnable())
			new_thread.start()
			threads.append(new_thread)
		for thread in threads:
			thread.join()
		newStockList = []
		while not stocks_records.empty():
			newStockList.append(stocks_records.get())
		return newStockList


if __name__ == "__main__":
	instantList = FastStocksCSVReader("StockValuations.csv").load()
	for item in instantList:
		itemList = item.split(',')
		print("Stock symbol: {}, Exchange country: {}, Company name: {}, Stock Price: {:.2f}, Exchange Rate: {:.2f},Shares Outstanding: {:.2f}, Net Income: {:.2f}".format(itemList[0], itemList[1], itemList[2], float(itemList[3]), float(itemList[4]), float(itemList[5]), float(itemList[6])))