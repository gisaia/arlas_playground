# OSM and phtovoltaic data

## Prerequisites

Check the prerequisites [here](../README.md).

## Introduction

The OSM data is provided by [GeoFabrik's](https://download.geofabrik.de/europe/france/languedoc-roussillon.html) regional download, the French administrative data by the [IGN](https://geoservices.ign.fr/adminexpress) and the photovoltaic potential data by [Solargis](https://solargis.com/resources/free-maps-and-gis-data?locality=france).

## Get in the right place

```shell
cd meteo_france
```

## Get the data

All the necessary data is stored in the Gisaïa bucket, and can be downloaded with:
```shell
export ARLAS_DEMO_REMOTE_DATA_PATH="gs://gisaia-public/demo"
export ARLAS_DEMO_LOCAL_DATA_PATH="${PWD}/data"
python download_raw_data.py
```

The path `ARLAS_DEMO_LOCAL_DATA_PATH` can be changed to any path of your liking.

## Transform the data

To transform the data, a notebook is available to cross the data sources.

## Ingest data in ARLAS demo

### Create empty index with correct mapping

Infer mapping directly from the data:

```
arlas_cli indices \
    --config local \
    mapping ${ARLAS_DEMO_LOCAL_DATA_PATH}/sunny_osm/osm_sunny.json/part-00000-*.json \
    --no-fulltext osm_id \
    --no-fulltext month \
    --no-fulltext unique_id \
    --no-fulltext name \
    --field-mapping time:date-epoch_second \
    --nb-lines 1000 \
    --push-on sunny_osm

```
### Index data

To index the object data created in `sunny_osm/osm_sunny.json`, run:
```
arlas_cli indices \
    --config local  \
    data sunny_osm \
    ${ARLAS_DEMO_LOCAL_DATA_PATH}/sunny_osm/osm_sunny.json/*.json
```

### Delete index

If you want to delete the index, run:
```
arlas_cli indices \
    --config local-admin \
    delete sunny_osm
```
Before reindexing data, don't forget to [recreate empty index with mapping](#create-empty-index-with-correct-mapping).

### Create collection

To create the ARLAS collection, run:
```
arlas_cli collections \
    --config local \
    create sunny_osm \
    --index sunny_osm \
    --display-name "Sunny OSM" \
    --centroid-path centroid \
    --geometry-path geometry \
    --date-path time \
    --id-path unique_id
```

### Push the dashboard

```
arlas_cli persist
    --config local \
    add dashboard.json config.json --name "Sunny OSM"
```