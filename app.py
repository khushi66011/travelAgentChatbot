from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

destinations = {
    "france": {
        "visa_required": True,
        "vaccination": "Routine + COVID recommended",
        "currency": "Euro (EUR)",
        "emergency": "112",
        "customs": "Say Bonjour while greeting. Tipping 5-10%."
    },
    "japan": {
        "visa_required": False,
        "vaccination": "Routine vaccines recommended",
        "currency": "Japanese Yen (JPY)",
        "emergency": "110 (Police), 119 (Ambulance)",
        "customs": "Bow while greeting. Remove shoes indoors."
    },
    "usa": {
        "visa_required": True,
        "vaccination": "Routine + COVID recommended",
        "currency": "US Dollar (USD)",
        "emergency": "911",
        "customs": "Tipping 15-20% in restaurants."
    },
    "india": {
        "visa_required": False,
        "vaccination": "Routine vaccines",
        "currency": "Indian Rupee (INR)",
        "emergency": "112",
        "customs": "Respect elders. Remove shoes in temples."
    }
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower().strip()

    # -------- START --------
    if "start" in user_message:
        return jsonify({
            "reply": "Hello! I am Treval Agent. How can I help you?",
            "options": ["CHECK VISA", "TRAVEL INFO", "HELP ME"]
        })

    # -------- CHECK VISA --------
    elif "check visa" in user_message:
        return jsonify({
            "reply": "Please enter destination country:",
            "options": []
        })

    # -------- DESTINATION INFO --------
    elif user_message in destinations:
        data = destinations[user_message]

        reply = f"""
Destination: {user_message.upper()}

Visa Required: {"YES" if data['visa_required'] else "NO"}
Vaccination: {data['vaccination']}
Currency: {data['currency']}
Emergency Contact: {data['emergency']}
Local Customs: {data['customs']}
"""

        return jsonify({
            "reply": reply,
            "options": ["CHECK ANOTHER", "THANK YOU"]
        })

    # -------- CHECK ANOTHER --------
    elif "check another" in user_message:
        return jsonify({
            "reply": "Please enter another destination country:",
            "options": []
        })

    # -------- TRAVEL INFO --------
    elif "travel info" in user_message:
        return jsonify({
            "reply": "Do you want vaccination information?",
            "options": ["YES", "NO"]
        })

    elif user_message == "yes":
        return jsonify({
            "reply": "Please enter destination country for details:",
            "options": []
        })

    elif user_message == "no":
        return jsonify({
            "reply": "Would you like visa information instead?",
            "options": ["YES", "NO"]
        })

    # -------- HELP --------
    elif "help me" in user_message:
        return jsonify({
            "reply": "I can help you with Visa Requirements, Vaccination Info, Currency Exchange, Emergency Contacts, and Local Customs.",
            "options": ["CHECK VISA", "TRAVEL INFO"]
        })

    # -------- THANK YOU --------
    elif "thank you" in user_message:
        return jsonify({
            "reply": "You are very welcome. I am always here to assist you with your travel plans. Have a safe and pleasant journey.",
            "options": ["START AGAIN"]
        })

    # -------- START AGAIN --------
    elif "start again" in user_message:
        return jsonify({
            "reply": "Hello again. How can I help you today?",
            "options": ["CHECK VISA", "TRAVEL INFO", "HELP ME"]
        })

    # -------- INVALID INPUT --------
    else:
        return jsonify({
            "reply": "Please type a valid destination like France, Japan, USA, or India.",
            "options": []
        })


if __name__ == "__main__":
    app.run(debug=True)
