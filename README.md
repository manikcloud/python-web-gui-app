# 🐍 Python Web GUI Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-varunmanik-black.svg)](https://github.com/varunmanik)

A modern, responsive web-based GUI application built with Flask that runs in your browser!

## 🌟 Live Demo
Run locally at: `http://localhost:5000` after following the setup instructions below.

## ✨ Features

- **🎨 Modern UI**: Beautiful, responsive design with gradient backgrounds
- **💬 Interactive Messaging**: Say hello and see messages in real-time
- **📝 Text Editor**: Built-in text editor with save/load functionality
- **💾 File Operations**: Save and download your text content
- **📱 Mobile Friendly**: Responsive design works on all devices
- **⚡ Real-time Updates**: Dynamic content updates without page refresh

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd python_web_app
python3 -m venv venv
source venv/bin/activate
pip install Flask==2.3.3
```

### 2. Run the Application
```bash
# Option 1: Direct run
python app.py

# Option 2: Using the runner script
python run_app.py
```

### 3. Access in Browser
Open your web browser and go to:
- **Local**: http://localhost:5000
- **Network**: http://0.0.0.0:5000

## 🖥️ Application Interface

### Main Features:
1. **Name Input Section**
   - Enter your name and click "Say Hello"
   - Messages appear in real-time below

2. **Messages Area**
   - View all hello messages with timestamps
   - Clear messages with one click

3. **Text Editor**
   - Multi-line text editing
   - Save text to server memory
   - Load previously saved text
   - Download text as a file

4. **Status Bar**
   - Real-time status updates
   - Action confirmations

## 🛠️ Technical Details

### Backend (Flask)
- **Framework**: Flask 2.3.3
- **Routes**: RESTful API endpoints
- **Features**: JSON responses, file handling, in-memory storage

### Frontend (HTML/CSS/JavaScript)
- **Styling**: Modern CSS with gradients and animations
- **Interactions**: Vanilla JavaScript with fetch API
- **Responsive**: Mobile-first design approach

### API Endpoints:
- `GET /` - Main application page
- `POST /api/say_hello` - Send hello message
- `POST /api/clear_messages` - Clear all messages
- `POST /api/save_text` - Save text content
- `GET /api/get_text` - Retrieve saved text
- `GET /api/download_text` - Download text as file

## 📁 Project Structure

```
python_web_app/
├── app.py              # Main Flask application
├── run_app.py          # Application runner script
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/
│   └── index.html     # Main HTML template
└── venv/              # Virtual environment
```

## 🎯 Usage Examples

### 1. Greeting System
- Type your name in the input field
- Click "Say Hello" button
- See personalized greeting appear in messages

### 2. Text Editor
- Write content in the text area
- Click "Save Text" to store it
- Use "Load Text" to retrieve saved content
- Click "Download Text" to get a .txt file

### 3. Message Management
- View all messages with timestamps
- Use "Clear Messages" to reset the message area
- Status bar shows current action results

## 🔧 Customization

### Styling
Edit the CSS in `templates/index.html` to change:
- Colors and gradients
- Fonts and typography
- Layout and spacing
- Animations and effects

### Functionality
Modify `app.py` to add:
- Database integration
- User authentication
- File upload capabilities
- Additional API endpoints

## 🌐 Browser Compatibility

Tested and working on:
- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🔒 Security Notes

This is a development application. For production use:
- Add proper authentication
- Implement CSRF protection
- Use HTTPS
- Add input validation
- Implement rate limiting

## 🚨 Troubleshooting

### Common Issues:

1. **Port already in use**
   ```bash
   # Kill existing Flask processes
   pkill -f "python.*app.py"
   ```

2. **Virtual environment issues**
   ```bash
   # Recreate virtual environment
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install Flask
   ```

3. **Browser not loading**
   - Check if Flask is running: `ps aux | grep python`
   - Verify port 5000 is accessible: `netstat -tuln | grep 5000`
   - Try different browser or incognito mode

## 🎉 Success!

Your Python Web GUI Application is now running! 

**Access it at: http://localhost:5000**

Enjoy your modern, browser-based Python GUI application! 🎊
