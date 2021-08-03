from flask import render_template,request,redirect,url_for
from CGReport import app,forms,db,session
from CGReport.gis_helpers import get_data_feature_layer
import pandas as pd
from werkzeug.utils import secure_filename
import os

@app.route("/")
def index():
    return render_template('index.html',title="Report Generation-Map")

@app.route("/parcels", methods=['GET','POST'])
def parcels():
    return render_template("parcels.html",title='Parcel Search')

@app.route("/apn_search",methods=['GET','POST'])
def apnSearch():
    apnForm = forms.ApnForm()
    if apnForm.validate_on_submit():
        print("apn")
        econLyer = get_data_feature_layer('econ')
        
        wc=f"APN ='{apnForm.APN.data}'"
        parcels = econLyer.query(where=wc,out_fields="APN,Acreage,NMTC,FTZ,OZ,Zoning",as_df=True)
        del parcels['SHAPE']
        del parcels['FID'] 
        parcelsDict = parcels.to_dict()
        session['parcelresults'] = parcelsDict
        session['psmessage'] = 'No Results Found'
        return redirect(url_for('parcelresults'))       
    else:
        apnForm = forms.ApnForm()
        return render_template('apn_search.html',apnForm=apnForm)

@app.route("/zone_search",methods=['GET','POST'])
def zoneSearch():
    zoneForm = forms.ZoneForm()

    if zoneForm.validate_on_submit():
        econLyer = get_data_feature_layer('econ')
        print('zone')
        wc=f"ZONING ='{zoneForm.ZONE.data}'"
        parcels = econLyer.query(where= wc,out_fields="APN,Acreage,NMTC,FTZ,OZ,Zoning",as_df=True)
        del parcels['SHAPE']
        del parcels['FID']
        parcelsDict = parcels.to_dict()
        session['parcelresults'] = parcelsDict
        return redirect(url_for('parcelresults'))
    else:
        zoneForm = forms.ZoneForm()
        return render_template('zone_search.html',zoneForm=zoneForm)

@app.route("/parcel_search",methods=['GET','POST'])
def parcelSearch():
    parcelForm = forms.ParcelForm()
    if parcelForm.is_submitted():
        parcelForm.validate()
        econLyer = get_data_feature_layer('econ')
        
        #create where clause for query
        wc = f"ACREAGE BETWEEN {parcelForm.aMin.data} AND {parcelForm.aMax.data} AND NMTC = '{parcelForm.NMTC.data}' AND OZ = '{parcelForm.OZ.data}' AND ZONING = '{parcelForm.ZONE.data}'"
        
        parcels = econLyer.query(where=wc,out_fields="APN,Acreage,NMTC,FTZ,OZ,Zoning",as_df=True)
        del parcels['SHAPE']
        del parcels['FID']
        if parcels.shape[0] == 0:
            session['psmessage'] = 'No results found.'
            return redirect(url_for('parcelSearch'))
        else:
            parcelsDict = parcels.to_dict()
            session['parcelresults'] = parcelsDict
            return redirect(url_for('parcelresults'))
    
    parcelForm = forms.ParcelForm()
    return render_template('parcel_search.html',parcelForm=parcelForm)

@app.route("/parcelresults",methods=['GET','POST'])
def parcelresults():
    # get parcelsDict from session convert to dataframe then to html
    if 'parcelresults' in session:
        data = session['parcelresults']
        parcelresults = pd.DataFrame(data)
        return render_template("parcelresults.html",parcelresults=parcelresults.to_html(index=False), title="Results")

    message = 'No Data Found'  
    return render_template('parcelresults.html',title="Parcel Search Results",message = message)

@app.route("/report",methods=['GET','POST'])
def report():
    # save csv or xlsx file to file system
    form = forms.Upload()
    if form.is_submitted():
        form.validate()
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(os.path.join(
            'CGReport', 'uploads', filename
        ))    
        return redirect(url_for('reportsupinfo'))

    form = forms.Upload()
    return render_template('report.html',form=form)

@app.route('/report/supinfo',methods=['GET','POST'])
def reportsupinfo():

    return render_template("supinfo.html")