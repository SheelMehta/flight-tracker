from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="templates")

API_KEY = "bd03a81a21c05ea96e2e2372ade3b8c7"
BASE_URL = "http://api.aviationstack.com/v1/flights"

# Function to fetch flight details
def get_flight_details(flight_number):
    params = {"access_key": API_KEY, "flight_iata": flight_number}
    response = requests.get(BASE_URL, params=params)

    print(f"\n--- API Debugging ---")
    print(f"Request URL: {response.url}")
    print(f"Response Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    if response.status_code == 200:
        data = response.json()
        if data.get("data"):
            return data["data"][0]  # Return first result
    return None

# Function to get an exterior image from Planespotters.net
def get_exterior_image(registration):
    if not registration:
        return None
    return f"https://www.planespotters.net/search?q={registration}"

@app.route("/", methods=["GET", "POST"])
def home():
    flight_data = None
    exterior_img = None
    error_message = None

    if request.method == "POST":
        flight_number = request.form.get("flight_number")

        print(f"\n--- Debugging Info ---")
        print(f"Received Flight Number: {flight_number}")

        if flight_number:
            flight_data = get_flight_details(flight_number)

            if flight_data:
                registration = flight_data["aircraft"].get("registration")
                exterior_img = get_exterior_image(registration)
                print(f"Flight Found! Registration: {registration}")
            else:
                error_message = f"❌ No data available for flight {flight_number}. Try another flight."
                print(error_message)

    return render_template(
        "index.html",
        flight=flight_data,
        exterior_img=exterior_img,
        error_message=error_message
    )

if __name__ == "__main__":
    app.run(debug=True)