from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

# Your code for peptide extraction and probability score calculation goes here
# You can use the Python functions you've written for this task

@app.route('/predict', methods=['POST'])
def predict():
    try:
        protein_sequence = request.form['protein_sequence']

        # Call your functions for peptide extraction and probability score calculation
        # Replace the following code with your actual logic
        peptides = ["Peptide1", "Peptide2", "Peptide3"]
        scores = [0.75, 0.86, 0.92]

        # Prepare the response data
        data = []
        for i in range(len(peptides)):
            data.append({
                'sequence_id': f'Sequence {i+1}',
                'peptide_sequence': peptides[i],
                'methylation_site': 'R',
                'score': scores[i]
            })

        return jsonify(data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
