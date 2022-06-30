from flask import Flask, render_template, request
from sqlite3 import *

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/save", methods=["POST"])
def save():
	name = request.form["name"]
	phone = request.form["phone"]
	pizza_size = request.form["r1"]
	to  = request.form.get("to")
	oi  = request.form.get("oi")
	co  = request.form.get("co")
	ch  = request.form.get("ch")
	pizza_toppings = ""
	if to:
		pizza_toppings += "Tomato"
	if oi:
		pizza_toppings += "Onion"
	if ch:
		pizza_toppings += "Cheese"

	order = "size:->" + pizza_size + "toppings:->" + pizza_toppings
	con = None

	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql = "insert into orders values('%s', '%s', '%s')"
		cursor.execute(sql % (name, phone, order))
		con.commit()
		return render_template("home.html", m="thanks for placing order")
	except Exception as e:
		con.rollback()
		return render_template("home.html", m=e)
	finally:
		if con is not None:
			con.close()

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)

			 