from flask import Flask, render_template

# buat objek flask
app = Flask(__name__)

# buat route untuk halaman utama
@app.route("/")
def home():
    return render_template("index.html")

# jalankan server
if __name__ == "__main__":
    app.run(debug=True)