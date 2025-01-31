# ✈️ Flight Tracker

A **real-time flight tracking web application** that allows users to enter a flight number and retrieve **live flight details** along with an **exterior image of the aircraft**.

## 🚀 Features
- ✅ **Real-time flight tracking** using the AviationStack API.
- ✅ **Displays flight details**, including:
  - Airline Name
  - Departure & Arrival Airports
  - Flight Status (Scheduled, Active, Delayed, etc.)
- ✅ **Fetches an exterior image** of the aircraft using Planespotters.net.
- ✅ **Modern & professional UI** built with Bootstrap.
- ✅ **Deployed on Render (Free Tier).**

## 🛠️ Technologies Used
- **Python** (Flask Framework)
- **HTML, CSS, Bootstrap** (Frontend UI)
- **APIs**: AviationStack (flight data), Planespotters.net (aircraft images)
- **Gunicorn** (Production-ready web server)

## 📦 Installation & Running Locally
### **1️⃣ Clone the Repository**

git clone https://github.com/YOUR-USERNAME/flight-tracker.git

2️⃣ Set Up a Virtual Environment (Recommended)

3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Run the Flask App

python app.py
The app will be available at http://127.0.0.1:5000/.

🌍 Deployment (Render)

Push your code to GitHub.
Connect your repository on Render
Use these commands for deployment:
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

Click "Deploy" and wait for the app to go live.

📄 License
This project is open-source under the MIT License.
