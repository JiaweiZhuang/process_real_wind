# Process & simplify real-world wind data

Data description: http://wiki.seas.harvard.edu/geos-chem/index.php/List_of_GEOS-FP_met_fields

Raw data can be downloaded by (will charge a few cents):

    aws s3 cp --request-payer=requester s3://gcgrid/GEOS_4x5/GEOS_FP/2016/07/GEOSFP.20160701.A3dyn.4x5.nc ./
    aws s3 cp --request-payer=requester s3://gcgrid/GEOS_4x5/GEOS_FP/2016/07/GEOSFP.20160701.I3.4x5.nc ./
    aws s3 cp --request-payer=requester s3://gcgrid/GEOS_0.25x0.3125/GEOS_FP/2016/07/GEOSFP.20160701.A3dyn.025x03125.nc ./
    aws s3 cp --request-payer=requester s3://gcgrid/GEOS_0.25x0.3125/GEOS_FP/2016/07/GEOSFP.20160701.I3.025x03125.nc ./
