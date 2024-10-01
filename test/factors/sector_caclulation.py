import sys
from pathlib import Path
_this_dir = Path(__file__).parent.parent.parent
sys.path.append(str(_this_dir))

from quant_free.utils.us_equity_utils import *
from quant_free.factor.sectors_ratio import *



if __name__ == "__main__":

  start_date = get_json_config_value("start_date")
  end_date = get_json_config_value("end_date")
  
  sector_file = 'us_equity_sector.csv'
  sectors = list(us_dir1_load_csv(dir0 = 'symbol', dir1 = 'xq', filename=sector_file)['name'].values)

  print(sectors)

  df_index = SectorsRatio(sectors, start_date, end_date, trade_option = 'market_capital', dir = 'xq')
  df = df_index.ratio()
  us_dir1_store_csv(dir0 = 'symbol', dir1 = 'xq', filename='xq_index_price_ratio' + '.csv', data = df)

  df_index = SectorsRatio(sectors, start_date, end_date, trade_option = 'amount', dir = 'xq')
  df = df_index.ratio()
  us_dir1_store_csv(dir0 = 'symbol', dir1 = 'xq', filename='xq_index_amount_ratio' + '.csv', data = df)


  sector_file = 'us_equity_sector.csv'
  sectors = list(us_dir1_load_csv(dir0 = 'symbol', dir1 = 'fh', filename=sector_file)['Sector'].values)

  print(sectors)

  df_index = SectorsRatio(sectors, start_date, end_date, trade_option = 'market_capital', dir = 'fh')
  df = df_index.ratio()
  us_dir1_store_csv(dir0 = 'symbol', dir1 = 'fh', filename='fh_index_price_ratio' + '.csv', data = df)

  df_index = SectorsRatio(sectors, start_date, end_date, trade_option = 'amount', dir = 'fh')
  df = df_index.ratio()
  us_dir1_store_csv(dir0 = 'symbol', dir1 = 'fh', filename='fh_index_amount_ratio' + '.csv', data = df)