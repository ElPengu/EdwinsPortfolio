--Create a user table
--A user has: id, username (unique), 
--password (hashed), email (unique),
--date_created, last_logged_in,
--name
CREATE TABLE IF NOT EXISTS "user"(
	id SERIAL PRIMARY KEY,
	username  VARCHAR(100) UNIQUE,
	password TEXT,
	email TEXT UNIQUE,
	date_created TIMESTAMP with time zone,
	last_logged_in TIMESTAMP,
	name VARCHAR(100)
);

--Test add user
INSERT INTO "user" (
username, password, email, 
date_created, 
last_logged_in, name
) VALUES (
'anayekulaMayai', 'hashedPwd', 
'Gaitho@fakeemail.com', NOW(), 
NOW(), 'Edwin Gaitho Nganga'
) 
ON CONFLICT (email) DO NOTHING;

SELECT * from "user";

INSERT INTO "user" (
username, password, email, 
date_created,
last_logged_in, name
) VALUES (
'mshindaji123', 'hashedPwd2',
'Nganga@fakeemail.com', NOW(),
NOW(), 'Nicholas Nganga Gaitho'
)
ON CONFLICT (email) DO NOTHING;

SELECT * FROM "user";

UPDATE "user" SET 
last_logged_in = NOW() 
WHERE email = 'Gaitho@fakeemail.com';

SELECT * FROM "user";