--Average Selling Price by Car Brand
SELECT c.brand, round(AVG(a.price::numeric)) AS average_price
FROM Cars c
JOIN Ads a ON c.car_id = a.car_id
GROUP BY c.brand
ORDER BY average_price DESC;

--Top 10 Users with the Most Ads Posted
SELECT u.user_id, u.username, COUNT(a.ads_id) AS total_ads
FROM Users u
JOIN Ads a ON u.user_id = a.user_id
GROUP BY u.user_id, u.username
ORDER BY total_ads DESC
LIMIT 10;

-- Top 5 Number of Bids Received Per Ad
SELECT a.ads_id, a.title,  COUNT(b.bid_id) AS NumberOfBids
FROM Ads a
LEFT JOIN Bids b ON a.ads_id = b.ads_id
GROUP BY a.ads_id
ORDER BY NumberOfBids desc
limit 10;

--Average Bid Price by Ad
SELECT a.ads_id, a.title, AVG(b.bid_price) AS average_bid_price
FROM Ads a
JOIN Bids b ON a.ads_id = b.ads_id
GROUP BY a.ads_id, a.title
ORDER BY average_bid_price DESC
LIMIT 10;

--Monthly user bid Trend
SELECT to_char(b.bid_date::date, 'mm-yyyy') AS Month, COUNT(b.bid_id) AS number_of_bid
FROM bids b 
GROUP BY to_char(b.bid_date::date, 'mm-yyyy')
ORDER BY Month;
