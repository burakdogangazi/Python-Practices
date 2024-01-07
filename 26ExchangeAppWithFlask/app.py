from flask import Flask,render_template,request
import requests

api_key ="08788a46f3faafbd0b2bf6b4bf7f7ae9"

url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")
        response  = request.get(url) # get request attık
        # app.logger.info(response) 

        infos = response.json()

        firstValue = infos["rates"][firstCurrency] # eur/usd
        secondValue = infos["rates"][secondCurrency]# eur/try

        result = (secondValue / firstValue) * float(amount)

        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)