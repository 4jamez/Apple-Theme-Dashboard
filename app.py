from flask import Flask, render_template

app = Flask(__name__)

# Mock data for your theme dashboard
themes = [
    {"id": 1, "name": "Minimalist Dark", "category": "iOS", "status": "Free"},
    {"id": 2, "name": "Cyberpunk Neon", "category": "Android", "status": "Premium"},
    {"id": 3, "name": "Pastel Dreams", "category": "iOS", "status": "Free"},
]

@app.route('/')
def index():
    return render_template("index.html", themes=themes)

@app.route('/edit/<theme_name>')
def edit_theme(theme_name):
    # These are the actual icons you will "Save to Photos" on your iPhone
    icons = [
        {'app': 'Instagram', 'url': 'https://cdn-icons-png.flaticon.com/512/174/174855.png'},
        {'app': 'WhatsApp', 'url': 'https://cdn-icons-png.flaticon.com/512/733/733585.png'},
        {'app': 'Settings', 'url': 'https://cdn-icons-png.flaticon.com/512/3524/3524659.png'}
    ]
    return render_template('theme_detail.html', name=theme_name, icons=icons)

if __name__ == '__main__':
    app.run(debug=True)