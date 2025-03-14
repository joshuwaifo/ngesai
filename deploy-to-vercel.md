# Deploying NGES.ai to Vercel with your nges.ai domain

Follow these steps to deploy your Flask application to Vercel and connect it to your nges.ai domain:

## Step 1: Download Your Project Files

First, download your project files from Replit by clicking on the three dots in the file explorer and selecting "Download as zip".

## Step 2: Set Up Vercel CLI (Optional)

If you prefer using the command line:
```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy your project
vercel
```

## Step 3: Deploy Using Vercel Web Interface

Alternatively, use the Vercel web interface:

1. Go to [vercel.com](https://vercel.com) and log in
2. Click "Add New" > "Project"
3. Import your project from your Git repository or upload the files directly
4. Configure the project:
   - Framework Preset: Other
   - Build Command: Leave empty
   - Output Directory: Leave empty
   - Install Command: Leave empty

## Step 4: Configure Environment Variables

Add these environment variables in the Vercel project settings:
- `DATABASE_URL`: Your PostgreSQL connection string
- `SESSION_SECRET`: A secure random string for your Flask sessions

## Step 5: Connect Your Custom Domain

1. In your Vercel project dashboard, go to "Settings" > "Domains"
2. Add your custom domain: `nges.ai`
3. Follow Vercel's instructions to verify domain ownership and set up DNS records

## Step 6: Managing Your Database

For the database:
1. You'll need a PostgreSQL database that's accessible from Vercel
2. Options include:
   - Vercel Postgres
   - Supabase
   - Railway
   - Neon
   - Any other PostgreSQL provider that offers a connection string

## Important Notes

- Make sure your application is configured to use environment variables for database connections
- The Flask application is configured to work in both development and production modes
- Static assets will be served correctly thanks to the vercel.json configuration
- NLTK data will be downloaded on the first request if needed

## Troubleshooting

- If you encounter any issues with NLTK data, you might need to include it in your deployment or use a different approach for text processing
- Check Vercel's function logs for any errors
- Ensure your database connection is correct and accessible from Vercel's servers