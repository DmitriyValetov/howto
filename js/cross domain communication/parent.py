from flask import Flask, render_template
app = Flask(__name__)
 

@app.route("/")
def index():
    return render_template('parent_index.html')
 

if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=5000) 