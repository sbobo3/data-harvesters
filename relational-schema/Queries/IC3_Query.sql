/*Season dates must be different*/

SELECT FMID, Season1Date, Season2Date, Season3Date, Season4Date
FROM Farmers_Market
WHERE Season1Date = Season2Date OR Season1Date = Season3Date OR Season1Date = Season4Date OR Season2Date = Season3Date OR Season2Date = Season4Date OR Season3Date = Season4Date
