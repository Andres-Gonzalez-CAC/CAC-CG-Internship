# coding: utf-8
from CGReport import db


class Parcel(db.Model):
    __tablename__ = 'Parcels'

    APN = db.Column(db.Text, primary_key=True)
    Acreage = db.Column(db.Numeric, nullable=False)
    NMTC = db.Column(db.Text, nullable=False)
    FTZ = db.Column(db.Text, nullable=False)
    OZ = db.Column(db.Text, nullable=False)
    Zone_Type = db.Column(db.Text)



class SiteParcel(db.Model):
    __tablename__ = 'Site_Parcels'

    APN = db.Column(db.Text, primary_key=True)
    Site_Num = db.Column(db.Integer, primary_key=True)



class Site(db.Model):
    __tablename__ = 'Sites'

    Site_Num = db.Column(db.Integer, primary_key=True)
    Site_Name = db.Column(db.Text, nullable=False)
    Site_Address = db.Column(db.Text)
    Site_Owner = db.Column(db.Text)
    Owner_Phone = db.Column(db.Text)
    Owner_Email = db.Column(db.Text)
    Distance_I10 = db.Column(db.Numeric)
    Distance_I8 = db.Column(db.Numeric)
    Distance_PHX_SH = db.Column(db.Numeric)
    Distance_PHX_MG = db.Column(db.Numeric)
    Distance_TIA = db.Column(db.Numeric)
    Distance_CGM = db.Column(db.Numeric)
    Nearest_Fire_Dept = db.Column(db.Numeric)
    Nearest_Police = db.Column(db.Numeric)



class SupplementarySiteInfo(db.Model):
    __tablename__ = 'Supplementary_Site_Info'

    Site_Num = db.Column(db.Integer, primary_key=True)
    Total_Square_Feet = db.Column(db.Numeric)
    Manufacturing_Space_SF = db.Column(db.Float)
    Office_Space_SF = db.Column(db.Float)
    Other_SF = db.Column(db.Float)
    Other_local_incentives = db.Column(db.Text)
    Asking_Lease_Rate_SFYR = db.Column(db.Text)
    Type_of_Lease_NNNFSG = db.Column(db.Float)
    Operating_Expenses_SFYR = db.Column(db.Float)
    Year_Built_include_any_additions = db.Column(db.Float)
    Absolute_Intermodal_Distance = db.Column(db.Text)
    Inland_Port_AZ_Planned_Distance = db.Column(db.Text)
    Number_of_ACRC_Credentials_wI_45_minutes = db.Column(db.Integer)
    Type_of_Construction = db.Column(db.Text)
    Num_of_Truck_Doors_Available = db.Column(db.Text)
    Clear_Height_minmax__Column_Bay_Spacing = db.Column(db.Text)
    Sprinklers_Wet_or_Dry = db.Column(db.Text)
    Electric_Power_Provider_distance_to_substation = db.Column(db.Text)
    Property_Tax_Rate_per_1000_of_Investment = db.Column(db.Float)
    LandBuilding = db.Column(db.Text)
    Machinery_and_Equipment = db.Column(db.Text)
    Inventories = db.Column(db.Text)
    If_exempt_please_indicate = db.Column(db.Float)
    Distance_to_Intermodal_Container_Facility = db.Column(db.Text)
    Rail_Carier_to_the_Site = db.Column(db.Text)
    Rail_Carier_to_the_Region_Class_1 = db.Column(db.Text)
    Are_there_any_easements_or_impediments_on_the_site = db.Column(db.Text)
    Topography_max_gradevariance = db.Column(db.Text)
    Is_the_site_located_in_a_flood_plain = db.Column(db.Text)
    What_is_located_in_the_surrounding_area_industrial_park_etc = db.Column(db.Text)
    What_utilities_are_present_at_the_site = db.Column(db.Text)
    Are_there_any_wetlands_on_the_site = db.Column(db.Text)
    Are_there_any_environmental_issues_on_the_site = db.Column(db.Text)
    Are_there_any_emissions_related_issues_or_restrictions_on_the_site = db.Column(db.Text)
    What_is_the_wastewater_treatment_capacity = db.Column(db.Text)
    Please_provide_the_real_property_tax_rate_for_this_parcel = db.Column(db.Float)
    Location_Coordinates = db.Column(db.Text)
    Name_of_Road_Directly_Serving_Site = db.Column(db.Text)
    Number_lanes_of_road_directly_serving_site = db.Column(db.Text)
    Name_of_Electric_Power_Provider = db.Column(db.Text)
    Distance_to_substation = db.Column(db.Text)
    Distance_of_distribution_line_to_site = db.Column(db.Text)
    Distribution_voltage = db.Column(db.Text)
    Substation_capacity_total__available = db.Column(db.Text)
    Name_of_Wastewater_Provider = db.Column(db.Text)
    Line_size = db.Column(db.Text)
    Distance_to_site = db.Column(db.Text)
    Specify_if_service_is_gravity_or_force_main = db.Column(db.Text)
    Wastewater_treatment_plant_capacity_MGD = db.Column(db.Text)
    _total_design_capacity = db.Column(db.Text)
    _annual_average_daily_flow = db.Column(db.Text)
    _peak_flow = db.Column(db.Text)
    _excess_available_capacity = db.Column(db.Text)
    Total_Capacity_of_line_serving_site = db.Column(db.Float)
    Excess_Capacity_of_line_serving_site = db.Column(db.Float)
    Telecommunication_Providers = db.Column(db.Text)
    Describe_known_service_at_site = db.Column(db.Text)
    Fire_Insurance_Rating_at_Site = db.Column(db.Text)
    Name_of_Water_Provider = db.Column(db.Text)
    Line_size1 = db.Column(db.Text)
    Distance_to_site1 = db.Column(db.Text)
    Most_recent_flow_test_datastatic_and_residual_pressure_gpm = db.Column(db.Text)
    Name_of_Natural_Gas_Provider = db.Column(db.Text)
    Line_size2 = db.Column(db.Text)
    Distance_to_site2 = db.Column(db.Text)
    Existing_pressure_at_site_psi = db.Column(db.Text)
    Former_Uses = db.Column(db.Text)
    Neighboring_Uses = db.Column(db.Text)
    Geological_and_Topographic_conditions = db.Column(db.Float)
    Average_grade_of_the_site = db.Column(db.Float)
    Has_the_site_been_graded = db.Column(db.Text)
    Lead_time_for_grading = db.Column(db.Float)
    Has_the_site_been_cleared = db.Column(db.Text)
    Lead_time_for_clearing = db.Column(db.Float)
    If_not_how_much_would_clearing_and_grading_cost = db.Column(db.Float)
    Ground_water_level_ie_per_water_table = db.Column(db.Float)
    Soil_bearing_capacity = db.Column(db.Float)
    Does_the_site_have_any_wetlands_or_streams = db.Column(db.Text)
    Has_the_soil_clay_layers = db.Column(db.Float)
    What_is_the_PI_Index_of_the_soil = db.Column(db.Float)
    Is_the_site_located_near_a_flood_plain = db.Column(db.Text)
    In_which_seismic_zone_is_the_site_located = db.Column(db.Text)
    In_which_hurricane_zone_is_the_site_loacted = db.Column(db.Float)
    What_is_the_wind_load_zone_for_the_site = db.Column(db.Text)
    No_contamination_or_pollution_on_the_site = db.Column(db.Text)
    No_endangering_due_to_radioactive_radiation = db.Column(db.Text)
    No_rocky_ground = db.Column(db.Text)
    Fracking_activities_around_the_site_50_miles_radius = db.Column(db.Text)
    PERMITS = db.Column(db.Float)
    Existing_environmental_audit__Phase_1_report = db.Column(db.Text)
    Existing_archaeological_audit = db.Column(db.Text)
    Lead_time_for_environmental_permitting = db.Column(db.Float)
    Lead_time_for_archaeological_permitting = db.Column(db.Float)
    Lead_time_for_air_permitting = db.Column(db.Text)
    Is_site_located_in_an_attainment_or_non_attainment_area = db.Column(db.Text)



t_sqlite_sequence = db.Table(
    'sqlite_sequence',
    db.Column('name', db.NullType),
    db.Column('seq', db.NullType)
)
