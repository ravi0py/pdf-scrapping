import fitz  # PyMuPDF
import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def categorize_text(text):
    """Categorize text using spaCy NLP."""
    doc = nlp(text)
    categories = {
        'introduction': [],
        'methods': [],
        'results': [],
        'conclusion': [],
        'other': []
    }
    
    current_category = 'other'
    for sent in doc.sents:
        sent_text = sent.text.strip().lower()
        if 'introduction' in sent_text:
            current_category = 'introduction'
        elif 'methods' in sent_text:
            current_category = 'methods'
        elif 'results' in sent_text:
            current_category = 'results'
        elif 'conclusion' in sent_text:
            current_category = 'conclusion'
        
        categories[current_category].append(sent.text.strip())
    
    return categories

def convert_categories_to_csv(categories):
    """Convert categorized text to a CSV formatted string."""
    rows = []
    for category, lines in categories.items():
        for line in lines:
            rows.append({'Category': category, 'Text': line})
    
    df = pd.DataFrame(rows)
    return df.to_csv(index=False).encode('utf-8')
