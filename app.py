from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# HTML template with a green background
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Green Flask App</title>
    <style>
        body {
            background-color: green;
            color: white;
            text-align: center;
            padding-top: 50px;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, message="This is New update Version")

# Health Check Endpoint
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
