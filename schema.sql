-- Poor initial schema: missing indexes, constraints
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id SERIAL,
    title TEXT,
    author TEXT,
    category TEXT,
    published_at DATE
    -- No PK, no NOT NULL, no indexes
);
