DROP TABLE IF EXISTS res_it;

CREATE TABLE res_it (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	title TEXT,
	start TEXT,
	end TEXT,
	content TEXT,
	type TEXT NOT NULL
)