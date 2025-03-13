import random
import nltk
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from models import KnowledgeBase, MarketData, Event, Company, TrendData
from data.sample_data import (
    STRATEGIC_ADVISOR_RESPONSES,
    GUIDANCE_SYSTEM_RESPONSES,
    TREND_FORECASTS
)

# Initialize logging
logger = logging.getLogger(__name__)

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
except Exception as e:
    logger.error(f"Failed to download NLTK data: {e}")

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Preprocess text by tokenizing, removing stop words, and lemmatizing."""
    try:
        tokens = word_tokenize(text.lower())
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
        return " ".join(tokens)
    except Exception as e:
        logger.error(f"Error preprocessing text: {e}")
        return text

def get_knowledge_base_data():
    """Get all knowledge base entries from the database."""
    try:
        kb_entries = KnowledgeBase.query.all()
        documents = [entry.content for entry in kb_entries]
        return kb_entries, documents
    except Exception as e:
        logger.error(f"Error retrieving knowledge base data: {e}")
        return [], []

def find_relevant_content(query, category=None):
    """Find relevant content in the knowledge base using TF-IDF and cosine similarity."""
    try:
        kb_entries, documents = get_knowledge_base_data()
        
        if not documents:
            return "No knowledge base data available."
        
        # Preprocess the query
        preprocessed_query = preprocess_text(query)
        
        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents + [preprocessed_query])
        
        # Calculate cosine similarity
        query_vector = tfidf_matrix[-1]
        similarities = cosine_similarity(query_vector, tfidf_matrix[:-1])
        
        # Get top matches
        top_indices = similarities[0].argsort()[-3:][::-1]
        
        # Return combined content from top matches
        relevant_content = "\n\n".join([kb_entries[idx].content for idx in top_indices])
        
        return relevant_content
    except Exception as e:
        logger.error(f"Error finding relevant content: {e}")
        return "Sorry, I couldn't find any relevant information at the moment."

def process_query(query_text, category):
    """Process a user query and generate a response."""
    try:
        logger.info(f"Processing query in category {category}: {query_text}")
        
        # Find relevant content from the knowledge base
        relevant_content = find_relevant_content(query_text, category)
        
        # Generate response based on the query category
        if category == 'strategic_advisor':
            # Get predefined response based on keywords in the query
            for keyword, response in STRATEGIC_ADVISOR_RESPONSES.items():
                if keyword.lower() in query_text.lower():
                    detailed_response = f"{response}\n\nBased on our knowledge base:\n{relevant_content}"
                    return detailed_response
            
            # If no keyword match, return a generic response
            return f"Based on my analysis, here are some strategic recommendations:\n\n{relevant_content}"
            
        elif category == 'guidance_system':
            # Get predefined response based on keywords in the query
            for keyword, response in GUIDANCE_SYSTEM_RESPONSES.items():
                if keyword.lower() in query_text.lower():
                    detailed_response = f"{response}\n\nAdditional information from our knowledge base:\n{relevant_content}"
                    return detailed_response
            
            # If no keyword match, return a generic response
            return f"Here's a step-by-step guide based on your query:\n\n{relevant_content}"
            
        else:
            # Generic response for other categories
            return f"Here's what I found in our knowledge base:\n\n{relevant_content}"
            
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        return "I apologize, but I encountered an error while processing your query. Please try again later."

def generate_report(title, category, description):
    """Generate a report based on the provided details."""
    try:
        logger.info(f"Generating report: {title} in category {category}")
        
        # Find relevant content from the knowledge base
        relevant_content = find_relevant_content(description, category)
        
        # Generate report structure based on category
        if category == 'market_analysis':
            report_content = f"""
# {title}

## Executive Summary
This market analysis report provides insights into the current state of the Saudi gaming and esports industry, focusing on the aspects mentioned in your description.

## Market Overview
{relevant_content}

## Key Findings
- The Saudi gaming market is experiencing rapid growth, with an increasing number of players and viewers.
- The esports sector is particularly promising, with significant investments from government entities.
- Mobile gaming continues to be the most popular platform among Saudi gamers.

## Opportunities
- Developing localized content that appeals to Saudi and regional audiences
- Establishing esports training programs and academies
- Creating partnerships between international and local gaming entities

## Challenges
- Limited local game development talent pool
- Need for more structured esports competitions and leagues
- Cultural considerations for content development

## Recommendations
Based on our analysis, we recommend focusing on mobile game development, esports infrastructure investment, and talent development programs to capitalize on the growing market.
"""
            
        elif category == 'investment_proposal':
            report_content = f"""
# {title}

## Investment Opportunity Overview
This proposal outlines investment opportunities in the Saudi gaming and esports industry, focusing on the areas mentioned in your description.

## Market Potential
{relevant_content}

## Investment Thesis
- The Saudi gaming market is projected to grow significantly in the coming years
- Government support through Vision 2030 initiatives creates a favorable environment
- First-mover advantage in an emerging market

## Proposed Investment Areas
- Game development studios focusing on culturally appropriate content
- Esports venues and infrastructure
- Gaming education and training programs
- Gaming event management companies

## Financial Projections
- Expected ROI: 15-20% within 3-5 years
- Market growth rate: 22% CAGR
- Potential exit strategies: Acquisition by international gaming companies, IPO

## Risk Assessment
- Market competition from established international players
- Regulatory changes affecting gaming content
- Talent acquisition challenges

## Next Steps
We recommend conducting a detailed due diligence process, meeting with potential partners, and developing a phased investment approach.
"""
            
        elif category == 'sponsorship_package':
            report_content = f"""
# {title}

## Sponsorship Opportunity
This package outlines sponsorship opportunities in the Saudi gaming and esports ecosystem, based on your specified interests.

## Audience Demographics
{relevant_content}

## Sponsorship Benefits
- Brand exposure to a young, tech-savvy, and engaged audience
- Association with a rapidly growing industry sector
- Multiple activation opportunities across digital and physical platforms
- Access to valuable consumer data and insights

## Sponsorship Tiers
### Platinum Tier (SAR 500,000+)
- Title sponsorship of major events
- Branded team or league naming rights
- Content integration across all platforms
- Exclusive merchandise opportunities

### Gold Tier (SAR 250,000-499,999)
- Featured sponsorship at select events
- Product placement opportunities
- Premium digital advertising
- Player endorsements

### Silver Tier (SAR 100,000-249,999)
- Event segment sponsorship
- Standard digital advertising package
- Booth presence at events
- Social media promotion

## Success Metrics
- Brand exposure metrics: Impressions, reach, engagement
- Conversion metrics: Website traffic, app downloads, sales
- Sentiment metrics: Brand perception, audience feedback

## Next Steps
Contact our sponsorship team to discuss customizing a package that meets your specific marketing objectives.
"""
            
        else:
            # Generic report template for other categories
            report_content = f"""
# {title}

## Overview
This report provides information and analysis related to the Saudi gaming and esports industry, focusing on {category}.

## Background
{relevant_content}

## Key Points
- The Saudi gaming and esports industry is growing rapidly as part of Vision 2030
- Government support through various initiatives is creating new opportunities
- The market is attracting international attention and investment

## Analysis
Based on the available data and information, we can observe several trends and patterns in the Saudi gaming and esports ecosystem.

## Recommendations
- Focus on areas with strong government support and alignment with Vision 2030
- Consider partnerships between international and local entities
- Invest in talent development and infrastructure

## Conclusion
The Saudi gaming and esports industry presents significant opportunities for growth and development, particularly in the areas highlighted in this report.
"""
        
        return report_content
    
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        return "An error occurred while generating the report. Please try again later."

def get_trend_forecast():
    """Get trend forecasts for the Saudi gaming and esports industry."""
    try:
        # Get current trend data from the database
        trends = TrendData.query.order_by(TrendData.confidence_score.desc()).limit(5).all()
        
        if not trends:
            # Use predefined trend forecasts if no data in database
            return TREND_FORECASTS
        
        # Format trend data
        forecast = []
        for trend in trends:
            forecast.append({
                'name': trend.trend_name,
                'description': trend.description,
                'confidence': int(trend.confidence_score * 100),
                'category': trend.category
            })
        
        return forecast
    
    except Exception as e:
        logger.error(f"Error getting trend forecast: {e}")
        return TREND_FORECASTS  # Return predefined forecasts as fallback
