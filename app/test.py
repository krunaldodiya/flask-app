class StrategyType:
  EQUITY_CNC = "EQUITY_CNC"
  EQUITY_MIS = "EQUITY_MIS"
  EQUITY_NRML = "EQUITY_NRML"
  INDEX_MIS = "INDEX_MIS"
  INDEX_NRML = "INDEX_NRML"

class TataMotors:
  def __init__(self) -> None:
    self.Symbol = "TataMotors"

class Nifty50:
  def __init__(self) -> None:
    self.Symbol = "Nifty50"

class Indices:
  def __init__(self) -> None:
    self.Nifty50 = Nifty50()

class Equities:
  def __init__(self) -> None:
    self.TataMotors = TataMotors()

class InstrumentList:
  TataMotors = {"name":"TataMotors"}
  Nifty50 = {"name":"Nifty50"}

class Instrument:
  def __init__(self, instrument) -> None:
    self.name = InstrumentList[instrument].name
    self.segment = InstrumentList[instrument].segment
    self.capitalization = InstrumentList[instrument].capitalization
    self.sector = InstrumentList[instrument].sector

instruments = [{'name': 'Nifty50'}, {'name': 'TataMotors'}]

# def monitor_instruments(instruments: List[Instrument]):
#   for instrument in instruments:
#     monitor_instrument(Instrument(instrument['name']))

#     print(instrument.name, "all")

#     if instrument.name == InstrumentList.Nifty50:
#       print(instrument.name, "selected")

# fundamental_scanner
# technical_scanner