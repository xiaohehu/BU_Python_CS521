import sqlite3

baseball_conn = sqlite3.connect('baseball.db')
c = baseball_conn.cursor()

# Create table
c.execute('''CREATE TABLE baseball_stats
             (player_name text, games_played int, average real, salary real)''')

# Save (commit) the changes
baseball_conn.commit()

baseball_conn.close()

stock_conn = sqlite3.connect('stocks.db')
c = stock_conn.cursor()

# Create table
c.execute('''CREATE TABLE stock_stats
             (company_name text, ticker text, country text, price real, exchange_rate real, shares_outstanding real, net_income real, market_value real, pe_ratio real)''')

# Save (commit) the changes
stock_conn.commit()

stock_conn.close()
