/*All FMIDs must be unique*/

SELECT FMID, COUNT(*)
FROM Farmers_Market
GROUP BY FMID
HAVING COUNT(*)>1;