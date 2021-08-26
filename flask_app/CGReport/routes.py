from flask import render_template, request, redirect, url_for, jsonify, json
from CGReport import app, forms
import pandas as pd
import os
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread


@app.route("/")
def index():
    return render_template("index.html", title="Report Generation-Map")


@app.route("/report", methods=["GET", "POST"])
def report():

    ## path to records folder
    path = os.path.dirname(os.path.abspath(__file__))
    ## set scope and credentials to connect to sheets and drive api
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]
    credfile = os.path.join(path, "cgcreds.json")
    # set credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name(credfile, scope)
    ## authorize credentials
    client = gspread.authorize(creds)
    # open sheet in google sheets
    sheet = client.open("Casa Grande Site Information").sheet1

    ## check if reportform was submitted
    ReportForm = forms.ReportForm()
    if ReportForm.is_submitted():
        ReportForm.validate()

        reportDict = {}
        for field in ReportForm:
            if (
                field.label.text == "Generate Report"
                or field.label.text == "CSRF Token"
            ):
                continue
            reportDict[field.label.text] = field.data

        # create a dataframe from the dictionary to output to excel
        reportdf = pd.DataFrame.from_dict(reportDict, orient="index")

        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        reportName = f"site{ReportForm.siteNum.data}report{dt_string}.xlsx"

        # output dataframe to excel for download later
        reportdf.to_excel(os.path.join(path, "static", "reports", reportName))

        ## push data to google sheet

        ## get values from dictionary into list
        col_vals = list(reportDict.values())
        for val in col_vals:
            if val == None:
                val = " "

        # start writing to google sheets
        col_count = sheet.col_count
        last_col = len(sheet.row_values(1))
        ## check if there is an empty column to add to or create one if there isn't
        if col_count > last_col:
            sheet.insert_cols([col_vals], col=last_col + 1, value_input_option="RAW")
        else:
            sheet.add_cols(1)
            sheet.insert_cols([col_vals], col=last_col + 1, value_input_option="RAW")

        return redirect(url_for("reportsuccess"))

    ##if form not submitted then do this
    ReportForm = forms.ReportForm()
    row_vals = sheet.row_values(1)
    site_num_val = int(row_vals[-1]) + 1

    return render_template("report.html", ReportForm=ReportForm, siteNum=site_num_val)


@app.route("/reportsuccess", methods=["GET", "POST"])
def reportsuccess():
    path = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(os.path.join(path, "static", "reports"))
    message = "Report Success"
    return render_template("reportsuccess.html", message=message, files=files)


@app.route("/downloads", methods=["GET", "POST"])
def downloads():

    path = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(os.path.join(path, "static", "reports"))

    if request.method == "POST":
        file = request.form["data"]

        rmfile = os.path.join(path, "static", "reports", file)
        os.remove(rmfile)
        response = {"response": 200}
        return redirect(url_for("downloads")), json.dumps(response)

    if len(files) > 0:
        return render_template("downloads.html", files=files)

    return render_template("downloads.html", message="No Files to Download")
