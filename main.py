import numpy as np
import pandas as pd
import math
import array
import time

from utils import files
from utils.data import get_dim_info

dxf = files.open_dxf_file()
df, entities, dimensions = get_dim_info(dxf)
print(df)
