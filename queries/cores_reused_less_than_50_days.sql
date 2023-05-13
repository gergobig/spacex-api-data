WITH unpacked_core_id_with_launch_date AS (
    SELECT
        element ->> 'core'::text AS core,
        to_date(api.date_utc, 'YYYY-MM-DD') AS launch_date
    FROM api,
        json_array_elements(array_to_json(cores)) AS element
),

cores_reused_within_50_days AS (
    SELECT
        core,
        launch_date,
        lag(launch_date)
            OVER (PARTITION BY core ORDER BY launch_date)
        AS previous_launch_date
    FROM
        unpacked_core_id_with_launch_date
)

SELECT DISTINCT core
FROM
    cores_reused_within_50_days
WHERE
    launch_date - previous_launch_date <= 50
    AND core IS NOT NULL;
