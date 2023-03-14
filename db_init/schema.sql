CREATE TABLE IF NOT EXISTS res_it (

    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
	name STRING NOT NULL,
	title STRING,
	startdate STRING,
	enddate STRING,
	content STRING,
	type STRING NOT NULL
);
