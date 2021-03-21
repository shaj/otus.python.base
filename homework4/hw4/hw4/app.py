from flask import Flask, render_template

from views.products import product_app


app = Flask(__name__)

app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", endpoint="root")
def hello_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
