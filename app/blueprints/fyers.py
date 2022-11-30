from app.ioc.fyers import fyersApiBuilder
from flask import Blueprint, request

fyers = Blueprint('fyers', __name__)

@fyers.get("/fyers/profile")
def get_profile():
    try:
        return fyersApiBuilder.client.get_profile()
    except Exception as e:
        raise e

@fyers.get("/fyers/funds")
def get_funds():
    try:
        return fyersApiBuilder.client.funds()
    except Exception as e:
        raise e

@fyers.get("/fyers/holdings")
def get_holdings():
    try:
        return fyersApiBuilder.client.holdings()
    except Exception as e:
        raise e

@fyers.get("/fyers/orderbook")
def get_orderbook():
    try:
        return fyersApiBuilder.client.orderbook()
    except Exception as e:
        raise e

@fyers.get("/fyers/tradebook")
def get_tradebook():
    try:
        return fyersApiBuilder.client.tradebook()
    except Exception as e:
        raise e

@fyers.get("/fyers/positions")
def get_positions():
    try:
        return fyersApiBuilder.client.positions()
    except Exception as e:
        raise e

@fyers.post("/fyers/order")
def place_order():
    try:
        return fyersApiBuilder.client.place_order(data=request.json)
    except Exception as e:
        raise e

@fyers.post("/fyers/order/<order_id>")
def cancel_order(order_id):
    try:
        return fyersApiBuilder.client.cancel_order(data={'id': order_id})
    except Exception as e:
        raise e

@fyers.post("/fyers/history/download")
def download_history_data():
    try:
        return fyersApiBuilder.get_history_data(
            symbol=request.json['symbol'], 
            range_from=request.json['range_from'], 
            range_to=request.json['range_to']
        )
    except Exception as e:
        raise e