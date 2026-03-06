from flask import Flask
from flask import Flask, render_template, request

# Create instance of flask
app = Flask(__name__)
# DECISION GENERATOR
# RANDOMLY PICKS FROM A LIST
# 2 HTML (one index, one results)

# Homepage route
@app.route("/")
def index():
    return render_template("index.html")

# RUN THE APP (or type flask run in terminal)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route("/submit", methods=['POST'])
def submit():
    form_data = {
        'Cuisine': request.form.get('cuisine'),
        'Do you want to cook or order?': request.form.get('cook'),
        'Just you or big group?': request.form.get('alone'),
        'Dessert?': request.form.get('dessert')
    }

    return render_template("results.html", form_data=form_data)