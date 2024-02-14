-- Select all the cities of California from the cities table
SELECT * FROM cities
WHERE state_id = (
    -- Subquery to get the id of California from the states table
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
