import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt


# Load the data
data_path = r'sample.csv'
data = pd.read_csv(data_path)

# Show the first few rows and check the structure
data.head(), data.info()


# Separate SNP data and trait data
snp_data = data.iloc[:, 2:-7]  # SNP columns (excludes first two columns and last 7 trait columns)
trait_data = data[['yld']]     # Using 'yld' as an example trait

# Initialize lists to store p-values and SNP names
p_values = []
snp_names = snp_data.columns


# Perform GWAS for each SNP
for snp in snp_names:
    # Prepare the SNP data and add constant for intercept
    X = sm.add_constant(snp_data[snp])
    y = trait_data['yld']

    # Fit linear regression model
    model = sm.OLS(y, X)
    results = model.fit()

    # Append the p-value for the SNP
    p_values.append(results.pvalues.iloc[1])  # p-value for the SNP (2nd in results.pvalues)

# Adjust p-values for multiple testing (Benjamini-Hochberg)
adjusted_p_values = multipletests(p_values, method='fdr_bh')[1]

# Store results in a DataFrame
gwas_results = pd.DataFrame({
    'SNP': snp_names,
    'p_value': p_values,
    'adjusted_p_value': adjusted_p_values
})

# Show top 10 SNPs by significance
gwas_results.sort_values(by='adjusted_p_value', inplace=True)
ic(gwas_results.head(10))



# Select a top SNP from the GWAS results for plotting (e.g., 'Bn-A03-p22744766')
selected_snp = 'Bn-A03-p22744766'

# Plotting SNP vs Yield (yld)
plt.figure(figsize=(10, 6))
plt.scatter(data[selected_snp], data['yld'], alpha=0.6, c="b")
plt.xlabel(f'SNP {selected_snp} (Values: -1, 0, 1)')
plt.ylabel('Yield (yld)')
plt.title(f'Relationship Between SNP {selected_snp} and Yield (yld)')
plt.grid(True)
plt.show()



