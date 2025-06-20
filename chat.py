import os
from flask import Flask, render_template_string, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import base64
from dotenv import load_dotenv
import tiktoken

# Load config
load_dotenv()

app = Flask(__name__)

# HTML Template
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mini Data Dashboard</title>
</head>
<body>
    <h1>Mini Data Dashboard</h1>
    <form method="post">
        <label>Enter URL to Analyze:</label>
        <input name="url" type="text" placeholder="https://example.com">
        <button type="submit">Fetch & Analyze</button>
    </form>
    {% if stats %}
        <h2>Fetched URL Stats:</h2>
        <ul>
            <li>Word Count: {{ stats.word_count }}</li>
            <li>Token Count: {{ stats.token_count }}</li>
        </ul>
    {% endif %}

    {% if plot_url %}
        <h2>Random Data Chart</h2>
        <img src="data:image/png;base64,{{ plot_url }}">
    {% endif %}

    <h2>Sample Table (Pandas)</h2>
    {{ table|safe }}
</body>
</html>
"""

# Text Stats Helper
def text_stats_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        word_count = len(text.split())
        tokenizer = tiktoken.get_encoding("cl100k_base")
        tokens = tokenizer.encode(text)
        return {
            "word_count": word_count,
            "token_count": len(tokens)
        }
    except Exception as e:
        return {
            "word_count": 0,
            "token_count": 0,
            "error": str(e)
        }
    
# Plot helper
def generate_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Noisy Sine Wave", color="blue")
    ax.legend()
    ax.set_title("Sine Wave Plot")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

@app.route("/", methods=["GET", "POST"])
def dashboard():
    stats = None
    plot_url = generate_plot()
    
    # Create a sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': np.random.randint(60, 100, 3),
        'Pass': [True, True, False]
    })
    table_html = df.to_html(classes="table table-striped")

    if request.method == "POST":
        url = request.form.get("url")
        stats = text_stats_from_url(url)

    return render_template_string(TEMPLATE, stats=stats, plot_url=plot_url, table=table_html)
