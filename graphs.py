import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

plt.style.use("bmh")
df = pd.read_csv("EPA/csv/tickets.csv")

#barchart 
plt.xlabel('Inquiry Status',fontsize=18)
plt.ylabel('Unit ID', fontsize=16) 