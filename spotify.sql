CREATE TABLE artist(
	id VARCHAR(22) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	followers int NOT NULL,
	popularity smallint NOT NULL,
	img VARCHAR(40) NOT NULL
);
SELECT * FROM artist;
CREATE TABLE album(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    label VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    popularity smallint NOT NULL,
    img VARCHAR(40) NOT NULL
);
SELECT * FROM album;
CREATE TABLE track(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    duration int NOT NULL,
    explicit BOOLEAN NOT NULL,
    img VARCHAR(40) NOT NULL,
    track_number smallint NOT NULL,
    album_id VARCHAR(22) NOT NULL
);
SELECT * FROM track;
CREATE TABLE artist-album(
    artist_id VARCHAR(22) NOT NULL,
    album_id VARCHAR(22) NOT NULL,
    