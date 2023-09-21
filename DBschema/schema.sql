CREATE TABLE IF NOT EXISTS "book" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT,
	"writer"	TEXT,
	"img"	TEXT,
	"price_books"	INTEGER,
	"link_books"	TEXT,
	"price_kingstone"	INTEGER,
	"link_kingstone"	TEXT,
	"price_sanmin"	INTEGER,
	"link_sanmin"	TEXT,
	"ranktimes"	INTEGER,
	"lowest_name"	TEXT,
	"lowest_price"	INTEGER
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"email"	TEXT
);
CREATE TABLE IF NOT EXISTS "hotbook" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT,
	"writer"	TEXT,
	"img"	TEXT,
	"price_books"	INTEGER,
	"link_books"	TEXT,
	"price_kingstone"	INTEGER,
	"link_kingstone"	TEXT,
	"price_sanmin"	INTEGER,
	"link_sanmin"	TEXT,
	"ranktimes"	INTEGER,
	"lowest_name"	TEXT,
	"lowest_price"	INTEGER
);
CREATE TABLE IF NOT EXISTS "newbook" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT,
	"writer"	TEXT,
	"img"	TEXT,
	"price_books"	INTEGER,
	"link_books"	TEXT,
	"price_kingstone"	INTEGER,
	"link_kingstone"	TEXT,
	"price_sanmin"	INTEGER,
	"link_sanmin"	TEXT,
	"ranktimes"	INTEGER,
	"lowest_name"	TEXT,
	"lowest_price"	INTEGER
);
