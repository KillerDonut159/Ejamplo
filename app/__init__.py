from flask import Flask, render_template
import sqlitetest4
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hugeform.html", lolzer=[sqlitetest4.display_test(), sqlitetest4.display_test2(), sqlitetest4.display_test3()])

if __name__ == "__main__":
    app.run(debug=True)