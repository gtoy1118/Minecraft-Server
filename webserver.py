from flask import Flask


app = Flask(__name__)

@app.route("/")
def homepage():
  try:
    file = open("url.txt")
  except:
    return "No IP available"
  url = file.read()
  file.close()
  return "Latest server IP is "+url

if __name__ == "__main__":
  app.run(host="0.0.0.0")