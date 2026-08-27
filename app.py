from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///applications.db"
db = SQLAlchemy(app)

SECTORS = ["Fintech", "Banking", "Tech Consultancy", "Defence", "Automotive", "Big Tech", "Other"]
STATUSES = ["Not Applied", "Applied", "Online Assessment", "Interview", "Offer", "Rejected"]

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable = False) 
    role = db.Column(db.String(100), nullable = False)
    sector = db.Column(db.String(50), nullable = False)
    status = db.Column(db.String(50), nullable = False, default =  "Not Applied")
    notes = db.Column(db.Text(), nullable = True)
    date_applied = db.Column(db.String(20), nullable = True)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    applications = Application.query.order_by(Application.id.desc()).all()
    return render_template("index.html", applications=applications, sectors=SECTORS, statuses=STATUSES)


@app.route("/add", methods=["POST"])
def add():
    new_application = Application(
        company=request.form["company"],
        role=request.form["role"],
        sector=request.form["sector"],
        status=request.form["status"],
        date_applied=request.form.get("date_applied"),
        notes=request.form.get("notes")
    )
    db.session.add(new_application)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:app_id>", methods=["GET", "POST"])
def edit(app_id):
    application = Application.query.get_or_404(app_id)

    if request.method == "POST":
        application.company = request.form["company"]
        application.role = request.form["role"]
        application.sector = request.form["sector"]
        application.status = request.form["status"]
        application.date_applied = request.form.get("date_applied")
        application.notes = request.form.get("notes")
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("edit.html", application=application, sectors=SECTORS, statuses=STATUSES)


@app.route("/delete/<int:app_id>", methods=["POST"])
def delete(app_id):
    application = Application.query.get_or_404(app_id)
    db.session.delete(application)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

    


