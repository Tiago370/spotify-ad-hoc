CREATE TABLE artist(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    followers int NOT NULL,
    popularity smallint NOT NULL,
    img VARCHAR(64) NOT NULL
);

CREATE TABLE album(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    qtd_artists smallint NOT NULL,
    qtd_tracks smallint NOT NULL,
    img VARCHAR(64) NOT NULL
);

CREATE TABLE track(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    duration int NOT NULL,
    explicit BOOLEAN NOT NULL,
    track_number smallint NOT NULL,
    qtd_artistas smallint NOT NULL,
    album_id VARCHAR(22) NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album (id)
);


CREATE TABLE artist_genres(
    artist_id VARCHAR(22) NOT NULL,
    name VARCHAR(100) NOT NULL,
    CONSTRAINT pk_AA primary key (artist_id, album_id),
    FOREIGN KEY (album_id) REFERENCES album (id)
);


-- SELECT * FROM album;
-- INSERT INTO album(id, name, release_date, qtd_artists, img)
-- VALUES('76N6imyjQ9h5p2NzakHT32', 'M.I.A.M.I.', '2004-08-03', 1, 'ab67616d0000b27300650b5e6be3af579ae18e7c');


-- SELECT * FROM track;
CREATE TABLE artist_album(
    artist_id VARCHAR(22) NOT NULL,
    album_id VARCHAR(22) NOT NULL,
    main_artist BOOLEAN NOT NULL,
    CONSTRAINT pk_AA primary key(artist_id, album_id)
);
-- SELECT * FROM artist_album;
