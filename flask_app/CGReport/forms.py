from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class ApnForm(FlaskForm):
    APN = StringField("Parcel Number", validators=[DataRequired()])
    submit = SubmitField("Search Parcels By APN")


class ZoneForm(FlaskForm):
    ZONE = SelectField(
        "Zoning",
        choices=[
            (" ", "None"),
            ("B-1", "B-1"),
            ("B-2", "B-2"),
            ("B-3", "B-3"),
            ("B-4", "B-4"),
            ("CO", "CO"),
            ("I-1", "I-1"),
            ("I-2", "I-2"),
            ("PAD", "PAD"),
        ],
    )
    submit = SubmitField("Search Parcels By Zone")


class ParcelForm(FlaskForm):
    aMin = DecimalField("Acreage Min", validators=[DataRequired()])
    aMax = DecimalField("Acreage Max", validators=[DataRequired()])
    NMTC = SelectField("New Market Tax Credit", choices=[("Yes", "Yes"), ("No", "No")])
    OZ = SelectField("Opportunity Zone", choices=[("Yes", "Yes"), ("No", "No")])
    ZONE = SelectField(
        "Zoning",
        choices=[
            (" ", "None"),
            ("B-1", "B-1"),
            ("B-2", "B-2"),
            ("B-3", "B-3"),
            ("B-4", "B-4"),
            ("CO", "CO"),
            ("I-1", "I-1"),
            ("I-2", "I-2"),
            ("PAD", "PAD"),
        ],
    )
    submit = SubmitField("Search for Parcels")


class Upload(FlaskForm):
    file = FileField()
    submit = SubmitField("Upload File")


class ReportForm(FlaskForm):

    ##Parcel/Site Information
    siteNum = StringField("Site Number")
    siteName = StringField("Site Name")
    apn = StringField("Assessor Parcel Number (APN)", widget=TextArea())
    buildingAddress = StringField("Building Address")
    city = StringField("City", default="Casa Grande")
    zip = StringField("ZIP", default="85193")
    owner = StringField("Owner (or Representative)", widget=TextArea())
    contactEmail = StringField("Contact email")
    contactPhone = StringField("Contact phone")
    totalSquareFeet = StringField("Total Square Feet:", default="N/A")
    manufacturingSpace = StringField("Manufacturing Space (SF)", default="N/A")
    officeSpace = StringField("Office Space (SF)", default="N/A")
    other = StringField("Other (SF)", default="N/A")

    ## NMTC FTZ and OZ are YES NO
    newMarketTaxCredit = SelectField(
        "New Market Tax Credit eligible?", choices=[("Yes", "Yes"), ("No", "No")]
    )
    foreignTradeZone = SelectField(
        "Foreign Trade Zone", choices=[("Yes", "Yes"), ("No", "No")]
    )
    opportunityZone = SelectField(
        "Opportunity Zone", choices=[("Yes", "Yes"), ("No", "No")]
    )
    otherLocalIncentives = StringField(
        "Other Local Incentives",
        default="Possible via a Development Agreement with City & County",
    )
    siteAcreage = StringField("Site Acreage / Additional Acreage Available")

    ##Transportaion Information
    nearestItst = StringField("Nearest Interstate", default="I8")
    i10Dist = StringField("Distance to Interstate 10", default="8 Miles")
    i8Dist = StringField("Distance to Interstate 8", default="3-4 Miles")
    SkyHarborDist = StringField("Distance to Phoenix Sky Harbor", default="46 Miles")
    MesaGatewayDist = StringField(
        "Distance to Phoenix Mesa Gateway", default="43 Miles"
    )
    tiaDist = StringField("Distance to Tucson International", default="76 Miles")
    genAviationAirportDist = StringField(
        "Nearest General Aviation Airport (Distance)",
        default="Casa Grande Municipal Airport",
    )
    absoluteIntermodalDist = StringField(
        "Absolute Intermodal Distance", default="57 Miles"
    )
    inlandPortAzDist = StringField(
        "Inland Port AZ Planned (Class 1) Distance", default="15 Miles"
    )
    intermodalContainerFacilityDist = StringField(
        "Distance to Intermodal Container Facility",
        default="""UP Tucson 80 Miles, BNSF Phoenix -55, New UP
     terminal in development by same owner 15 miles 
     east of site""",
        widget=TextArea(),
    )
    railCarrierToRegion = StringField(
        "Rail Carrier to the Region (Class 1)", default="Union Pacific"
    )
    railCarrierToSite = StringField(
        "Rail Carrier to the Site", default="Union Pacific with switch by Mtn. States"
    )
    locationCoordinates = StringField("Location Coordinates")
    roadServingSite = StringField("Name of Road Directly Serving Site")
    lanesServingSite = StringField(
        "Number lanes of road directly serving site", default="2 Lanes"
    )

    ##Financial Information
    askingLeaseRate = StringField("Asking Lease Rate($/SF/YR", widget=TextArea())
    leaseType = StringField("Type of Lease(NNN/FSG)", default="N/A")
    operatingExpenses = StringField("Operating Expenses($/SF/YR", default="N/A")
    propTaxPer1000 = StringField(
        "Property Tax Rate Per $1000 of Investment:", default="N/A"
    )
    landBuilding = StringField(
        "Land/Building:",
        default="15.89% (Primary + Secondary rate) per $100 of assessed value",
    )
    realPropTaxRate = StringField(
        "Please provide the real property tax rate for this parcel", default="N/A"
    )

    ##Utilities
    utilsAtSite = StringField(
        "What utilities are present at the site?",
        default="Water, Sewer, Electrical, Gas",
    )
    wwTreatmentCap = StringField(
        "What is the wastewater treatment capacity",
        default="12 mgd plant with 6 mgd available",
    )
    powerProvider = StringField("Name of Electric Power Provider", default="APS")
    substationDis = StringField("Distance to substation", default="1 Mile")
    distriLineSiteDis = StringField("Distance of distribution line to site")
    distriVoltage = StringField("Distribution voltage", default="12.47kVA")
    substationCapacity = StringField(
        "Substation capacity (total / available)", default="7.5 MW"
    )
    wastewaterProvider = StringField(
        "Name of Wastewater Provider", default="City of Casa Grande"
    )
    wwLineSize = StringField("Line size (waste)", default='12"')
    wwdistanceToSite = StringField(
        "Distance to site (waste)", default="Immediately Adjacent"
    )
    gravityOrForceMain = StringField(
        "Specify if service is gravity or force main", default="Gravity"
    )
    wwPlantCap = StringField(
        "Wastewater treatment plant capacity (MGD)", default="12MGD"
    )
    totalCapacity = StringField("total (design) capacity", default="12MGD")
    annAvgDlyFlow = StringField("annual average daily flow", default="6MGD")
    peakFlow = StringField("peak flow", default="7MGD")
    excessCapacity = StringField("excess (available) capacity", default="-5MGD")
    totalLineCapacity = StringField("Total Capacity of line serving site")
    excessLineCapacity = StringField("Excess Capacity of line Serving Site")
    telecommProvider = StringField(
        "Telecommunications Provider", default="Century Link/Cox"
    )
    knownServices = StringField(
        "Describe Known Services at Site", default="Century Link"
    )
    fireInsurance = StringField("Fire Insurance Rating at Site", default="ISO 3")
    waterProvider = StringField(
        "Name of Water Provider", default="Arizona Water Company"
    )
    waterLineSize = StringField("Line size (water)")
    waterdistanceToSite = StringField("Distance to site (water)", default="Adjacent")
    flowTestData = StringField(
        "Most recent flow test data (static and residual pressure, gpm)",
        default="3,000 to 4,000 gallons per minute fire flow",
    )
    naturalGasProvider = StringField(
        "Name of Natural Gas Provider", default="Southwest Gas"
    )
    gasLineSize = StringField("Line size (gas)", widget=TextArea())
    gasDistanceToSite = StringField("Distance to site (gas)", default="At Site")
    existingSitePressure = StringField("Existing pressure at site (psi)")

    ##Building Information
    yearBuilt = StringField("Year Built (include any additions)", default="N/A")
    zoning = SelectField(
        "Zoning",
        choices=[
            (" ", "None"),
            ("B-1", "B-1"),
            ("B-2", "B-2"),
            ("B-3", "B-3"),
            ("B-4", "B-4"),
            ("CO", "CO"),
            ("I-1", "I-1"),
            ("I-2", "I-2"),
            ("PAD", "PAD"),
        ],
        default="I-1",
    )
    acrcCreds = StringField("Number of ACRC Credentials w/I 45 minutes", default="842")
    constructionType = StringField("Type of Construction", default="Built to Suit(BTS)")
    truckDoorsAvailable = StringField("Number of Truck Doors Available", default="BTS")
    clearHeight = StringField(
        "Clear Height (min/max) / Column (Bay) Spacing", default="BTS"
    )
    sprinklers = StringField("Sprinklers (Wet or Dry)", default="BTS")
    equipment = StringField(
        "Machinery and Equipment (If exempt, please indicate):", default="Exempt"
    )
    inventories = StringField(
        "Inventories (If exempt, please indicate):", default="Exempt"
    )
    easmentsOrImpediments = StringField(
        "Are there any easements or impediments on the site", default="No"
    )
    topography = StringField(
        "Topography (max grade/variance)", default="Extremely Flat"
    )
    inFloodPlain = StringField("Is the site located in a flood plain", default="No")
    surroundingArea = StringField(
        "What is located in the surrounding area (industrial park, etc.)",
        default="Industrial",
    )

    ##Topography and Environmental
    geoTopoConditions = StringField(
        "Geological and Topographic conditions", default="N/A"
    )
    averageSiteGrade = StringField("Average grade of the site", default="N/A")
    siteGraded = StringField("Has the site been graded?", default="Yes")
    gradingLeadTime = StringField("Lead time for grading", default="N/A")
    siteCleared = StringField("Has the site been cleared?", default="Yes")
    clearingLeadTime = StringField("Lead time for clearing", default="N/A")
    clearingGradingCost = StringField(
        "If not, how much would clearing and grading cost?", default="N/A"
    )
    groundWaterLevel = StringField("Ground water level (i.e. per water table)")
    soilBearingCapacity = StringField("Soil bearing capacity")
    siteWetlandsOrStreams = StringField(
        "Does the site have any wetlands or streams?", default="No"
    )
    soilClayLayers = StringField("Has the soil clay layers?")
    soilPIIndex = StringField("What is the PI Index of the soil?")
    nearFloodPlain = StringField(
        "Is the site located near a flood plain?", default="No"
    )
    seismicZone = StringField(
        "In which seismic zone is the site located?", default="Seismic Zone 1"
    )
    hurricaneZone = StringField("In which hurricane zone is the site located?")
    windLoadZone = StringField(
        "What is the wind load zone for the site?", default="Wind Zone 1"
    )
    siteContamination = StringField(
        "No contamination or pollution on the site?", default="No"
    )
    radioactiveRadiation = StringField(
        "No endangering due to radioactive radiation?", default="No"
    )
    rockyGround = StringField("No rocky ground?", default="No")
    frackingActivities = StringField(
        "Fracking activities around the site? (50 miles radius)", default="No"
    )
    environmentalIssues = StringField(
        "Are there any environmental issues on the site", default="No"
    )
    emissionIssuesOrRestrictions = StringField(
        "Are there any emissions related issues or restrictions on the site?",
        default="County Air Quality Standards",
    )
    formerUses = StringField("Former Uses", default="Agriculture")
    neighboringUses = StringField("Neighboring Uses", default="Agriculture")
    permits = StringField("Permits")
    environmentalAudit = StringField(
        "Existing environmental audit / Phase 1 report?", default="Yes"
    )
    archaeologicalAudit = StringField("Existing archaeological audit?", default="Yes")
    envPermitting = StringField("Lead time for environmental permitting", default="N/A")
    archPermitting = StringField(
        "Lead time for archaeological permitting", default="N/A"
    )
    airPermitting = StringField(
        "Lead time for air permitting", default="Not required for this project"
    )
    attainmentArea = StringField(
        "Is site located in an attainment or non-attainment area?",
        default="Non-attainment Zone for PM-10",
    )

    submit = SubmitField("Generate Report")
