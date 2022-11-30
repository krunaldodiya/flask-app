from app.config.fyers import config
from fyers_api import accessToken, fyersModel
from fyers_api.Websocket import ws
from fyers_api_builder import FyersApiBuilder


class FyersIoc:
  instance = None

  def __init__(self, config):
    if not self.instance:
      self.instance = FyersApiBuilder(config=config, accessToken=accessToken, fyersModel=fyersModel, ws=ws)

  def singleton(self):
    if not self.instance:
      raise Exception("Instance not available")

    return self.instance

fyersApiBuilder = FyersIoc(config).singleton()
