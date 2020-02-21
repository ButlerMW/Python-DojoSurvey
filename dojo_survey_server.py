from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dojo_survey_index.html")

@app.route('/result', methods=["POST"])
def survey_result():
    print("survey info works")
    print(request.form)
    name_from_form = request.form['name']
    locationlist_from_form = request.form['locationlist']
    languagelist_from_form = request.form['languagelist']
    comment_from_form = request.form['comment']
    return render_template("dojo_survey_result.html", name_on_template=name_from_form, location_on_template=locationlist_from_form, language_on_template=languagelist_from_form, comment_on_template=comment_from_form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_page.html")

if __name__=="__main__":
    app.run(debug=True)