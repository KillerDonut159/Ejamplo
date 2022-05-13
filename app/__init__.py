from flask import Flask, render_template, request, redirect, url_for
import sqlitetest4
import sqlitetest5



app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():
    first = request.form.get("finame")
    last = request.form.get("laname")
    print(first, last)
    sqlitetest5.display_test5add(first, last)
    return render_template("hugeform.html", lolzer=[sqlitetest4.display_test(), sqlitetest4.display_test2(), sqlitetest4.display_test3(), sqlitetest5.display_test5check()
    ])

if __name__ == "__main__":
    app.run(debug=True)