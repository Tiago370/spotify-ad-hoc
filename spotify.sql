CREATE TABLE artist(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    followers int NOT NULL,
    popularity smallint NOT NULL,
    img VARCHAR(64) NOT NULL
);

CREATE TABLE artist_genres(
    id_artist varchar(22),
    genre varchar(100),
    CONSTRAINT pk_genre PRIMARY KEY (id_artist, genre),
    CONSTRAINT id_fk FOREIGN KEY(id_artist) REFERENCES artist(id)
);

CREATE TABLE album(
    id VARCHAR(22) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    qtd_artists smallint NOT NULL,
    qtd_tracks smallint NOT NULL,
    img VARCHAR(64) NOT NULL
);

CREATE TABLE artist_album(
    id_artist VARCHAR(22),
    id_album VARCHAR(22),
    main_artist BOOLEAN,
    CONSTRAINT fk_artist FOREIGN KEY(id_artist) REFERENCES artist(id),
    CONSTRAINT fk_album FOREIGN KEY (id_album) REFERENCES album(id),
    CONSTRAINT pk_artistAlbum PRIMARY KEY (id_artist, id_album)
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

CREATE TABLE artist_track(
    id_artist VARCHAR(22),
    id_track VARCHAR(22),
    main_artist BOOLEAN,
    CONSTRAINT fk_artist FOREIGN KEY(id_artist) REFERENCES artist(id),
    CONSTRAINT fk_track FOREIGN KEY (id_track) REFERENCES track(id),
    CONSTRAINT pk_artistTrack PRIMARY KEY (id_artist, id_track)
);