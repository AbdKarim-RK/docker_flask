from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>À propos de moi</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                text-align: center;
                margin-top: 100px;
            }
            .card {
                background: white;
                width: 400px;
                margin: auto;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 { color: #0078D7; }
            p { font-size: 1.1em; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Abdoul Karim Mahamadou</h1>
            <p>👨‍💻 Étudiant en ingénierie électronique et informatique</p>
            <p>📍 Localisation : France</p>
            <p>📧 Contact : abdoulkarimmahamad99@gmail.com</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    # Écoute sur toutes les interfaces pour Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
