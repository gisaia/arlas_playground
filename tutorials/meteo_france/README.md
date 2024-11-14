# Météo France Climatological data

## Prerequisites

Check the prerequisites [here](../../README.md).

## Introduction

The data are provided by [Météo France](https://meteo.data.gouv.fr/datasets/6569b51ae64326786e4e8e1a):

***Climatological data from all stations in mainland France and overseas since their opening, for all available parameters. These data have been climatologically checked.***

## Get in the right place

```shell
cd meteo_france
```

## Get the data

```shell
curl https://object.files.data.gouv.fr/meteofrance/data/synchro_ftp/BASE/QUOT/Q_31_previous-1950-2022_RR-T-Vent.csv.gz \
    -o Q_31_previous-1950-2022_RR-T-Vent.csv.gz
gunzip Q_31_previous-1950-2022_RR-T-Vent.csv.gz
```

## Transform the data

```shell
csvjson Q_31_previous-1950-2022_RR-T-Vent.csv -u 3 -d ";" --stream \
    --lat LAT --lon LON \
    | jq -c -M '.properties.ALTI=(.properties.ALTI|tonumber)' \
    | jq -c -M 'if .properties.RR? then .properties.RR=(.properties.RR|tonumber)else . end' \
    | jq -c -M 'if .properties.QRR? then .properties.QRR=(.properties.QRR|tonumber)else . end' \
    | jq -c -M 'if .properties.TN? then .properties.TN=(.properties.TN|tonumber)else . end' \
    | jq -c -M 'if .properties.TX? then .properties.TX=(.properties.TX|tonumber)else . end' \
    | jq -c -M 'if .properties.TM? then .properties.TM=(.properties.TM|tonumber)else . end' \
    | jq -c -M 'if .properties.TM? then .properties.has_TM=true else .properties.has_TM=false end' \
    | jq -c -M 'if .properties.TAMPLI? then .properties.TAMPLI=(.properties.TAMPLI|tonumber)else . end' \
    | jq -c -M 'if .properties.FFM? then .properties.FFM=(.properties.FFM|tonumber)else . end' \
    | jq -c -M 'if .properties.FFM? then .properties.has_FFM=true else .properties.has_FFM=false end' \
    | jq -c -M 'if .properties.DXY? then .properties.DXY=(.properties.DXY|tonumber)else . end' \
    | jq -c -M '.properties.id=input_line_number' \
    > Q_31_previous-1950-2022_RR-T-Vent.ndjson
```

Note: with `csvjson`, we use `--lat` and `--lon` in order to create a geojson geometry node. Also, we apply `tonumber` to the fieldslike `ALTI`, `RR` or `QRR` so that they are json numbers instead of strings. Finally, we create boolean fields like `has_TM` to tell whether the field (here `FF2M`) is provided or not.

```shell
 wc -l Q_31_previous-1950-2022_RR-T-Vent.ndjson
```
should confirm that we have 876 233 lines.

### Format

Thanks to csvkit, the format is geojson in new line delimeter (NDJON) format. The structure of an entry looks lilke this:

```json
{
  "type": "Feature", 
  "properties": {
    "NUM_POSTE": "31011001", 
    "NOM_USUEL": "ARBAS", 
    "ALTI": 405, 
    "AAAAMMJJ": "19680306",
    "RR": 9.0, 
    "QRR": 1
  }, 
  "geometry": {
    "type": "Point", 
    "coordinates": [0.908833, 42.9965]
  }
}
```

## Index the data

Before indexing the data, we need to create and reference the mapping. It's very easy with `arlas_cli`:

```shell
arlas_cli indices \
    --config local \
    mapping Q_31_previous-1950-2022_RR-T-Vent.ndjson \
    --nb-lines 100 \
    --field-mapping properties.AAAAMMJJ:date-yyyyMMdd \
    --nb-lines 50000 \
    --push-on weather_station_measure
```

Note: we use `--field-mapping properties.AAAAMMJJ:date-yyyyMMdd` to set the type of the field as `date` and to provide the date format (`yyyyMMdd`).

It is good to check the mapping is ok:
```shell
arlas_cli indices \
    --config local \
    describe weather_station_measure
```

We can now index the data in `weather_station_measure`:
```shell
arlas_cli indices \
    --config local \
    data weather_station_measure \
    Q_31_previous-1950-2022_RR-T-Vent.ndjson
```

Let's check how the data look like:
```shell
arlas_cli indices \
    --config local \
    sample weather_station_measure 
```

And the number of entries:
```shell
arlas_cli indices \
    --config local \
    list
```

We can now create an ARLAS collection:
```shell
arlas_cli collections \
    --config local \
    create weather_station_measure \
    --index weather_station_measure \
    --display-name "Weather Station Measures" \
    --centroid-path geometry \
    --geometry-path geometry \
    --date-path properties.AAAAMMJJ \
    --id-path properties.id
```

And the number of entries:
```shell
arlas_cli collections \
    --config local \
    describe weather_station_measure
```

Add a dashboard

```shell
arlas_cli persist 
    --config local \
    add dashboard.json config.json --name weather
```

It's now available on arlas: http://localhost/hub/
