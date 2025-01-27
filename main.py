from tkinter import filedialog
import pandas as pd
import numpy as np
from icecream import ic



def make_sample_and_population_csv(fulldata_csv_path, samplename, populationname):
    data = pd.read_csv(fulldata_csv_path)
    header = data.columns

    data_shuffled = data.sample(frac=1, random_state=42).reset_index(drop=True)

    sample_size = int(0.2 * len(data_shuffled))

    sample_data = data_shuffled.iloc[:sample_size]
    population_data = data_shuffled.iloc[sample_size:]

    sample_data.to_csv(samplename, index=False, header=header)
    population_data.to_csv(populationname, index=False, header=header)




samplename = 'sample.csv'
populationname = 'population.csv'
# data_path = filedialog.askopenfilename(title="Select The .csv file")
# data_path = r"C:\Users\armfa\PycharmProjects\ThesisGeneticTraitAssociation\canola_data.csv"
# make_sample_and_population_csv(data_path, samplename, populationname)

