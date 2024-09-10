--Following tutorial found in
--https://www.youtube.com/watch?v=zw4s3Ey8ayo

--To display the version of the database
SELECT VERSION();

--Added IF NOT EXISTS to keep this 
--uncommented
CREATE TABLE IF NOT EXISTS profile(
	id SERIAL PRIMARY KEY
	--AUTOMATICALLY INCREMENTS
	--A UNIQUE IDENTIFIER
	, 
	name VARCHAR(255) ---- VARCHAR
	--= TEXT HAS CONSTRAINT ON SIZE
	, 
	email VARCHAR(255),
	password TEXT --Never store
	--password directly, THIS IS 
	--HASHED
	,
	age INT
);

--Quote since user is a keyword
CREATE TABLE IF NOT EXISTS "user"(
	id SERIAL PRIMARY KEY, 
	name VARCHAR(255), 
	email VARCHAR(255) UNIQUE,
	password TEXT,
	age INT
);

SELECT * FROM profile;

INSERT INTO "user" (email, name, 
age, password) VALUES (
'edwin@fake.email',
'edwin',
21,
'hashedpassword'
) ON CONFLICT (email) DO UPDATE SET
name='edwin',
age=21,
password='hashedpassword';

INSERT INTO "user" (email, name,
age, password) VALUES (
'sophia@fake.email',
'sophia',
16,
'anotherhashedpassword'
)
ON CONFLICT (email) DO UPDATE SET
name = 'sophia',
age=16,
password='anotherhashedpassword';

SELECT * FROM "user" WHERE age > 13;

SELECT * FROM "user" WHERE age > 13;

INSERT INTO "user" (
name, email, age, password
) VALUES 
(
'Kamau',
'kamau@fakeemail',
26,
'YetAnotherHashPassword'
) ON CONFLICT (email) DO UPDATE SET
name='Kamau',
age=26,
password='YetAnotherHashPassword';

SELECT * FROM "user";

--How about removing
DELETE FROM "user" WHERE name='Kamau';

SELECT name FROM "user";


--Table relationships
--There are one-one, one-many, 
--many-many
--
--one-one: avatar_id in user table 
--related to user_id in avatar table
--
--one-to-many
--A post table has a user_id column,
--which can be used to find id in 
--user table
--
--Many-to-many
--A subscriber table has two columns
--subscribed_by related to user table
--subscribed_to relates to YouTuber table
--Basically two one-to-manys

--Table with foreign key
DELETE FROM post;
CREATE TABLE IF NOT EXISTS post(
id SERIAL PRIMARY KEY,
NAME VARCHAR(255),
content TEXT,
user_id INT,
CONSTRAINT fk_user
	FOREIGN KEY(user_id)
		references "user"(id)
);

SELECT * FROM post;

INSERT INTO post (name, content, user_id)
VALUES ('Nakipenda Kiswahili', 
'lugha za mataifa ya Afrika 
Mashariki', 1);

SELECT * FROM post;

INSERT INTO post (name, content, 
user_id)
VALUES
('Methali ya baba', 
'Mgaagaa na upwa hali wali mkavu',
1);

--Miswrote the text by accident, 
--let us update!
--Be careful of single quotes 
--"for text"
--vs double quotes (for columns)
UPDATE post SET 
content = 'Lugha kwa mataifa ya Afrika Mashariki!'
WHERE NAME = 'Nakipenda Kiswahili';

SELECT * FROM post;

--Let's get the user with their 
--id and post
SELECT "user".*, post.id AS post_id,
post.name AS title, post.content, 
post.user_id FROM "user" 
JOIN post ON
post.user_id = "user".id;