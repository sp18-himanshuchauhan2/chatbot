# 📊 Mini Data Dashboard

A Python web application that fetches and analyzes any public webpage, displaying word and token counts, a data plot, and a styled Pandas table — all in one interactive dashboard.

---

## 🚀 Features

- ✅ Analyze **word count** and **GPT token count** from any URL
- 📈 Display a **random data chart** using Matplotlib
- 🧮 Render a **sample Pandas DataFrame** as an HTML table
- 🌐 Built using **Flask**, **BeautifulSoup**, **tiktoken**, and more

---

## 📁 Project Structure

```bash
mini-data-dashboard/
│
├── chat.py             # Helper Python script
├── main.py             # Main Python script
├── requirements.txt    # All required packages with versions
├── .gitignore  
└── README.md
```

---

## 🛠️ Setup Instructions

### Step 1. Clone the Repository

```bash
git clone https://github.com/sp18-himanshuchauhan2/mini-data-dashboard.git
cd mini-data-dashboard
```

### Step 2. Create and Activate a Virtual Environment

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3. Install Required Packages

```bash
pip install -r requirements.txt
```

#### 📦 requirements.txt
```ini
flask==2.2.3
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
requests==2.28.2
beautifulsoup4==4.12.2
python-dotenv==1.0.0
tiktoken==0.5.1
```

### ▶️ How to Run the App

```bash
python main.py
```

<p>You will see:</p>

```cpp
Starting Flask Dashboard...
Available on http://127.0.0.1:5000
```

### 🧪 How to Use
<ol>
    <li>Open your browser and go to: http://127.0.0.1:5000</li>
    <li>Enter any valid public URL (e.g., a Wikipedia page).</li>
    <li>Click Fetch & Analyze.</li>
    <li>See the results:<ul>
        <li>Word Count</li>
        <li>Token Count (useful for GPT models)</li>
        <li>Random Chart (auto-generated)</li>
        <li>A simple Pandas DataFrame in table format</li>
    </ul></li>
</ol>

### 📦 Example Input & Output

#### Input URL:

```cpp
https://en.wikipedia.org/wiki/OnePlus_Nord
```

#### Output Sample:
<ul>
    <li>Word Count: <b>6358</li>
    <li>Token Count: <b>12325</li>
    <li>Random sine plot image</li>
    <li>Table with 3 users, scores, and pass/fail status</li>
</ul>
