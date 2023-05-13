SELECT
    (element ->> 'core')::text AS core,
    SUM((element ->> 'flight')::integer) AS flight_number
FROM public.api,
    JSON_ARRAY_ELEMENTS(ARRAY_TO_JSON(cores)) AS element
WHERE (element ->> 'core') IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
