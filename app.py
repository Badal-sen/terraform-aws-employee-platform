from flask import Flask, render_template, request, redirect
from models import db, Deployment

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def dashboard():
    deployments = Deployment.query.all()

    total_deployments = Deployment.query.count()

    successful_deployments = Deployment.query.filter_by(
        status="Success"
    ).count()

    failed_deployments = Deployment.query.filter_by(
        status="Failed"
    ).count()

    return render_template(
        "dashboard.html",
        deployments=deployments,
        total_deployments=total_deployments,
        successful_deployments=successful_deployments,
        failed_deployments=failed_deployments
    )

@app.route("/new-deployment", methods=["GET", "POST"])
def new_deployment():

    if request.method == "POST":

        deployment = Deployment(
            application=request.form["application"],
            version=request.form["version"],
            environment=request.form["environment"],
            status=request.form["status"],
            deployed_by=request.form["deployed_by"]
        )

        db.session.add(deployment)
        db.session.commit()

        return redirect("/")

    return render_template("new_deployment.html")

@app.route("/delete/<int:id>")
def delete_deployment(id):

    deployment = Deployment.query.get_or_404(id)

    db.session.delete(deployment)
    db.session.commit()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_deployment(id):

    deployment = Deployment.query.get_or_404(id)

    if request.method == "POST":
        deployment.application = request.form["application"]
        deployment.version = request.form["version"]
        deployment.environment = request.form["environment"]
        deployment.status = request.form["status"]
        deployment.deployed_by = request.form["deployed_by"]

        db.session.commit()

        return redirect("/")

    return render_template(
        "edit_deployment.html",
        deployment=deployment
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
