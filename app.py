#!/usr/bin/env python3
"""
Python Web GUI Application
A Flask-based web application that runs in the browser
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import tempfile
from datetime import datetime

app = Flask(__name__)

# Store messages in memory (in production, use a database)
messages = []
text_content = ""

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html', messages=messages)

@app.route('/api/say_hello', methods=['POST'])
def say_hello():
    """Handle hello button click"""
    data = request.get_json()
    name = data.get('name', '').strip()
    
    if name:
        message = {
            'text': f"Hello, {name}! Welcome to the Web GUI app.",
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }
        messages.append(message)
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'error': 'Please enter your name first!'})

@app.route('/api/clear_messages', methods=['POST'])
def clear_messages():
    """Clear all messages"""
    global messages
    messages = []
    return jsonify({'success': True})

@app.route('/api/save_text', methods=['POST'])
def save_text():
    """Save text content"""
    global text_content
    data = request.get_json()
    text_content = data.get('content', '')
    return jsonify({'success': True, 'message': 'Text saved successfully'})

@app.route('/api/get_text')
def get_text():
    """Get current text content"""
    return jsonify({'content': text_content})

@app.route('/api/download_text')
def download_text():
    """Download text as file"""
    # Create temporary file
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
    temp_file.write(text_content)
    temp_file.close()
    
    return send_file(temp_file.name, as_attachment=True, download_name='content.txt')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
