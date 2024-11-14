import pyspark.sql.functions as F
from sedona.spark import SedonaContext

if __name__ == '__main__':

    """ Create Sedona spark session """
    config = SedonaContext.builder() \
        .config("spark.driver.memory", "15g") \
        .config('spark.jars.packages',
                ",".join(["org.elasticsearch:elasticsearch-hadoop:7.7.1",
                          "org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.6.1",
                          "org.datasyslab:geotools-wrapper:1.6.1-28.2"])) \
        .master("local[8]") \
        .appName('spark_ais_tutorial') \
        .getOrCreate()
    spark = SedonaContext.create(config)

    """ Create point geometry and unique identifier """
    ais_df = spark.read.option("header", True).option("inferSchema", True).csv("tutorials/ais/data/ais_data_sample.csv")

    ais_df = (ais_df
              .withColumn("point_geom", F.expr(f"ST_AsText(ST_Point(Longitude, Latitude))"))
              .withColumn("unique_id", F.concat(F.col("MMSI"), F.lit("_"), F.col("Timestamp")))
              )

    ais_df.write.mode("overwrite").json("tutorials/ais/data/ais_data_sample.json")

    print("AIS Data stored in NDJSON at: tutorials/ais/data/ais_data_sample.json")

