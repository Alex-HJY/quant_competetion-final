import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime

economic_df=pd.read_csv('../data/economic_indicator.csv',encoding='utf-8-sig')
print(economic_df.head())