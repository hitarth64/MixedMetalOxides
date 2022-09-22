import pandas as pd
import numpy as np

class Data:
  def __init__(self):
    self.path = 'datasets/'
    
  def GetData(self, type):
    if type == 'surface':
      return pd.read_pickle(self.path+type+'.pkl')
    elif type == 'o':
      return pd.read_pickle(self.path+type+'Rad.pkl')
    elif type == 'oh':
      return pd.read_pickle(self.path+type+'Rad.pkl')
    elif type == 'ooh':
      return pd.read_pickle(self.path+type+'Rad.pkl')
    elif type == 'exp':
      return pd.read_excel(self.path+'outcome_overpotentials.xlsx')
