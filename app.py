from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder='.')

BED_AVAILABILITY = {"General Wards":14,"ICU Wards":3,"Emergency Wards":5,"Special Wards":2}
BLOOD_BANK_DATA = {
    "
    "A+": {
        units: 12,
        nearest_bank: "City Blood Center"
    },
    "A-": {
        units: 6,
        nearest_bank: "Red Cross Metro"
    },
    "B+": {
        units: 8,
        nearest_bank: "Red Cross Metro"
    },
    "B-": {
        units: 3,
        nearest_bank: "LifeSave Blood Bank"
    },
    "O+": {
        units: 15,
        nearest_bank: "Central Hospital Bank"
    },
    "O-": {
        units: 2,
        nearest_bank: "LifeSave Blood Bank"
    },
    "AB+": {
        units: 4,
        nearest_bank: "City Blood Center"
    },
    "AB-": {
        units: 1,
        nearest_bank: "Central Hospital Bank"
    }
};
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/book-appointment", methods=["POST"])
def book_appointment():
    data=request.json or {}
    return jsonify({"status":"Success","message":f"Appointment booked with Dr. {data.get('doctor')} ({data.get('department')}) for {data.get('time')}."})

@app.route("/api/beds")
def get_bed_status():
    return jsonify(BED_AVAILABILITY)

@app.route("/api/blood")
def get_blood_availability():
    group=request.args.get("group","O+")
    return jsonify(BLOOD_BANK_DATA.get(group,{"units":0,"nearest_bank":"Not Found"}))

@app.route("/api/chatbot", methods=["POST"])
def chatbot_guidance():
    symptoms=(request.json or {}).get("symptoms","").lower()
    if "fever" in symptoms or "cough" in symptoms:
        guidance="Possible mild viral infection. Rest, stay hydrated, and consult a healthcare professional if symptoms persist or worsen."
    elif "chest pain" in symptoms or "breathlessness" in symptoms:
        guidance="Potentially serious symptoms. Seek urgent medical help or use the emergency service available in your area."
    else:
        guidance="Symptoms logged. Consider consulting a qualified healthcare professional for proper evaluation."
    return jsonify({"guidance":guidance})

@app.route("/api/sos", methods=["POST"])
def trigger_sos():
    return jsonify({"status":"Demo","message":"Emergency SOS request recorded. This is a demonstration; no real ambulance has been dispatched."})

if __name__ == "__main__":
    app.run(debug=True)
