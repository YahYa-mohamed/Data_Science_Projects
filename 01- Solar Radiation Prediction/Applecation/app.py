from flask import Flask, render_template, request
import joblib

# __name__ is equal to app.py
app = Flask(__name__)

# load model from model.pck
model = joblib.load('model.pkl')



@app.route("/", methods=['GET'])
def home():
   return render_template('index.html')



@app.route("/Predict The Radiation", methods=["POST"])
def predict():
	Temperature =  request.form['Temperature']
	Pressure =  request.form['Pressure']
	Humidity =  request.form['Humidity']
	WindDirection =  request.form['WindDirection(Degrees)']
	Speed =  request.form['Speed']
	Year =  request.form['Year']
	Hour_TimeSunRise =  request.form['Hour_TimeSunRise']
	Minute_TimeSunRise =  request.form['Minute_TimeSunRise']
	Hour_TimeSunSet =  request.form['Hour_TimeSunSet']
	Minute_TimeSunSet =  request.form['Minute_TimeSunSet']
	Day =  request.form['Day']
	Month =  request.form['Month']

	if Month == 'January':
		Month=1
	elif Month == 'February':
		Month=2
	elif Month == 'March':
		Month=3
	elif Month == 'April':
		Month=4
	elif Month == 'May':
		Month=5
	elif Month == 'June':
		Month=6
	elif Month == 'July':
		Month=7
	elif Month == 'August':
		Month=8
	elif Month == 'September':
		Month=9
	elif Month == 'October':
		Month=10
	elif Month == 'November':
		Month=11
	else:
		Month=12

	Radiation = model.predict([[Temperature,Pressure,Humidity,WindDirection,Speed,Year,Month,Day,Hour_TimeSunRise,Minute_TimeSunRise,Hour_TimeSunSet,Minute_TimeSunSet]])[0]
	return render_template("index.html", Radiation=Radiation)	




if __name__ == "__main__":
    app.run(debug=True)
