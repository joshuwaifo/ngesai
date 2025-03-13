import nltk
import os

# Create a directory for NLTK data if it doesn't exist
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

# Set the download directory
nltk.data.path.append(nltk_data_dir)

# Download required NLTK packages
packages = ['punkt', 'stopwords', 'wordnet']
for package in packages:
    print(f"Downloading {package}...")
    nltk.download(package, download_dir=nltk_data_dir)
    
print("NLTK data download complete!")