import pandas as pd
from mhcflurry import Class1PresentationPredictor

# Load the trained predictor (you can replace with your own trained model)
predictor = Class1PresentationPredictor.load()

# Example peptide sequences and MHC alleles
peptides = ["SIINFEKL", "SIINFEKD", "SIINFEKQ"]
alleles = ["HLA-A0201", "HLA-A0301"]

# Generate predictions for each peptide and allele
predictions = []
for peptide in peptides:
    for allele in alleles:
        prediction = predictor.predict([peptide], [allele])
        predictions.append({
            "Peptide": peptide,
            "Allele": allele,
            "Predicted Affinity (nM)": prediction#["prediction"],
        })

# Create a DataFrame from the predictions
df = pd.DataFrame(predictions)

# Print the predictions
print(df)
