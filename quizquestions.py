from flask import Flask, render_template, request, send_from_directory
import requests

app = Flask("quiz")

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/takethequiz')
def takethequiz():
	return render_template("quiz.html")

@app.route('/<path:filename>')
def send_file(filename):
	return send_from_directory(app.static_folder, filename)

@app.route('/quiz', methods=['POST'])
def quiz():
	skin = request.form.get('skin')
	problem = request.form.get('problem')
	result = ""
	if problem == 'ageing':
		if skin == 'dry':
			result = 'Masque Tissu by AVENE';
	if problem == 'ageing':
		if skin == 'combination':
			result = 'Pure Oxygen Radience Mask by LUZERN';
	if problem == 'ageing':
		if skin == 'oily':
			result = 'ChinUp Starter by UPYOURS';

	if problem == 'pores':
		if skin == 'dry':
			result = 'Pores Refining Solution by CLINIQUE';
	if problem == 'pores':
		if skin == 'combination':
			result = 'Pink Clay aha Mask by FACETHEORY';
	if problem == 'pores':
		if skin == 'oily':
			result = 'Algenist by PERFECT';

	if problem == 'acne':
		if skin == 'dry':
			result = 'Clear Skin Probiotic Masque by EMINENCE';
	if problem == 'acne':
		if skin == 'combination':
			result = 'Umbrian Clay Purifying Mask by FRESH';
	if problem == 'acne':
		if skin == 'oily':
			result = 'Ionic Clay Mask by BOTANICS';

	print("Your Perfect Face Mask is: ",result)
	return render_template("quiz.html", product=result)

 
if __name__ == '__main__':
	app.run()

