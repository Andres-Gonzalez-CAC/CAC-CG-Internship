from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,SubmitField,SelectField,FileField
from wtforms.validators import DataRequired


class ApnForm(FlaskForm):
    APN = StringField('Parcel Number',validators=[DataRequired()])
    submit = SubmitField('Search Parcels By APN')

class ZoneForm(FlaskForm):
    ZONE = SelectField('Zoning',choices = [(" ","None"),("B-1","B-1"),("B-2","B-2"),("B-3","B-3"),("B-4","B-4"),("CO","CO"),("I-1","I-1"),("I-2","I-2"),("PAD","PAD")])
    submit = SubmitField('Search Parcels By Zone')

class ParcelForm(FlaskForm):
    aMin = DecimalField('Acreage Min',validators=[DataRequired()])
    aMax = DecimalField('Acreage Max',validators=[DataRequired()])
    NMTC = SelectField('New Market Tax Credit',choices =[('Yes','Yes'),('No','No')])
    OZ = SelectField('Opportunity Zone',choices =[('Yes','Yes'),('No','No')])
    ZONE = SelectField('Zoning',choices = [(" ","None"),("B-1","B-1"),("B-2","B-2"),("B-3","B-3"),("B-4","B-4"),("CO","CO"),("I-1","I-1"),("I-2","I-2"),("PAD","PAD")])
    submit = SubmitField('Search for Parcels')

class Upload(FlaskForm):
    file = FileField()
    submit = SubmitField('Upload File')