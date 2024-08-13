DROP DATABASE IF EXISTS sonic_stream;

-- create the database of our app
CREATE DATABASE IF NOT EXISTS sonic_stream;
USE sonic_stream;

CREATE TABLE IF NOT EXISTS listener
(
    id INT PRIMARY KEY,
    username varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    location varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS friends
(
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    userID INT,
    friendID INT,
    PRIMARY KEY (userID, friendID),
    CONSTRAINT fk_01 FOREIGN KEY (userID) REFERENCES listener(id)
        ON UPDATE cascade,
    CONSTRAINT fk_02 FOREIGN KEY (friendID) REFERENCES listener(id)
        ON UPDATE cascade
);

CREATE TABLE IF NOT EXISTS concert
(
    id INT PRIMARY KEY,
    venue VARCHAR(60),
    event_date DATE
);

CREATE TABLE IF NOT EXISTS listener_concert
(
    listener_id INT,
    concert_id INT,
    PRIMARY KEY (listener_id, concert_id),
    CONSTRAINT fk_03 FOREIGN KEY (listener_id) REFERENCES listener(id)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_04 FOREIGN KEY (concert_id) REFERENCES concert(id)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS artist
(
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    bio VARCHAR(2500) NOT NULL
);

CREATE TABLE IF NOT EXISTS artist_concert(
    artist_id INT,
    concert_id INT,
    PRIMARY KEY (artist_id, concert_id),
    CONSTRAINT fk_05 FOREIGN KEY (artist_id) REFERENCES artist(id)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_06 FOREIGN KEY (concert_id) REFERENCES concert(id)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS listener_artist(
    listener_id INT,
    artist_id INT,
    PRIMARY KEY (listener_id, artist_id),
    CONSTRAINT fk_07 FOREIGN KEY (listener_id) REFERENCES listener(id)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_08 FOREIGN KEY (artist_id) REFERENCES artist(id)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS playlist
(
    listener_id INT,
    playlist_number INT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500) NOT NULL,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(listener_id, playlist_number),
    FOREIGN KEY (listener_id) REFERENCES listener(id)
        ON UPDATE cascade
);

CREATE TABLE IF NOT EXISTS revenue
(
    id INT PRIMARY KEY,
    song_payout DECIMAL NOT NULL,
    company_revenue DECIMAL NOT NULL,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS song
(
    id INT PRIMARY KEY,
    album VARCHAR(70),
    title VARCHAR(50) NOT NULL,
    genre VARCHAR(50),
    duration TIME NOT NULL,
    release_date DATE DEFAULT (CURDATE()),
    revenue_id INT,
    FOREIGN KEY (revenue_id) REFERENCES revenue(id)
);

CREATE TABLE IF NOT EXISTS playlist_song(
    listenerID INT,
    playlist_number INT,
    song_id INT,
    PRIMARY KEY (listenerID, playlist_number, song_id),
    CONSTRAINT fk_10 FOREIGN KEY (listenerID, playlist_number) REFERENCES playlist(listener_id, playlist_number)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_11 FOREIGN KEY (song_id) REFERENCES song(id)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS review
(
    review_num INTEGER NOT NULL,
    song_id INTEGER,
    listener_id INTEGER,
    text VARCHAR(2500) NOT NULL,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (song_id, review_num),
    CONSTRAINT fk_12 FOREIGN KEY (song_ID) REFERENCES song(id)
        ON UPDATE cascade ON DELETE cascade,
    foreign key (listener_id) REFERENCES listener(id)
);

CREATE TABLE IF NOT EXISTS artist_revenue(
    artist_id INT,
    revenue_id INT,
    PRIMARY KEY (artist_id, revenue_id),
    CONSTRAINT fk_13 FOREIGN KEY (artist_id) REFERENCES artist(id)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_14 FOREIGN KEY (revenue_id) REFERENCES revenue(id)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS artist_song(
    artist_id INT,
    song_id INT,
    PRIMARY KEY (artist_id, song_id),
    CONSTRAINT fk_15 FOREIGN KEY (artist_id) REFERENCES artist(id)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_16 FOREIGN KEY (song_id) REFERENCES song(id)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS advertisement(
    id INT PRIMARY KEY,
    name VARCHAR(60) UNIQUE NOT NULL,
    company VARCHAR(60) NOT NULL,
    target_location VARCHAR(100),
    target_age VARCHAR(50),
    status VARCHAR(60),
    revenue_id INT,
    FOREIGN KEY (revenue_id) REFERENCES revenue(id)
);

CREATE TABLE IF NOT EXISTS listener_song(
    listener_id INT,
    song_id INT,
    playcount INT NOT NULL,
    liked_on DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (listener_id, song_id),
    CONSTRAINT fk_17 FOREIGN KEY (listener_id) REFERENCES listener(id)
        ON UPDATE cascade ON DELETE CASCADE,
    CONSTRAINT fk_18 FOREIGN KEY (song_id) REFERENCES song(id)
        ON UPDATE cascade ON DELETE cascade
);
