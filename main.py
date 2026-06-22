from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Arduino Monitor</title>
        <link rel="icon" href="/favicon.ico">
    </head>
    <body>
        <h1>✓ Favicon Berhasil!</h1>
        <p>Lihat ikon biru "A" di tab browser</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)