# 📊 Mini Data Dashboard

A Python web application that fetches and analyzes any public webpage, displaying word and token counts, a data plot, and a styled Pandas table — all in one interactive dashboard.

---

## 🚀 Features

- ✅ Analyze **word count** and **GPT token count** from any URL
- 📈 Display a **random data chart** using Matplotlib
- 🧮 Render a **sample Pandas DataFrame** as an HTML table
- 🌐 Built using **Flask**, **BeautifulSoup**, **tiktoken**, and more

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sp18-himanshuchauhan2/mini-data-dashboard.git
cd mini-data-dashboard
```

### 2. Create and Activate a Virtual Environment

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

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 📦 requirements.txt
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
