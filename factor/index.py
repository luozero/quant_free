
from dataset.us_equity_load import *

class index:
  def __init__(self, sectors, start_date, end_date):
     self.sectors = sectors
     self.start_date = start_date
     self.end_date = end_date

  def calc(self):
      dict_index = {}
      for sector in self.sectors:
        print(f"processing {sector} ...")
        symbols = us_dir1_load_csv(dir0 = 'symbol', dir1 = 'fh', filename= sector +'.csv')['symbol'].values
        if (len(symbols) > 0):
          data = us_equity_daily_data_load(symbols = symbols, start_date = self.start_date,
                                            end_date = self.end_date, trade_option = 'market_capital', 
                                            dir_option = 'xq')
          df = pd.DataFrame(data)
          df_sum = df.sum(axis=1)
          index = df_sum * 1000 /df_sum.iloc[0]
          dict_index[sector] = index
        else:
           print(f"remove {sector} ...")
           self.sectors.remove(sector)

      return pd.DataFrame(dict_index)

  def ratio(self, days = 1):
     df = self.calc()
     return df.pct_change(days).round(3) * 100 
