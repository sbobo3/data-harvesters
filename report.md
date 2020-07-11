# CS 513 Final Project - Farmer's Market

## Authors

* Alex Antonison (ada4)
* Andrew Vojak (vojak1)
* Steven Bobo (sbobo3)

## Introduction

The Data Harvester's final project involved cleaning a Farmer's Market dataset.  The Farmer's Market data was downloaded from [https://www.ams.usda.gov/local-food-directories/farmersmarkets](https://www.ams.usda.gov/local-food-directories/farmersmarkets).  The Farmers Market Directory is a list that notes instances where two or more farm vendors are selling products to customers at a consistent location.

The primary goal of this project for Data Harvester's is to understand, clean, and enhance the data to help people be able to find Farmer's Markets that suit their needs.  With this, Data Harvester's will make the process of cleaning and preparing the data automated to ensure that when future Farmer's Markets are added to the dataset, they can be automatically processed.

## Initial Assessment

### Dataset Structure and Quality Assessment

//  You should describe the structure and content of the dataset and quality issues that are apparent from an initial inspection.

The Farmer's Market data is 8,687 records with 59 columns.  Each record in the dataset represents a different farmer's market location.  

* Farmers Market Name and Identifiers
  * Each farmer's market is uniquely identifiable with the `FMID` that is a number.  
  * The `MarketName` column is a more user friendly method of identifying a Farmers Market, however there are instances where numerous Farmers Markets can have the same name but are not related, an example being "Livingston Farmers Market" which exists in 5 different states.
  * These columns are always filled out which is to be expected.
* Online Information
  * There are numerous fields to capture different types of digital media such as a `website`, `facebook`, `twitter`, `youtube`, as well as an `OtherMedia` column.
  * These columns have a lot of blanks.  While the website column is 59% full and the Facebook column is 45% populated; twitter, youtube, and OtherMedia are mostly empty at below 15% populated.
  * For the Facebook column, it is a combination of links and names.
* Location Information
  * The location information across `street`, `city`, `County`, `State`, and `zip` all have high fill rates with the lowest being `zip` at 89%.
  * When evaluating `street`, most instances an address is provided but there are a handful of instances where common names such as `Main Street` are used.
  * The `x` and `y` columns represent latitude and longitude and are populated 99% of the time.
  * There is a `Location` column that indicates the type of location such as a "Private business parking lot" or "Local government building grounds."
* Seasonal Availability
  * Although there are four locations for a farmers market to specify date and time, it is rare for a farmers market to specify more than one.  It is worth noting that even the first section of noting what season a farmers market is available is only populated about 65% of the time. This would be an opportunity to work with farmers markets to better populate their availability to better inform the general public of when they are open.
* Accept forms of Payment
  * In these columns, `Credit`, `WIC`, `WICcash`, `SFMNP`, and `SNAP`, it indicates what forms of payment a farmers market will accept.  Whether it be a credit card or various government assisted programs.
  * As to be expected, all of these columns are 100% populated.
* Type of Goods Sold
  * The following 30 columns are a series of flags that indicate what kind of goods are sold at the farmers market ranging from organic to kinds of meats.
  * Although the `Organic` column is 100% populated, all of the other columns are around 66% populated.
* Record Metadata
  * There is an `updateTime` column that appears to for the most part has a date timestamp but around 30% of the time only has a year for 2009, 2011, and 2013.

### Use Cases

// You should also describe a (hypothetical or real) use case of the dataset and derive from it some data cleaning goals that can achieve the desired fitness for use.

The farmers market dataset can be used by people interested in finding farmers markets close to them to either purchase or sell items.  To help with this, we have the following data cleaning goals:

* Cleanse up the online information columns to ensure it is easier for people find information about farmers markets close to them.  Additionally, to ensure future consistency, put data validation checks in place to for properly entered hyperlinks to online content.
* Transform the Seasonal Availability columns to help make it easier to determine when farmers markets are open.
* Transform the updateTime to be a consistent date timestamp.
* Cleanse the location information to ensure that only valid information is entered in each field.

// Additionally

// Are there use cases for which the dataset is already clean enough?

The farmers market data as it currently is does provide useful information to people seeking farmers markets.  However, there are numerous instances where the data entered is malformed and would require a person to interpret the entered information about a farmers market.  

// Are there use cases for which the dataset will not be clean enough?

As there are parts of the dataset that predominantly blank, it would be difficult to perform a comprehensive analysis on aspects of farmers markets like goods sold, online presence, and seasonal availability.

## Data Cleansing

// Document the process and result of this phase, both in narrative form along with supplementary information (e.g., which columns were cleaned and what changes were made?).

* Farmers Market Name and Identifiers
  * No work needs to be done regarding the `FMID` as each record is unique.
  * No work needs to be done regarding `MarketName` since even though there are instances where a farmers market has a duplicate name, the additional information provided in a record provides enough context to identify the correct farmers market.
* Online Information
  * For Facebook, I am removing all invalid instances of Facebook groups using the following GREL and creating a column `Facebook_Link`:

        if(value.contains("facebook.com"), value, "")

  * For Twitter, I am removing all invalid instances of Twitter users using the following GREL and creating a column `Twitter_Link`: 

        if(value.contains("twitter.com"), value, "")

  * For Youtube, I am removing all invalid instances of Youtube users using the following GREL and creating a column `Youtube_Link`: 

        if(value.contains("youtube.com"), value, "")

  * For OtherMedia, I am removing all instances where an invalid website link was provided and created a column OtherMedia_Link:

        if(
          length(
            value.find(/^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/)) 
          >= 1, 
          value, "")

* Location Information
* Seasonal Availability
* Accepted forms of Payment
* Type of Goods Sold
* Record Metadata

// Can you quantify the results of your efforts? Also, provide provenance information from OpenRefine. Pay close attention to what OpenRefine includes and does not include in its operation history!

// If important information is missing in the latter, provide that information in narrative form.
