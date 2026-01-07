"""
Tamil Story Generator - Backend API
"""

import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import urllib.request
import urllib.parse
import json

from story_generator import TamilStoryGenerator

app = Flask(__name__)
CORS(app)

story_generator = TamilStoryGenerator()
print("✅ Tamil Story Generator initialized")


def translate_text(text, target_lang):
    """Translate text using Google Translate (free)"""
    if target_lang == 'en' or not text:
        return text
    try:
        base_url = "https://translate.googleapis.com/translate_a/single"
        params = {'client': 'gtx', 'sl': 'en', 'tl': target_lang, 'dt': 't', 'q': text}
        url = base_url + '?' + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=10)
        result = json.loads(response.read().decode('utf-8'))
        translated = ''.join([s[0] for s in result[0] if s[0]])
        return translated if translated else text
    except Exception as e:
        print(f"Translation error: {e}")
        return text


@app.route('/')
def serve_frontend():
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend')
    return send_from_directory(frontend_path, 'index.html')


@app.route('/<path:filename>')
def serve_static(filename):
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend')
    return send_from_directory(frontend_path, filename)


@app.route('/api/generate-story', methods=['POST'])
def generate_story():
    """Generate Tamil story"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        keywords = data.get('keywords', [])
        age_group = data.get('age_group', 'all')
        language = data.get('language', 'en')
        
        if not keywords:
            return jsonify({'success': False, 'error': 'No keywords provided'}), 400
        
        keywords = [k.strip() for k in keywords if k.strip()]
        
        print(f"🎯 Generating: {keywords}, {age_group}, lang={language}")
        
        story_data = story_generator.generate_tamil_story(keywords, age_group)
        
        # Translate if not English
        title = translate_text(story_data.title, language) if language != 'en' else story_data.title
        moral = translate_text(story_data.moral, language) if language != 'en' else story_data.moral
        
        # Build pages
        pages = []
        for p in story_data.pages:
            page_title = translate_text(p.title, language) if language != 'en' else p.title
            page_content = translate_text(p.content, language) if language != 'en' else p.content
            
            pages.append({
                'page_number': p.page_number,
                'title': page_title,
                'content': page_content,
                'characters': p.characters,
                'location': p.location,
                'action': p.action
            })
        
        # Translate educational facts
        edu_facts = story_data.educational_facts
        if language != 'en' and edu_facts:
            edu_facts = [translate_text(f, language) for f in edu_facts]
        
        story_dict = {
            'title': title,
            'keywords': story_data.keywords,
            'pages': pages,
            'moral': moral,
            'age_group': story_data.age_group,
            'festival_connection': story_data.festival_connection,
            'region': story_data.region,
            'era': story_data.era,
            'story_type': story_data.story_type,
            'historical_context': story_data.historical_context,
            'cultural_elements': story_data.cultural_elements,
            'educational_facts': edu_facts,
            'total_pages': story_data.total_pages,
            'language': language
        }
        
        print(f"✅ Generated: {story_dict['title']} with {len(pages)} pages")
        return jsonify({'success': True, 'story': story_dict})
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'Tamil Story Generator API running'})


if __name__ == '__main__':
    print("🚀 Starting Tamil Story Generator...")
    print("📍 http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
