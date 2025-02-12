import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./dataset/Sample_Data_for_Activity.csv")
print(df.head())

sns.displot(df['Normal_Distribution'], kde=True)

output_path = "./output/Activity1Plot.jpg"
plt.savefig(output_path)