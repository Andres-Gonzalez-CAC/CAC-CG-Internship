from flask import Flask,render_template,request,redirect
import gis_helpers
app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/home",methods=['GET','POST'])
def home():
    
    return render_template('home.html')

@app.route("/report",methods=['GET','POST'])
def report():
    if(request.method=='POST'):
        req = request.form
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("report.html", feedback=feedback)

        filter_params = {
            "amin": req["amin"],
            "amax": req["amax"],
            "nmtc": req["nmtcradio"],
            "ftz" : req["ftzradio"],
            "oz"  : req["ozradio"]
        }

        df = gis_helpers.query_data(filter_params)
        del df['ObjectId']
        del df['ObjectId2']
        table = df.to_html()
        print(table)
        return render_template('report.html',table=table)
    
    return render_template('report.html',table='No Data')

if __name__ == "__main__":
    app.run(ssl_context='adhoc',debug=True)