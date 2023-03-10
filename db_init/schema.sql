DROP TABLE IF EXISTS res_it;

CREATE TABLE res_it (
	id UUID PRIMARY KEY,
	name TEXT NOT NULL,
	title TEXT,
	start TEXT,
	end TEXT,
	content TEXT,
	type TEXT NOT NULL
)
