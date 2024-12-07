import abc_1
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])
def running():
    return "Server is running!"
@app.route('/send-contract', methods=['POST'])
def send_contract():
    try:
        data = request.json  # Parse JSON data from the request
        
        # Extract contract data from request
        contract_data = data['contract_data']


        contractor_email = data['contractor_email']
        
        email_subject = f"Approved Contract: Assured Contract Farming"
        sender_email = "krishisarthofficial@gmail.com"
        sender_password = "tlmc arid zudz yeac"
          # Use app password if 2FA is enabled
        
        email_body = f"""Dear {contract_data["buyer_name"]} and {contract_data["seller_name"]},\n\nThis email serves as confirmation of the finalized contract between you, the buyer, and {contract_data["seller_name"]}, the seller. The contract has been agreed upon by both parties and is now considered final. Please find the attached signed contract for your reference.\n\nAs per the agreement, no further changes can be made after this point.\nIf you have any questions, please contact us at your earliest convenience.\n\nThank you for your trust in KrishiSarth.\n\n\nBest regards,\nKrishiSarth  \nkrishisarthofficial@gmail.com \n+91-8780557462\n  
        """
        sender_name = "KrishiSarth"
        # Generate contract as PDF
        pdf_path = "approved_contract.pdf"
        abc_1.generate_contract_pdf(contract_data, pdf_path)
        abc_1.send_contract_email(sender_email, sender_password, contractor_email, email_subject, email_body, pdf_path, sender_name)
        return jsonify({"message": "Contract sent successfully!"}), 200
    except Exception as e:
        # Log the error and return error response
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,port=5000)