DROP TABLE IF EXISTS res_it;

CREATE TABLE res_it (

    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
	name STRING NOT NULL,
	title STRING,
	start STRING,
	finish STRING,
	content STRING,
	type STRING NOT NULL
);