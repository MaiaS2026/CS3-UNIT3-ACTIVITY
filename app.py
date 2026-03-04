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
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'hobby': request.form.get('hobby'),
        'color': request.form.get('favorite_color'),
        'lukcy': request.form.get('lucky_number')
    }

    return render_template("results.html", form_data=form_data)