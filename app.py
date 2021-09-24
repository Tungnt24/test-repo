from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<html>helo nguyentutung</html>"

if __name__ == "__main__":
    app.run()
