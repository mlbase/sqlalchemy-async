CREATE TABLE api_user(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    is_active boolean DEFAULT = TRUE,
    is_superuser boolean DEFAULT = FALSE
)

CREATE TABLE api_video(
    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
    owner_id INTEGER,
    TITLE VARCHAR(100),
    is_deleted BOOLEAN DEFAULT = FALSE,
    is_reported BOOLEAN DEFAULT = FALSE,
    watch_count INTEGER,
    report_count INTEGER,
    like_count INTEGER
)

CREATE TABLE api_like(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    is_liked BOOLEAN DEFAULT = FALSE,
    owner_id INTEGER,
    video_id INTEGER
)

ALTER TABLE api_video
ADD FOREIGN KEY (owner_id) references api_user(id)

ALTER TABLE api_like
ADD FOREIGN KEY (owner_id) references api_user(id)

ALTER TABLE api_like
ADD FOREIGN KEY (video_id) references api_video(id)