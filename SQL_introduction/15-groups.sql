-- Counts records grouped by score, sorted by the count descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
