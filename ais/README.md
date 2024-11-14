# ARLAS-stack-ais-tutorial

## About this tutorial
### What will you learn ?
With this tutorial, you'll be able to:

- Start an ARLAS-Exploration stack locally
- Index some AIS data in Elasticsearch
- Reference the indexed AIS data in ARLAS
- Create a view of ARLAS-wui (a dashboard) to explore the AIS data using ARLAS-wui-hub and ARLAS-wui-builder

### What will you need ?

You will need :

- python
- curl
- arlas_cli (See [project README.md](../README.md))
- ARLAS Exploration stack up and running (See [project README.md](../README.md))

<br />

### What will you get ?

<br />
<p align="center">
    <img src="./images/29_ais_arlas_wui_widget.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
 Exploration app created in this tutorial
</p>

## AIS data

Let's explore some boats position data, provided by __Danish Maritime Authority__ on their [website](https://www.dma.dk/SikkerhedTilSoes/Sejladsinformation/AIS/Sider/default.aspx).

This tutorial is based on AIS data emitted from 11/20/2019 to 11/27/2019. We extracted boats positions having the following MMSI :

 - 257653000
 - 265177000
 - 220051000
 - 240305000
 
We built a subset named `ais_data_sample.csv`. It contains around 162192 boats positions described with 26 columns.

Example of some columns:

- Timestamp: Moment when the position is emitted
- MMSI: Identifier of the boats emitter
- Name: Name of the boat
- Ship type: Type of the boat

A line of the csv file looks like:

|Timestamp|Type of mobile|MMSI|Latitude|Longitude|Navigational status|ROT|SOG|COG|Heading|IMO|Callsign|Name|Ship type|Cargo type|Width|Length|Type of position fixing device|Draught|Destination|ETA|Data source type|A|B|C|D|  
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|20/11/2019 06:45:09|Class A|240305000|55.931783|17.345067|Under way using engine|0.0|10.5|257.0|259|9288710|SYEF|DELTA CAPTAIN|Tanker|""|44|249|GPS|10.0|FOR ORDERS|22/11/2019 06:00:00|AIS|216|33|22|22|

## Add AIS data in ARLAS

We will explore this data using ARLAS.

- Check that `ais_data_sample.csv` file is downloaded

```shell
ls -l ais/data/ais_data_sample.csv
```

__1. Prepare AIS data__

Apply basic transformations with a python scripts before ingesting the data.

```shell
python3.10 ais/prepare_ais_data.py
```

Here the script create the points wkt geometry and a unique identifier and write the data in an NDJson file (`ais/data/ais_data_sample.json`). 
The script can be edited to enrich the data before the exploration.

__2. Indexing AIS data in Elasticsearch__

- Create an empty `ais_geopoints` index in Elasticsearch with inferred mapping

```shell
arlas_cli indices \
    --config local \
    mapping ais/data/ais_data_sample.json/part-00000-*.json \
    --no-fulltext unique_id \
    --field-mapping MMSI:keyword \
    --field-mapping Timestamp:date-"dd/MM/yyyy HH:mm:ss" \
    --push-on ais_geopoints
```

- Index data that is in `ais_data_sample.json` in Elasticsearch with `arlas_cli`
```shell
arlas_cli indices \
    --config local \
    data ais_geopoints ais/data/ais_data_sample.json/*.json
```

- Check if __162189__ AIS positions are available in the `ais_geopoints` index:

```shell
arlas_cli indices --config local list
```

__3. Declaring `ais_geopoints` collection in ARLAS__

ARLAS-server interfaces with data indexed in Elasticsearch via a collection reference.

The collection references an identifier, a timestamp, and geographical fields which allows ARLAS-server to perform a spatial-temporal data analysis


- Create the `tuto_ais_geopoint` collection in ARLAS

```shell
arlas_cli collections \
    --config local \
    create tuto_ais_geopoint \
    --index ais_geopoints \
    --display-name "AIS Geopoints" \
    --id-path unique_id \
    --centroid-path point_geom \
    --geometry-path point_geom \
    --date-path Timestamp
```

- Check that the collection is created:

```shell
arlas_cli collections --config local list
```

__4. Create a dashboard to explore `AIS data` with ARLAS__

ARLAS stack is up and running and we have ais position data available for exploration. We can now create our first dashboard composed of
- A map to observe the boats positions' geographical distribution
- A timeline presenting the number of boats positions over time
- A search bar to look for boats by their names for instance
- Some widgets to analyse the data from another axis such as the speed distribution.

To do so, let's go to [ARLAS-wui-hub](http://localhost:81/hub) and create a new dashboard named `Boats dashboard`

<p align="center">
    <img src="./images/0_ais_create_dashboard.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 0: Creation of a dashboard in ARLAS-wui-hub
</p>
<br />

After clicking on __Create__, you are automatically redirected to ARLAS-wui-builder to start configuring your dashboard.

### Choosing the collection

The first thing we need to do is to tell ARLAS which collection of data we want to use to create our dashboard

<p align="center">
    <img src="./images/1_ais_choose_collection.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 1: Choose collection
</p>
<br />

in our case we choose the `tuto_ais_geopoint`

### Map configuration

As a first step, I'll set the map at zoom level 13 and the map's center coordinates at Latitude=57,451545 and Longitude=10,787131. This way, when loading my dashboard in ARLAS-wui, the map will be positionned over Danmark.

<p align="center">
    <img src="./images/2_ais_global_map.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 2: Map initialisation
</p>
<br />

For now, the map is empty. The first thing we want to find out is where the boats are ?

<p align="center">
    <img src="./images/3_ais_layer_view.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 3: Layer view
</p>
<br />

To do so, let's add a layer named `Boats` to visualise the boats positions.
In the Geometry section, choose the `point_geom` features geo-field

<p align="center">
    <img src="./images/4_ais_geometric_features_geom.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 4: Adding a Geometric features layer named 'Boats'
</p>
<br />

Now, let's define the layer's style. As a starter, we choose the best representation of our geometries: Boats positions are points. We also choose a fixed color (green for instance) and a fixed radius of 4 pixels

<p align="center">
    <img src="./images/5_ais_geometric_features_style.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 5: Customising 'Boats' style
</p>
<br />

After clicking on Validate, our first layer is created

<p align="center">
    <img src="./images/6_ais_boats_layer.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 6:  New layer 'Boats' is created
</p>
<br />

We can go and preview the layer in Preview tab

<p align="center">
    <img src="./images/7_ais_boats_layer_preview.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 7:  Preview of 'Boats' layer
</p>
<br />

We see now where the boats are passing by thanks to this layer
<br />
<br />

### Timeline configuration
Let's find out the time period when these positions were emitted.

For that, let's define a timeline: a histogram that will represent the number of boats positions over time.

For the x-Axis we choose the timestamp field and for the y-Axis we choose Hits count: the number of positions in each bucket. We set 50 buckets in this example

<p align="center">
    <img src="./images/8_ais_timeline_data.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 8:  Define timeline
</p>
<br />

In the Render tab we can set a title for the timeline, date format and the histogram type.

<p align="center">
    <img src="./images/9_ais_timeline_render.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 9:  Rendering of timeline
</p>
<br />
<br />

### Search Bar configuration

To define the search bar we can set :

 - the placeholder string;
 - the field used to seach keywords
 - the field used to autocomplete the searched words

<p align="center">
    <img src="./images/10_ais_search.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 10:  Define search bar
</p>
<br />
<br />


### Save the dashboard and start exploring in ARLAS-wui

Now we defined :

 - 'Boats' layer in the map
 - the timeline 
 - the search bar

Let's save this dashboard by clicking on the 'Disk' icon at the left-bottom of the page.

If we go back to [ARLAS-wui-hub](http://localhost:8094/), we'll find the Boats dashboard created.

<p align="center">
    <img src="./images/11_ais_dashboard_list.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 11:  List of created dashboards
</p>
<br />

We can now __View__ it in [ARLAS-wui](http://localhost:81/wui)
<p align="center">
    <img src="./images/12_ais_arlas_wui.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 12:  Visualize in ARLAS-wui
</p>
<br />


### Geo Big Data
For this tutorial, we only have ~160 000 boats positions to explore. This allowed us to display the boats positions directly on the map.

But what to do in case we had millions of positions to display ?

It would be very difficult to display them all as it would be very heavy to request all that data at once and the browser will not be able to render as many features. We will end up loosing the user experience fluidity.

Most importantly, loading millions of boats positions on the map will not be necessarily understandable: we cannot derive clear and synthesized information from it.

That's why ARLAS proposes a geo-analytic view: we can aggregate the boats positions to a geographical grid and obtain a geographical distribution !

Let's create a dedicated layer for boats positions geographical distribution.
<p align="center">
    <img src="./images/21_ais_distribution_layer.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 21: Creating a geographical distribution layer
</p>
<br />

We choose to aggregate `point_geom` geo-field to a geographical H3 grid and we choose a fine granularity for this grid.

We will display on the map the grid's cells.

Let's define the style of these cells in `Style` section
<p align="center">
    <img src="./images/22_ais_distribution_layer_style.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 13: Creating a geographical distribution layer
</p>
<br />

We interpolate the cells colors to the number of boats positions in each cell. That's why we choose Hits count that we normalise and choose a color palette

After saving this layer, we can again visualise it and explore where the positions are geographically
<p align="center">
    <img src="./images/23_ais_distribution_layer_preview.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 14: Boats positions geographical distribution
</p>
<br />

### Analytics board
We focused on the geographical and temporal analysis. We can also explore other dimensions of the data.

Let's see what does the heading distribution of these positions looks like.

To do so we need to create a histogram. ARLAS proposes to organise all the histograms and other widgets in an analytics board.

We can split the analytics board into tabs. Let's create a tab called 'Tracking' where will add our Heading distribution histogram
<p align="center">
    <img src="./images/24_ais_tracking_tab.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 15: Creating tab in Analytics board
</p>
<br />

Once the tab is created, we can add in it a group of widgets. Let's name it 'Heading'
<p align="center">
    <img src="./images/25_ais_heading_group.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 16: Creating a group in Analytics board tab
</p>
<br />

Let's now create our histogram
<p align="center">
    <img src="./images/26_ais_histogram.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 17: Choosing a histogram for heading distribution
</p>
<br />

We can give a title to the Heading distribution histogram

For the x-Axis we choose `Heading` field and for the y-Axis we choose `Hits count`: the number of positions in each bucket. 

<p align="center">
    <img src="./images/27_ais_histogram_data.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 18: Defining heading distribution histogram
</p>
<br />

When we save the histogram we automatically get a preview of it in the analytics board!
<p align="center">
    <img src="./images/28_ais_histogram_preview.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 19: Preview heading distribution histogram
</p>
<br />

We can now save the dashboard again using the 'Disk' icon at the left-bottom of the page and view it ARLAS-wui
<p align="center">
    <img src="./images/29_ais_arlas_wui_widget.png" width="100%">
</p>
<p align="center" style="font-style: italic;" >
figure 20: Exploring Boats dashboard in ARLAS-wui
</p>
<br />
<br />
 
As you can see we created a simple dashboard to start exploring AIS data!

Check out a more sophisticated dashboard about the AIS data [demo space](https://demo.cloud.arlas.io/arlas/wui/?config_id=Rnbr4k634bkw8RxkOCbb&extend=-0.5108640078143765,52.476089090578085,19.846802007810794,58.54532820589935)!

You can get inspired from our different [demos](https://demo.cloud.arlas.io/) to build other map layers and other widgets.