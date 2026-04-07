from flask import Flask, render_template
import os

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

PROJECTS = [
    {
        "title": "Consigliare Editor",
        "status": "Stable",
        "status_class": "badge-stable",
        "desc": "La guida definitiva agli editor 2026. Ottimizzata per performance e SEO.",
        "link": "https://stanckdev-consigliare-editor.netlify.app"
    },
    {
        "title": "stanckDEV|OFF.WEB.",
        "status": "Stable",
        "status_class": "badge-stable",
        "desc": "L'architettura che stai navigando. SPA custom focalizzata su UX fluida e design Bento.",
        
    },

]

@app.route('/')
def index(): return render_template('index.html', projects=PROJECTS)

@app.route('/visione')
def visione(): return render_template('visione.html')

@app.route('/business')
def business(): return render_template('business.html')

@app.route('/blog')
def blog(): return render_template('blog.html')

@app.route('/google495aa6fdf106bb3c.html') 
def google_verification():
    return "google-site-verification: google495aa6fdf106bb3c.html" 

app = app
# Cancella queste righe:
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)