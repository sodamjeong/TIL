-- 문제 1
CREATE TABLE users (
	userid INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100) DEFAULT NULL,
    country VARCHAR(100) DEFAULT NULL,
    email VARCHAR(100) DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userid)
);

-- 문제 2
INSERT INTO
	users(first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01','','','beemo@hphk.kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', ''),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', ''),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', '');
-- 문제 3
INSERT INTO
	users(first_name, last_name, birthday, city, country, email)
VALUES
	('Tory', 'Jeong', '2014-09-14','Kyeonggi','Korea','mungmung@naver.com'),
    ('Cat', 'Kang', '2020-06-22', 'Seoul', 'Korea', 'miao@gmail.com'),
    ('Cow', 'Malang', '2008-08-28', 'Seoul', 'Korea', 'podong@podong.com'),
    ('Bunny', 'Bunny', '2011-03-02', 'Missouri', 'USA', 'kkang@chong.co.kr'),
	('person', 'Han', '0001-01-01', 'World', 'Earth', '');
-- 문제 4
UPDATE users
SET first_name = 'Sodam',
	last_name = 'Jeong',
	birthday = '1992-08-28'
WHERE userid = 2;

-- 문제 5
UPDATE users
SET country = 'Korea'
WHERE country = '';

-- 문제 6
DELETE FROM users
WHERE first_name = 'Beemo';

-- 문제 7
DELETE FROM users
WHERE first_name = 'Kwangsoo' AND last_name = 'Lee';

-- 문제 8
DELETE FROM users
ORDER BY created_at DESC,userid DESC
LIMIT 1;
