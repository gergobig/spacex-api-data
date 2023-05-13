SELECT DISTINCT year || '-' || LPAD(month::text, 2, '0') AS launch_date FROM (
    SELECT
        EXTRACT(YEAR FROM TO_DATE(date_utc, 'YYYY-MM-DD')) AS "year",
        EXTRACT(MONTH FROM TO_DATE(date_utc, 'YYYY-MM-DD')) AS "month"
    FROM api
    GROUP BY 1, 2
    HAVING COUNT(*) > 1
) AS more_than_one_launch
ORDER BY 1 DESC;
