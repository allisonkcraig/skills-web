from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def form_page():
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_page():
	first_name_input = request.form.get('first-name')
	last_name_input = request.form.get('last-name')
	salary_req_input = request.form.get('salary-req')
	job_title_input = request.form.get('job-title')
	return render_template("application.html", first_name=first_name_input, last_name=last_name_input, salary_req=salary_req_input, job_title=job_title_input)

if __name__ == "__main__":
    app.run(debug=True)