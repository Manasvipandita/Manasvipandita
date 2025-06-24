from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained model
with open('phone_price_prediction.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def prediction():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def brain():
    try:
        Brand = float(request.form['Brand'])
        Model = float(request.form['Model'])
        RAM = float(request.form['RAM'])  # Removed (GB) from variable name
        Storage = float(request.form['Storage'])  # Removed (GB)
        Camera = float(request.form['Camera'])  # Removed (MP)

        values = [Brand, Model, RAM, Storage, Camera]

        # Check if RAM is within valid range
        if 0 < RAM < 258:    
            prediction = model.predict([values])
            return render_template("prediction.html", prediction=prediction)
        else:
            return "Invalid RAM value", 400

    except ValueError as e:
        return f"Invalid input: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
