import numpy as np
import pandas as pd
import math
import array
import time

from AutocadProject.utils import files
from AutocadProject.utils.data import get_dim_info

dxf = files.open_dxf_file()
print(type(dxf))
df, entities, dimensions = get_dim_info(dxf)
print(df)
