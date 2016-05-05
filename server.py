from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = "I<3SecretsToo"

@app.route('/')
def index():
	ninja = "show"
	return render_template('main.html', ninja = ninja)

@app.route('/ninja')
def none_shall_pass():
		ninja4 = "show"
		ninja = "hide"
		return render_template('main.html', ninja = ninja, ninja4 = ninja4)

@app.route('/ninja/<ninjaa>')
def show_ninja(ninjaa):
	ninja4 = "hide"
	if ninjaa == 'red' or ninjaa == 'blue' or ninjaa == 'orange' or ninjaa == 'purple':
		return render_template('main.html', ninja = ninjaa, ninja4 = ninja4)
	else:
		return render_template('404april.html')

app.run(debug=True)