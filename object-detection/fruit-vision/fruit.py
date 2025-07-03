import kagglehub

# Download latest version
path = kagglehub.dataset_download("icebearogo/fruit-classification-dataset")

print("Path to dataset files:", path)