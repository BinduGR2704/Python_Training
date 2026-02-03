import pandas as pd
import json
from pandas import json_normalize

with open('/content/raw_nyc_phil.json') as f:
    d = json.load(f)

nucphil = json_normalize(d)
print(nucphil.head(3))

# Create a json file for this program