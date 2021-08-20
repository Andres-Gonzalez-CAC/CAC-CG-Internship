from flask import render_template,request,redirect,url_for,flash
from CGReport import app,forms,db,session
import pandas as pd
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

@app.route("/")
def index():
    return render_template('index.html',title="Report Generation-Map")



@app.route("/report",methods=['GET','POST'])
def report():
    

    ReportForm = forms.ReportForm()
    if ReportForm.is_submitted():
        ReportForm.validate()

        reportDict = {}
        for field in ReportForm:
            if field.label.text == "Generate Report" or field.label.text == "CSRF Token":
                continue
            reportDict[field.label.text]=field.data
        
        reportdf= pd.DataFrame.from_dict(reportDict,orient='index')
        
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        reportName = f"site{ReportForm.siteNum.data}report{dt_string}.xlsx"
        path = os.path.dirname(os.path.abspath(__file__))
        
        
        reportdf.to_excel(os.path.join(path,'static','reports',reportName))
        
        ## push data to google sheet
        ## set scope and credentials to connect to sheets and drive api
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        credfile = os.path.join(path,'cgcreds.json')
        creds = ServiceAccountCredentials.from_json_keyfile_name(credfile, scope)
        client = gspread.authorize(creds)
        sheet = client.open("Casa Grande Site Information").sheet1

        ## get values from dictionary into list
        col_vals = list(reportDict.values())
        for val in col_vals:
            if val == None:
                val = " "
                
        col_count = sheet.col_count
        last_col = len(sheet.row_values(1))
        ## check if there is an empty column to add to or create one if there isn't
        if col_count > last_col:
            sheet.insert_cols([col_vals],col= last_col+1,value_input_option='RAW')
        else:
            sheet.add_cols(1)
            sheet.insert_cols([col_vals],col= last_col+1,value_input_option='RAW')


        return redirect(url_for('reportsuccess'))

    ReportForm = forms.ReportForm()
    return render_template('report.html',ReportForm=ReportForm)

@app.route('/reportsuccess',methods=['GET','POST'])
def reportsuccess():
    path = os.path.dirname(os.path.abspath(__file__))
    files= os.listdir(os.path.join(path,'static','reports'))
    message="Report Success"
    return render_template('reportsuccess.html',message=message,files=files)

@app.route('/downloads',methods=['GET','POST'])
def downloads():
    path = os.path.dirname(os.path.abspath(__file__))
    files= os.listdir(os.path.join(path,'static','reports'))
    
    return render_template('downloads.html',files=files)

