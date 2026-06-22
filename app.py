from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My smart web</title>
        <link rel="icon" href="/favicon.ico">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);  /* Merah-Orange */
background: linear-gradient(135deg, #00D2FC 0%, #3A7BD5 100%);  /* Biru */
background: linear-gradient(135deg, #12C2E9 0%, #C471ED 100%);  /* Cyan-Purple */
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
                padding: 40px;
                max-width: 600px;
                width: 100%;
                text-align: center;
            }
            
            .icon {
                font-size: 80px;
                margin-bottom: 20px;
            }
            
            h1 {
                color: #333;
                font-size: 2.5em;
                margin-bottom: 15px;
            }
            
            .status {
                background: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                display: inline-block;
                font-weight: bold;
                margin-bottom: 30px;
            }
            
            p {
                color: #666;
                font-size: 1.1em;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            
            .info-box {
                background: #f5f5f5;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                border-left: 4px solid #667eea;
            }
            
            .info-box h3 {
                color: #667eea;
                margin-bottom: 10px;
            }
            
            .button {
                background: #667eea;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 25px;
                font-size: 1em;
                cursor: pointer;
                transition: background 0.3s;
                margin: 10px 5px;
            }
            
            .button:hover {
                background: #764ba2;
            }
            
            .data-display {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                margin: 30px 0;
            }
            
            .data-card {
                background: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                border: 2px solid #667eea;
            }
            
            .data-card h4 {
                color: #667eea;
                margin-bottom: 10px;
            }
            
            .data-value {
                font-size: 1.8em;
                font-weight: bold;
                color: #333;
            }
            
            footer {
                margin-top: 30px;
                color: #999;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="icon">🔵A</div>
            
            <h1>Manual Protecien</h1>
            <div class="status">✓ Sistem Aktif</div>
            
            <p>Selamat datang di Web Server Arduino Anda</p>
            
            <div class="info-box">
                <h3>📊 Status Koneksi</h3>
                <p>Web server berjalan dengan baik dan siap menerima data dari Arduino</p>
            </div>
            
            <div class="data-display">
                <div class="data-card">
                    <h4>🌡️ Suhu</h4>
                    <div class="data-value">25.5°C</div>
                </div>
                <div class="data-card">
                    <h4>💧 Kelembaban</h4>
                    <div class="data-value">60%</div>
                </div>
                <div class="data-card">
                <h4>⚡ Daya</h4>
                 <div class="data-value">120W</div>
                       </div>
            </div>
            
            <button class="button">Refresh Data</button>
            <button class="button">Pengaturan</button>
            <button class="button">Tentang</button a href="https://github.com/Arrafa556/Arrafa556/" target="_blank">Arrafa556</a></button>
             <a href="https://github.com/Arrafa556/Arrafa556/" target="_blank">Arrafa556</a>
            
            <footer>
                <p>Arduino Monitoring System © 2026</p>
            </footer>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)