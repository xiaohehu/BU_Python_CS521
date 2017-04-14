##Requirements:

To extract the raw data (row) into a usable format that can be relied upon by the rest of your application, we will define the concept of a record.

1. Create class: AbstractRecord
	* This class will contain 1 (instance) member: name

2. Create a record class for each of the files you want to load. i.e. BaseballStatRecord and StockStatRecord. And including the following functionality:

	* inherit the AbstractRecord
	* have an initializer method that takes the data you want to load as arguments:
	* For stocks:
		* Stock symbol (ticker)→ this should be stored in the “name” member
		* Company name (company_name)
		* Exchange country (exchange_country)
		* Stock Price (price)
		* Exchange Rate (exchange_rate)
		* Shares Outstanding (shares_outstanding)
		* Net Income (net_income)
		* Market Value in USD (market_value_usd) – This value is calculated in step 4e
		* Price/Earnings Ratio (pe_ratio) – This step is calculated in step 4e
	* For baseball:
		* player name → this should be stored in the “name” member
		* salary
		* G (Games played)
		* AVG (which is the batting average)
		
	* For each record type, override `__str__()` <https://docs.python.org/3/reference/datamodel.html#object.__str__> to return a string of the form: “<name of the record type> ( <value1>, <value2>,  <...> )” using “str.format”.
For floats please only display 2 decimal numbers (2 numbers after the comma)


	To load the data we are going to need a CSV reader. 

3. Create 1 AbstractCSVReader class
	* The class should have an initializer method taking the path to the file to be read
	* The class should have the method: row_to_record(row)
		* Where “row” is a row from the CSV as a dictionary
		* This method should be implemented by simply raising NotImplementedError.
	* The class should have the method: load() that returns a list of records. Load should:
		* Use “with” to open the CSV files
		* read each row from the file into a list
		* call the row_to_record method and send the row as a parameter
		* handle the BadData exception raised by  row_to_record by skipping the record – For more on BadData Exception see step 5
		* If no exception is raised: then the record should be added to the list of records.
		* Once all records are loaded into the list, returns the list.
		
4. Create a CSV reader class for each of the files you want to load
 	*i.e. BaseballCSVReader and StocksCSVReader*
	
	* The class should inherit the AbstractCSVReader
	* Each class should implement its own row_to_record method. The input is a list of unvalidated data, it should validate the data, parse it, create new record and return the record created. (Hint: a tuple if a good structure to use for records)
	* The validation depends on your concrete record:
		* Validation fails for any row that is missing any piece of information
		* Validation fails if the name (symbol or player name) is empty
		* Validation fails if any of the numbers (int or float) cannot be parsed (watch out of the division by zero!!)
	* If validation fails: this method should raise a BadData exception (requirement #5)
	* StocksCSVReader should have two calculations using the extracted records:
		* market_value_usd  = Price * ExchangeRate * SharesOutstanding
		* pe_ratio = Price * SharesOutstanding / NetIncome
5. Create a BadData custom exception to handle record creation errors
6. From your main section ( https://docs.python.org/3/library/__main__.html )
	* load the CSV (e.g.  BaseballCSVReader('path to my CSV').load())
	* Print each record to the console. You are to use: print(record)