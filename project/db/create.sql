-- CREATE DATABASE users_prod;
-- CREATE DATABASE users_dev;
-- CREATE DATABASE users_test;
CREATE TABLE IF NOT EXISTS pathcount (
  path TEXT PRIMARY KEY,
  count INT DEFAULT 0
);
