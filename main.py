from chat import app

def main():
    print("\n********** Welcome to Flask App **********")
    print("Starting Flask Dashboard...")
    print("Available on http://127.0.0.1:5000")
    app.run(debug=True)

if __name__ == "__main__":
    main()