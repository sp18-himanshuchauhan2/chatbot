📊 Mini Data Dashboard
A Python web application that fetches and analyzes any public webpage, displaying word and token counts, a sample data chart, and a rendered Pandas table — all in one interactive dashboard.

🚀 Features
Analyze the word count and GPT token count of any webpage (via URL).

Display a random data chart generated using NumPy and Matplotlib.

Render a Pandas DataFrame as a styled HTML table.

Simple web UI built with Flask.

📁 Project Structure
bash
Copy
Edit
my_project/
│
├── dashboard_app.py        # Main Python script
├── requirements.txt        # All required packages with versions
├── .env                    # (Optional) Environment file for secrets/configs
└── README.md               # This file
⚙️ Setup Instructions
✅ Step 1: Create Virtual Environment (Manually)
bash
Copy
Edit
# For Windows
python -m venv env
env\Scripts\activate

# For macOS/Linux
python3 -m venv env
source env/bin/activate
✅ Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt:

txt
Copy
Edit
flask==2.2.3
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
requests==2.28.2
beautifulsoup4==4.12.2
python-dotenv==1.0.0
tiktoken==0.5.1
▶️ How to Run the App
bash
Copy
Edit
python dashboard_app.py
You will see:

nginx
Copy
Edit
Starting Flask Dashboard...
Available on http://127.0.0.1:5000
🧪 How to Use
Open your browser and go to: http://127.0.0.1:5000

Enter any valid public URL (e.g., a Wikipedia page).

Click Fetch & Analyze.

See the results:

Word Count

Token Count (useful for GPT models)

Random Chart (auto-generated)

A simple Pandas DataFrame in table format

📦 Example Input
URL:

arduino
Copy
Edit
https://en.wikipedia.org/wiki/OnePlus_Nord
Output:

Word Count: ~6350

Token Count: ~12300

Random noisy sine plot

A 3-row sample table of names and scores

🧰 Technologies Used
Library	Purpose
Flask	Web server and routing
Pandas	Data table creation
NumPy	Numerical calculations
Matplotlib	Data visualization (plotting)
Requests	Fetching webpage HTML
BeautifulSoup4	HTML parsing
python-dotenv	Config management
tiktoken	GPT-style token counting

📌 Notes
Requires internet access to fetch and analyze online URLs.

Only supports plain HTML (not JavaScript-rendered pages).

Tested on Python 3.10+

💡 Future Ideas
Add file upload support for .txt or .html files

Save token/word stats to a CSV

Add more visualizations and user input options

🧑‍💻 Author
Himanshu Chauhan
Student at IIIT Delhi
Feel free to connect or contribute!