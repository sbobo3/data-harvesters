/*SeasonStartDate must be less than SeasonEndDate*/

/*Season1*/
SELECT FMID, Season1StartDate, Season1EndDate
FROM Farmers_Market
WHERE Season1StartDate > Season1EndDate

/*Season2*/
SELECT FMID, Season2StartDate, Season2EndDate
FROM Farmers_Market
WHERE Season2StartDate > Season2EndDate

/*Season3*/
SELECT FMID, Season3StartDate, Season3EndDate
FROM Farmers_Market
WHERE Season3StartDate > Season3EndDate

/*Season4*/
SELECT FMID, Season4StartDate, Season4EndDate
FROM Farmers_Market
WHERE Season4StartDate > Season4EndDate