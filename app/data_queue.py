import threading
from queue import Queue

from app.ioc.fyers import fyersApiBuilder

data_queue = Queue()

def custom_message(msg):
  print(msg)
  print("\n")

def subscribe_to_live_data(symbol):
  fyersApiBuilder.subscribe(
    symbol=symbol, data_type="symbolData", custom_message=custom_message
  )

def start_live_data_thread(symbol):
  live_data_thread = threading.Thread(target=subscribe_to_live_data, args=(symbol, None))
  live_data_thread.start()

start_live_data_thread(symbol=["NSE:NIFTY50-INDEX", "NSE:NIFTYBANK-INDEX"])
