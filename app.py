from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is Listening"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = request.get_json()
    protein_sequence = data.get('protein_sequence')
    threshold = float(data.get('threshold'))
    enable_threshold = data.get('enableThreshold')

    print(protein_sequence, threshold, enable_threshold)

    # Process the protein_sequence and make predictions
    # ...
    #Q92997	27	LVKLPLPAERVTLADFKGV	0.598706
    prediction_results = [{"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706}
                          ,{"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706}
                          ,{"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706}
                          ,{"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706}
                          ,{"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706},
                          {"SeqId":"Q92997","R site":27,"Peptides":"LVKLPLPAERVTLADFKGV","Prediction Score":0.598706}
                          ]

    # Return the prediction results as JSON
    return jsonify(prediction_results)


if __name__ == '__main__':
    app.run(debug=True)
