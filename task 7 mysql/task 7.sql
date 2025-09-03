
CREATE TABLE Movie (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year YEAR,
    description TEXT
);

CREATE TABLE Media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    media_type ENUM('Video', 'Image') NOT NULL,
    media_url VARCHAR(500) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

-- Insert movie Amaran
INSERT INTO Movie (title, release_year, description) VALUES (
    'Amaran', 
    2024, 
    'A biographical action war film about Major Mukund Varadarajan.'
);

-- Insert media data for Amaran
INSERT INTO Media (movie_id, media_type, media_url) VALUES
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), 'Video', 'http://example.com/amaran-trailer.mp4'),
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), 'Image', 'http://example.com/amaran-poster.jpg');

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE MovieGenre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

-- Insert genres
INSERT INTO Genre (genre_name) VALUES ('Action'), ('Biography'), ('War');

-- Link Amaran movie to genres
INSERT INTO MovieGenre (movie_id, genre_id) VALUES
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), (SELECT genre_id FROM Genre WHERE genre_name = 'Action')),
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), (SELECT genre_id FROM Genre WHERE genre_name = 'Biography')),
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), (SELECT genre_id FROM Genre WHERE genre_name = 'War'));

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 10),
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Insert users
INSERT INTO User (username, email) VALUES ('filmfan1', 'fan1@example.com'), ('filmfan2', 'fan2@example.com');

-- Insert reviews by users for Amaran
INSERT INTO Review (movie_id, user_id, rating, comment) VALUES
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), (SELECT user_id FROM User WHERE username = 'filmfan1'), 9, 'Great portrayal and story.'),
((SELECT movie_id FROM Movie WHERE title = 'Amaran'), (SELECT user_id FROM User WHERE username = 'filmfan2'), 8, 'Powerful and emotional!');

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Skill (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE ArtistSkill (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (skill_id) REFERENCES Skill(skill_id)
);

-- Insert artist
INSERT INTO Artist (name) VALUES ('Sivakarthikeyan');

-- Insert skills
INSERT INTO Skill (skill_name) VALUES ('Acting'), ('Dancing');

-- Link artist to skills
INSERT INTO ArtistSkill (artist_id, skill_id) VALUES
((SELECT artist_id FROM Artist WHERE name = 'Sivakarthikeyan'), (SELECT skill_id FROM Skill WHERE skill_name = 'Acting')),
((SELECT artist_id FROM Artist WHERE name = 'Sivakarthikeyan'), (SELECT skill_id FROM Skill WHERE skill_name = 'Dancing'));

CREATE TABLE Role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE ArtistRoleMovie (
    artist_id INT,
    role_id INT,
    movie_id INT,
    PRIMARY KEY (artist_id, role_id, movie_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (role_id) REFERENCES Role(role_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

-- Insert roles
INSERT INTO Role (role_name) VALUES ('Actor'), ('Producer');

-- Link artist to roles in movie Amaran
INSERT INTO ArtistRoleMovie (artist_id, role_id, movie_id) VALUES
(
  (SELECT artist_id FROM Artist WHERE name = 'Sivakarthikeyan'),
  (SELECT role_id FROM Role WHERE role_name = 'Actor'),
  (SELECT movie_id FROM Movie WHERE title = 'Amaran')
),
(
  (SELECT artist_id FROM Artist WHERE name = 'Sivakarthikeyan'),
  (SELECT role_id FROM Role WHERE role_name = 'Producer'),
  (SELECT movie_id FROM Movie WHERE title = 'Amaran')
);
