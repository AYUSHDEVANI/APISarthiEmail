# import abc_1
from flask import Flask, request, jsonify
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from weasyprint import HTML

app = Flask(__name__)

# stamp_image = "Images\left-image.png"
# left_image = "Images/left-image.png"
# right_image = "Images/right-image.png"

# Function to generate the contract as a PDF
def generate_contract_pdf(contract_data, output_path):
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contract Farming Agreement</title>
    <style>
        /* Basic reset */
/* General Styles */
body {{
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    margin: 0;
    padding: 12px;
}}

h1, h2, p {{
    color: #333;
    margin: 0;
}}

h1 {{
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    margin-top: 40px;
    color: #0056b3;
}}

h2 {{
    font-size: 24px;
    text-align: center;
    margin: 20px 0;
    font-weight: normal;
}}

p {{
    font-size: 16px;
    text-align: justify;
    margin: 15px 0;
    color: #555;
}}

strong {{
    font-weight: bold;
}}

/* Contract Section Titles */
.clause-title {{
    font-size: 18px;
    font-weight: bold;
    margin-top: 30px;
    border-bottom: 2px solid #0056b3;
    padding-bottom: 5px;
    color: #0056b3;
}}

/* List Styles */
ul {{
    list-style-type: none;
    padding-left: 20px;
}}

ul li {{
    font-size: 16px;
    color: #555;
    margin: 10px 0;
}}

ul ul {{
    margin-left: 20px;
}}

ul ul li {{
    font-size: 15px;
}}

/* Table Styling (for any tabular data if added) */
table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}}

table, th, td {{
    border: 1px solid #ddd;
}}

th, td {{
    padding: 10px;
    text-align: left;
    font-size: 16px;
}}

th {{
    background-color: #f2f2f2;
    font-weight: bold;
}}

/* Paragraph Styling for Better Readability */
p, ul li {{
    text-align: justify;
    font-size: 16px;
}}

p span {{
    display: inline-block;
    margin-bottom: 10px;
}}

/* Footer */
footer {{
    text-align: center;
    font-size: 14px;
    color: #999;
    margin-top: 40px;
    padding-bottom: 20px;
}}

/* Divider line */
hr {{
    border: 0;
    height: 1px;
    background-color: #ccc;
    margin: 40px 0;
}}


    </style>
</head>
<body>
       <!-- Add the header image at the start -->
    <div class="header-image">
        <img src="Images/stamp.jpg" alt="Header Image">
    </div>

    <div class="container">
        <div class="left-image">
            <img src="{"Images/left-image.png"}" alt="Left Image">
        </div>
        
        <div class="content">
            <h1><strong>CONTRACT FARMING AGREEMENT</strong></h1>
            <h3>Contract ID: {contract_data["contract_id"]}</h3>
            <h2><strong>Between</strong></h2>
            <h2><strong>{contract_data["buyer_name"]}</strong></h2>
            <h2><strong>And</strong></h2>
            <h2><strong>{contract_data["seller_name"]}</strong></h2>
            <!-- Add the rest of your content here as needed -->
        </div>
        
        <div class="right-image">
            <img src="Images/right-image.png" alt="Right Image">
        </div>
    </div>
    
    <br><br>
    <p><strong>CONTRACT FARMING AGREEMENT</strong></p>
    <p>between</p>
    <p>{contract_data["seller_name"]} [hereafter called ‘the Farmer`]</p>
    <p>and</p>
    <p>{contract_data["buyer_name"]} having a place of business at {contract_data["buyer_address"]} [hereafter called ‘the Contractor`]</p>
     <p class="clause-title">1. Contract Details</p>
            <ul>
                <li><strong>1.1 Duration of agreement:</strong> {contract_data['agreement_duration']}</li>
                <li><strong>1.2 Start Date:</strong> The agreement shall commence on {contract_data['start_date']}.</li>
                <li><strong>1.3 End Date:</strong> The agreement shall end on {contract_data['end_date']} unless terminated earlier in accordance with the terms outlined herein.</li>
                <li><strong>1.4 Contract Type:</strong></li>
                <ul>
                    <li>The Contractor acts as the Sponsor, providing technical support as well as resources such as seeds, fertilizer, etc.</li>
                    <li>The Farmer retains full responsibility for resources and production.</li>
                </ul>
                <li><strong>1.5 Sponsorship Clause</strong></li>
                <ul>
                    <li>➣ If the buyer is sponsoring:</li>
                    <ul>
                        <li>The contractor agrees to provide the following resources to the farmer:</li>
                        <ul>
                            <li><b>Seeds:</b> {contract_data['seeds']}</li>
                            <li><b>Fertilizers:</b> {contract_data['fertilizers']}</li>
                            <li><b>Pesticides:</b> {contract_data['pesticides']}</li>
                            <li><b>Other support:</b> {contract_data['other_support']}</li>
                        </ul>
                        <li>These inputs will be delivered to the Farmer (Seller) by {contract_data['delivery_date']} and must be used solely for the production of the contracted crop.</li>
                        <li>Any unused inputs must be returned to the Contractor unless otherwise agreed.</li>
                        <li>The Contractor retains the right to monitor and verify the quality of inputs used by the Farmer to ensure compliance with the agreed-upon standards.</li>
                    </ul>
                    <li>➣ If the farmer is responsible for procuring resources:</li>
                    <ul>
                        <li>The farmer agrees to procure all necessary resources for farming, including:</li>
                        <ul>
                            <li><b>Seeds:</b> {contract_data['seeds']}</li>
                            <li><b>Fertilizers:</b> {contract_data['fertilizers']}</li>
                            <li><b>Pesticides:</b> {contract_data['pesticides']}</li>
                        </ul>
                        <li>The Farmer will ensure that the inputs meet the quality standards specified by the Contractor.</li>
                        <li>The Contractor will not bear any costs related to the procurement of inputs.</li>
                    </ul>
                </ul>
            </ul>

            <p class="clause-title">2. Description of Farm Land Covered by Agreement</p>
            <ul>
                <li><strong>2.1 Acreage and Location:</strong> The contracted farmland covers an area of {contract_data['land_size']}, located at {contract_data['farm_address']}.</li>
                <li>The location and boundaries of the farmland are as recorded with the revenue authority of the concerned area.</li>
                <li><strong>2.2 Facilities Available:</strong></li>
                <ul>
                    <li>The farmland is equipped with the following facilities for agricultural production:</li>
                    <ul>
                        <li><b>Irrigation:</b> {contract_data['irrigation_type']}</li>
                        <li><b>Land Features:</b> {contract_data['land_features']}</li>
                        <li><b>Other Facilities:</b> {contract_data['other_facilities']}</li>
                    </ul>
                    <li>These features are deemed adequate for the production of the contracted crops and reflect the specific conditions under which the agreement has been made.</li>
                    <li>The Farmer affirms that the land particulars match the records maintained by the revenue authority and that there are no legal disputes concerning the ownership or possession of the land.</li>
                </ul>
            </ul>

            <p class="clause-title">3. Description of Farm Produce</p>
            <ul>
                <li><strong>3.1 Type of farm produce:</strong> The agricultural produce covered under this agreement shall include {contract_data['crop_name']}.</li>
                <li>The specific variety of the crop to be grown is {contract_data['crop_variety']}, as agreed upon between the Farmer and the Contractor.</li>
                <li><strong>3.2 Quantity of Farm Produce:</strong> The expected quantity of the produce to be delivered by the Farmer is {contract_data['produce_quantity']}, subject to natural factors such as weather and pest conditions.</li>
                <li>Both parties agree to renegotiate the deliverable quantity in case of force majeure events.</li>
                <li><strong>3.3 Quality of Farm Produce:</strong></li>
                <ul>
                    <li>The quality of the produce must meet the following standards:</li>
                    <ul>
                        <li><b>Physical Appearance:</b> {contract_data['physical_appearance']}</li>
                        <li><b>Moisture Content:</b> Not exceeding {contract_data['moisture_content']}.</li>
                        <li><b>Other Quality Parameters:</b> {contract_data['quality_parameters']}</li>
                    </ul>
                    <li>The Contractor reserves the right to inspect and approve the produce before acceptance.</li>
                </ul>
                <li><strong>3.4 Testing and Certification:</strong> The quality parameters shall be verified by {contract_data['testing_method']}, and any disputes regarding quality shall be resolved by mutual agreement or as per {contract_data['dispute_resolution_method']}.</li>
            </ul>
    <p class="clause-title">4. Crop Delivery Arrangements</p>
    <ul>
        <li><strong>4.1 Mode of Delivery:</strong></li>
                The delivery of the contracted farm produce shall be arranged through (select one of following methods), as mutually agreed upon by both parties involved:
                <ul>
                    <li>Pickup by the Contractor: The Contractor shall arrange for the collection of the produce from the Farmer's location at {contract_data['delivery_pickup_address']}.</li>
                    <li>Delivery by the Farmer: The Farmer shall deliver the produce to {contract_data['delivery_location']}.</li>
                    <li>KrishiSarth Delivery Service: The Farmer shall arrange for delivery using KrishiSarth's delivery service.</li>
                </ul>
                <li><strong>4.2 Delivery Timeline:</strong> The delivery shall be made within the agreed timeline of {contract_data['delivery_timeline']}.</li>
                <li><strong>4.3 Inspection Upon Delivery:</strong> 
                <ul> 
                    <li> The Contractor shall inspect the delivered produce upon receipt to ensure that the quality and quantity meet the agreed standards as outlined in the agreement.</li>
                    <li>Any discrepancies shall be reported within [specify time frame, e.g., 24 hours], failing which the delivery shall be deemed accepted.</li>
                    <li>The risk of loss or damage to the produce shall transfer to the Contractor once the delivery has been inspected and accepted.</li>
                </ul>
                </li>
    </ul>

<p class="clause-title">5. Pricing and Payment Arrangements</p>
            <ul>
                <li><strong>5.1 Pricing of Farm Produce:</strong></li>
                <ul>
                    <li>The price for the produce shall be {contract_data['pricing_structure']}, as mutually decided and documented in this agreement.</li>
                    <li>Any changes in the agreed pricing shall require prior written approval from both parties.</li>
                    <li>A guaranteed price of {contract_data['guaranteed_price']} will be offered to the farmer for the produce, ensuring a baseline payment regardless of market conditions.</li>
                    <li>If applicable, the agreement may also include additional payments, such as bonuses or premiums, determined based on specific benchmarks or reference prices, such as market rates or rates set by agricultural bodies.</li>
                </ul>
                <li><strong>5.2 Payment Process:</strong></li>
                <ul>
                    <li>To ensure their commitment, the Contractor must deposit {contract_data['deposit_percentage']}% of the total order value into the app`s in-app wallet at the time of placing the order. This deposit shall serve as a security for the Farmer and as an assurance of the Contractor`s intent to honor the agreement.</li>
                    <li>All payments under this agreement shall be processed through the in-app wallet provided by KrishiSarth Platform.</li>
                    <li>Upon placing the order, the remaining payment amount shall be frozen in the wallet as security for the Farmer.</li>
                    <li>Once the delivery of produce is confirmed by the Contractor, the payment shall be released to the Farmer, with a receipt provided to confirm the transaction.</li>
                    <li>If any dispute arises regarding delivery or quality, the frozen payment shall remain on hold until the dispute is resolved.</li>
                </ul>
                <li><strong>5.3 Market Price Clause:</strong></li>
                <ul>
                    <li>If the farmer receives a market price exceeding {contract_data['market_price_multiplier']} times the agreed price for the produce, the farmer shall have the right to sell the produce in the open market.</li>
                    <li>In such a case, the sponsor may retain the agreement by paying the farmer an amount equal to {contract_data['retention_percentage']} times the difference between the agreed price and the higher market price.</li>
                    <li><strong>Example:</strong> If the agreed amount is ₹100 and the market price is ₹150, the sponsor must pay ₹{contract_data['retention_amount']} (0.5 times the difference) extra, making the new total ₹{contract_data['new_total_price']}, to retain the contract. The farmer must sell the produce to the sponsor if this price is paid.</li>
                    <li>If the farmer chooses to sell the produce in the market at double the agreed price, the farmer is obligated to return the invested amount by the sponsor (e.g., input costs, support, logistics), any advance payment received from the sponsor, along with {contract_data['additional_profit_percentage']}% of the additional profit earned.</li>
                    <li><strong>Example:</strong> If the agreed amount is ₹100 and the market price is ₹200, the farmer must pay back the sponsor's investment and ₹{contract_data['additional_payment']} (25% of ₹100 additional profit).</li>
                </ul>

                <li><strong>5.4 Late Payment Penalties:</strong></li>
                <ul>
                    <li>If payment is not released within the agreed timeline after delivery confirmation, the Buyer shall incur a penalty of {contract_data['late_payment_penalty']}% of the order value per day of delay, unless the delay is due to force majeure events or mutual agreement.</li>
                </ul>
            </ul>


<p class="clause-title">6. Force Majeure Clause</p>
<p>Force Majeure refers to unforeseen and unavoidable external events that hinder the fulfillment of obligations under this agreement. Such events include, but are not limited to:</p>
<ul>
    <li>Natural disasters (e.g., floods, droughts, earthquakes).</li>
    <li>Unseasonal or extreme weather conditions (e.g., hailstorms, heavy rains).</li>
    <li>Epidemics or outbreaks of disease affecting crops, livestock, or people.</li>
    <li>Pest infestations or locust attacks.</li>
</ul>

<p><strong>In the event of Force Majeure:</strong></p>
<ol>
    <li>The affected party must notify the other party promptly and provide evidence of the event (e.g., {contract_data["force_majeure_evidence"]}, such as government reports or weather data).</li>
    <li>Contractual obligations may be suspended for the duration of the Force Majeure event.</li>
    <li><strong>Farmer Compensation:</strong></li>
    <ul>
        <li><strong>a. Force Majeure Before the Harvest</strong></li>
        <ul>
            <li><strong>Scenario:</strong> A drought or pest outbreak destroys the crop before it is ready for harvest.</li>
            <li><strong>Farmer`s Payment:</strong></li>
            <ul>
                <li>During the contract, it is advised for both parties to discuss and agree on a certain percent of payment for such cases.</li>
                <li>If the agreement explicitly covers such cases (e.g., through an insurance clause), the farmer may receive compensation under an insurance policy.</li>
                <li>If no insurance or risk mitigation is included, the farmer may not receive any payment since no produce is delivered, and Force Majeure exempts both parties from fulfilling obligations.</li>
            </ul>
        </ul>
        <li><strong>b. Force Majeure After Harvest but Before Delivery</strong></li>
        <ul>
            <li><strong>Scenario:</strong> The farmer successfully harvests the crop, but a flood prevents delivery or destroys the stored produce.</li>
            <li><strong>Farmer`s Payment:</strong></li>
            <ul>
                <li>During the contract, it is advised for both parties to discuss and agree on a certain percent of payment for such cases.</li>
                <li>If the crop is insured, the insurance provider compensates the farmer for the loss.</li>
                <li>If uninsured, the farmer typically does not receive payment unless the sponsor agrees to partially compensate for inputs or labor costs as a goodwill gesture.</li>
            </ul>
        </ul>
        <li><strong>c. Partial Force Majeure</strong></li>
        <ul>
            <li><strong>Scenario:</strong> The event impacts only part of the crop (e.g., a locust attack destroys 50% of the field).</li>
            <li><strong>Farmer`s Payment:</strong></li>
            <ul>
                <li>During the contract, it is advised for both parties to discuss and agree on a certain percent of payment for such cases.</li>
                <li>The farmer is paid for the undamaged portion of the crop delivered, based on the agreed price.</li>
                <li>The damaged portion is exempt from penalties under Force Majeure.</li>
            </ul>
        </ul>
    </ul>
    <li>If the event destroys only a portion of the crop, the farmer will be paid for the undamaged portion delivered, while the affected portion is exempt from penalties.</li>
</ol>

<p>This clause ensures fairness and protects both parties from liability in extraordinary circumstances beyond their control.</p>

<p class="clause-title">7. Dispute Resolution Mechanism</p>

<p><strong>7.1 Resolution Mechanism</strong></p>
<p>
    Any disputes arising from this agreement, including but not limited to issues related to the delivery, quality, pricing, or payment of farm produce, 
    shall be resolved in a fair and transparent manner through the dispute resolution process facilitated by the KrishiSarth Platform.
</p>

<p><strong>7.2 Resolution Process</strong></p>
<p>
    Disputes will be addressed by a neutral arbitration panel or mediator appointed by the platform. The parties agree to cooperate in good faith to 
    provide necessary evidence or documentation to resolve the dispute efficiently. The platform’s decision on the dispute shall be binding on both 
    parties unless mutually agreed otherwise.
</p>
<p>
    This agreement and its dispute resolution shall be governed by the laws of {contract_data["jurisdiction"]}. Any legal action arising from unresolved disputes 
    shall be addressed in the courts of {contract_data["legal_location"]}. Explained below:
</p>

<ol>
    <li>
        <strong>Conciliation Process:</strong> Both parties will initially attempt to resolve the issue amicably through a Conciliation Board. This board 
        will consist of representatives from both parties to ensure a balanced and fair discussion.
    </li>
    <li>
        <strong>Sub-Divisional Authority:</strong> If the dispute remains unresolved, it will be escalated to the Sub-Divisional Authority, which will decide 
        the matter in a summary manner within 30 days. The decision will have the same enforceability as a decree from a civil court.
    </li>
</ol>

<p><strong>7.3 Outcome of Dispute Resolution</strong></p>
<ul>
    <li>If the dispute is resolved in favor of the Farmer, the deposit and any additional payments owed shall be released to the Farmer.</li>
    <li>If the dispute is resolved in favor of the Contractor, the deposit shall be refunded, and any necessary adjustments to payment will be made accordingly.</li>
    <li>In the case of a shared fault or mutual agreement, the deposit and payment may be split as decided during the resolution process.</li>
</ul>

<p class="clause-title">8. Insurance Agreements</p>

<p><strong>8.1 Coverage Requirements</strong></p>
<p>
    Both parties agree to ensure that the farm produce, including its transportation and storage, is covered under a valid insurance policy (such as KrishiSarth’s in-app crop insurance) to safeguard against potential risks such as:
</p>
<ul>
    <li>Damage</li>
    <li>Theft</li>
    <li>Natural calamities</li>
    <li>Other unforeseen events</li>
</ul>

<p><strong>8.2 Responsibilities of the Farmer and the Contractor</strong></p>
<ul>
    <li>
        <strong>The Farmer:</strong>
        <ul>
            <li>Shall obtain and maintain insurance coverage for the cultivation and harvesting of the agreed crops. This includes risks such as crop failure, pest infestations, or adverse weather conditions.</li>
            <li>Agrees to share relevant details of the insurance policy with the Contractor upon request.</li>
        </ul>
    </li>
    <li>
        <strong>The Contractor:</strong>
        <ul>
            <li>Shall obtain and maintain insurance coverage for the transportation and storage of the farm produce, starting from the point of pickup or delivery.</li>
            <li>Agrees to share details of the insurance policy with the Farmer upon request.</li>
        </ul>
    </li>
    <li>The cost of insurance coverage may be borne by one party or shared between the Farmer and the Contractor, as mutually agreed upon and specified in this agreement.</li>
</ul>

<p><strong>8.3 Claim Settlement</strong></p>
<p>
    In the event of damage or loss covered under the insurance policies, both parties agree to cooperate in filing claims and providing necessary documentation to the insurer.
</p>
<ul>
    <li>Any proceeds from insurance claims shall be used to compensate the affected party or to cover any mutual losses as agreed between the parties.</li>
    <li>
        Neither party shall hold the other liable for losses or damages covered by insurance policies, provided that both parties fulfill their respective obligations to secure and maintain the agreed insurance coverage.
    </li>
    <li>
        Both parties agree to periodically review their insurance policies to ensure adequate coverage and compliance with the terms of this agreement.
    </li>
</ul>

            <p class="clause-title">9. Land Use and Restrictions</p>
            <p>This agreement does not grant the Sponsor/Buyer any ownership, lease, or mortgage rights over the farmer’s land.</p>
            <p>
                <li>Any structures or modifications made during the contract period must be removed or restored to their original state upon termination of the agreement.</li>
                <li>If the Sponsor fails to remove such structures, ownership of these structures will automatically transfer to the farmer at no additional cost.</li>
            </p>
            <p>This clause is intended to protect the farmer’s property rights and ensure that their land remains under their control throughout and after the agreement period.</p>

            <p class="clause-title">10. Amendments and Termination</p>
            <ul>
                <li><p>This agreement may be amended with mutual consent.</p></li>
                <li><p>Either party may terminate the agreement with a [specify notice period, e.g., three months] written notice.</p></li>
                <li><p>Termination will not affect obligations or payments already due under the agreement.</p></li>
            </ul>

            <p class="clause-title">11. Compliance and Exemptions</p>
            <ul>
                <li><p>Both parties agree to comply with applicable laws and agricultural standards.</p></li>
                <li><p>This agreement is exempt from state laws regulating the sale or purchase of agricultural produce, ensuring flexibility and alignment with national regulations.</p></li>
            </ul>

            
            <p>By entering into this agreement, both parties acknowledge and agree to the terms and conditions outlined above.</p>
            <p><strong>For assistance or further information, contact:</strong> {contract_data["contact_information"]}</p>
            <p><strong>Last Updated:</strong> {contract_data["last_updated_date"]}</p>
        </div>
</body>
</html>
    """

    # Convert the HTML to PDF
    HTML(string=html_content).write_pdf(output_path)
    # pdfkit.from_string(html_content, output_path)
    print(f"Contract PDF generated at {output_path}")

# Function to send the contract via email
def send_contract_email(sender_email, sender_password, recipient_email, subject, body, contract_path, sender_name="KrishiSarth"):
    try:
        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = f"KrishiSarth <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject
    

        # Add email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the PDF
        if os.path.exists(contract_path):
            with open(contract_path, 'rb') as contract_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(contract_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(contract_path)}'
                )
                msg.attach(part)
        else:
            print(f"Error: The file '{contract_path}' does not exist.")
            return

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print(f"Email sent successfully to {recipient_email}!")

    except Exception as e:
        print(f"An error occurred: {e}")


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
        generate_contract_pdf(contract_data, pdf_path)
        send_contract_email(sender_email, sender_password, contractor_email, email_subject, email_body, pdf_path, sender_name)
        return jsonify({"message": "Contract sent successfully!"}), 200
    except Exception as e:
        # Log the error and return error response
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,port=5000)