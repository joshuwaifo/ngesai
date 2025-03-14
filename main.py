import os
import nltk

# Configure NLTK data path
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
if os.path.exists(nltk_data_dir):
    nltk.data.path.append(nltk_data_dir)

from app import app

# This enables both local development and Vercel deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
# For Vercel serverless deployment
app = app
