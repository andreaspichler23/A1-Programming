-- updating a table during runtime of the script with a join

ALTER TABLE shops_per_city ADD merchant_type DOUBLE;
/*ALTER TABLE shops_per_city ADD city_latitude DOUBLE*/

UPDATE shops_per_city AS shop
INNER JOIN city_list AS city
ON shop.city_id = city.city_id
SET shop.city_latitude = city.city_latitude;


-- selecting the list for a where statement with a subquery

SELECT * 
FROM shopstation
WHERE Dealer_ID_Long IN 
	(select Dealer_ID_Long
	FROM shop_list);
	
-- also possible to join on a subquery (notice that there is no ; in the subquery)
SELECT *, -- this select needs to have all columns of the result table
FROM shopcounter_category_daily_v2 AS shop
INNER JOIN 
	(SELECT *
	FROM weather_owm_daily_2014
	WHERE cityId = 2761369) AS weather
ON shop.RECORD_DATE = weather.DATE;

-- update a column using CASE
UPDATE creditcard_merchtype 
SET online =
	(CASE
    	WHEN Merchantname LIKE "%.at%" THEN 1
    	WHEN Merchantname LIKE "%.com%" THEN 1
    	ELSE 0
	END);
	
-- alter column name	
ALTER TABLE creditcard_at_v1 CHANGE cityId city_id INT;


-- creating temporary table for later use:

CREATE TEMPORARY TABLE id_list AS
SELECT COUNT(*) AS days, dealer_name, DEALER_ID, Dealer_ID_Long
FROM shopcounter
WHERE YEAR(RECORD_DATE) > 2017
GROUP BY dealer_name, DEALER_ID, Dealer_ID_Long
HAVING days > 752;

CREATE TABLE shopcounter_stable AS
SELECT *
FROM shopcounter
WHERE Dealer_ID_Long IN 
	(SELECT Dealer_ID_Long
	FROM id_list) && YEAR(RECORD_DATE) > 2017;
