/*Latitude and longitude should match only one city*/

SELECT DISTINCT city, longitude || ' ' || latitude AS longitude_latitude
FROM Farmers_Market 
WHERE longitude_latitude IN 
(
SELECT longitude || ' ' || latitude AS longitude_latitude
FROM Farmers_Market
GROUP BY longitude_latitude
HAVING COUNT(*) > 1
) 
ORDER BY longitude_latitude