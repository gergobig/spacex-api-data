-- FACT TABLE
CREATE TABLE launches AS (SELECT
    id AS launch_id,
    success AS launch_success,
    launchpad AS launch_site_id,
    rocket AS rocket_id,
    to_date(date_utc, 'YYYY-MM-DD') AS launch_date,
    coalesce(array_length(payloads, 1), 0) AS payloads_count,
    coalesce(array_length(crew, 1), 0) AS crew_count
FROM api);
ALTER TABLE launches ADD PRIMARY KEY (launch_id);

-- DIMENSION TABLES

CREATE TABLE crew_members AS (
    SELECT
        id AS launch_id,
        crew_member ->> 'crew' AS crew_id,
        crew_member ->> 'role' AS "role"
    FROM api,
        json_array_elements(array_to_json(crew)) AS crew_member
);
ALTER TABLE crew_members ADD PRIMARY KEY (crew_id);
ALTER TABLE crew_members
ADD CONSTRAINT fk_launch_id
FOREIGN KEY (launch_id)
REFERENCES launches (launch_id);

CREATE TABLE rockets AS (
    SELECT
        rocket AS rocket_id,
        name AS rocket_name,
        min(to_date(date_utc, 'YYYY-MM-DD')) AS first_usage_date,
        max(to_date(date_utc, 'YYYY-MM-DD')) AS last_usage_date
    FROM api
    GROUP BY 1, 2
);
ALTER TABLE rockets ADD PRIMARY KEY (rocket_id, rocket_name);
