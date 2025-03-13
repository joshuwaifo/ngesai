import logging
from models import KnowledgeBase, MarketData, Event, Company, TrendData
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Initialize logging
logger = logging.getLogger(__name__)

# Make sure NLTK data is downloaded
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
    """Preprocess text for search functionality."""
    try:
        # Tokenize text
        tokens = word_tokenize(text.lower())
        
        # Remove stop words and punctuation, then lemmatize
        filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
        
        # Join tokens back into a string
        processed_text = ' '.join(filtered_tokens)
        
        return processed_text
    except Exception as e:
        logger.error(f"Error preprocessing text: {e}")
        return text

def search_knowledge_base(query):
    """Search the knowledge base for relevant information."""
    try:
        # Get all knowledge base entries
        kb_entries = KnowledgeBase.query.all()
        
        if not kb_entries:
            logger.warning("No knowledge base entries found")
            return []
        
        # Preprocess query
        processed_query = preprocess_text(query)
        
        # Preprocess knowledge base entries
        documents = [entry.content for entry in kb_entries]
        processed_documents = [preprocess_text(doc) for doc in documents]
        
        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(processed_documents + [processed_query])
        
        # Calculate cosine similarity between query and documents
        doc_vectors = tfidf_matrix[:-1]
        query_vector = tfidf_matrix[-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]
        
        # Create a list of (index, score) tuples and sort by score
        results_with_scores = [(i, score) for i, score in enumerate(similarity_scores)]
        results_with_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Get the top 10 results
        top_results = []
        for idx, score in results_with_scores[:10]:
            if score > 0.1:  # Only include results with a minimum similarity score
                result = {
                    'id': kb_entries[idx].id,
                    'title': kb_entries[idx].title,
                    'content': kb_entries[idx].content[:200] + '...' if len(kb_entries[idx].content) > 200 else kb_entries[idx].content,
                    'category': kb_entries[idx].category,
                    'score': round(score * 100, 2)
                }
                top_results.append(result)
        
        return top_results
    
    except Exception as e:
        logger.error(f"Error searching knowledge base: {e}")
        return []

def search_entities(query, entity_type):
    """Search for entities like events, companies, etc."""
    try:
        processed_query = preprocess_text(query)
        
        if entity_type == 'events':
            entities = Event.query.all()
            texts = [f"{e.name} {e.description}" for e in entities]
        elif entity_type == 'companies':
            entities = Company.query.all()
            texts = [f"{e.name} {e.description}" for e in entities]
        else:
            logger.warning(f"Unknown entity type: {entity_type}")
            return []
        
        if not entities:
            logger.warning(f"No {entity_type} found")
            return []
        
        # Preprocess entity texts
        processed_texts = [preprocess_text(text) for text in texts]
        
        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(processed_texts + [processed_query])
        
        # Calculate cosine similarity
        entity_vectors = tfidf_matrix[:-1]
        query_vector = tfidf_matrix[-1]
        similarity_scores = cosine_similarity(query_vector, entity_vectors)[0]
        
        # Create a list of (index, score) tuples and sort by score
        results_with_scores = [(i, score) for i, score in enumerate(similarity_scores)]
        results_with_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Get the top 5 results
        top_results = []
        for idx, score in results_with_scores[:5]:
            if score > 0.1:  # Only include results with a minimum similarity score
                entity = entities[idx]
                result = {
                    'id': entity.id,
                    'name': entity.name,
                    'description': entity.description,
                    'score': round(score * 100, 2)
                }
                top_results.append(result)
        
        return top_results
    
    except Exception as e:
        logger.error(f"Error searching {entity_type}: {e}")
        return []

def get_market_data_for_visualization(category=None):
    """Get market data formatted for visualization."""
    try:
        if category:
            data = MarketData.query.filter_by(category=category).order_by(MarketData.date).all()
        else:
            data = MarketData.query.order_by(MarketData.date).all()
        
        # Group data by metric name
        grouped_data = {}
        for item in data:
            if item.metric_name not in grouped_data:
                grouped_data[item.metric_name] = {
                    'labels': [],
                    'values': [],
                    'unit': item.unit
                }
            
            grouped_data[item.metric_name]['labels'].append(item.date.strftime('%Y-%m-%d'))
            grouped_data[item.metric_name]['values'].append(item.value)
        
        return grouped_data
    
    except Exception as e:
        logger.error(f"Error getting market data for visualization: {e}")
        return {}

def get_upcoming_events(limit=5):
    """Get upcoming events."""
    from datetime import datetime
    try:
        events = Event.query.filter(Event.start_date >= datetime.utcnow()).order_by(Event.start_date).limit(limit).all()
        return events
    except Exception as e:
        logger.error(f"Error getting upcoming events: {e}")
        return []
