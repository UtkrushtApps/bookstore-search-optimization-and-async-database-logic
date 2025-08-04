-- Sample books
INSERT INTO books (title, author, category, published_at) VALUES ('Book A', 'Alice Smith', 'Fiction', '2023-01-01');
INSERT INTO books (title, author, category, published_at) VALUES ('Book B', 'Bob Jones', 'Nonfiction', '2022-05-12');
INSERT INTO books (title, author, category, published_at) VALUES ('Book C', 'Alice Smith', 'Science Fiction', '2019-07-21');
INSERT INTO books (title, author, category, published_at) VALUES ('Book D', 'Dana White', 'Fiction', '2021-10-10');

-- Bulk-insert to mimic a larger dataset
DO $$
DECLARE
  i INTEGER;
BEGIN
  FOR i IN 1..400 LOOP
    INSERT INTO books (title, author, category, published_at) VALUES (
      'RandomBook' || i, 'Author' || (i % 10), CASE WHEN i % 3 = 0 THEN 'Fiction' WHEN i % 3 = 1 THEN 'Nonfiction' ELSE 'Fantasy' END, '2020-01-01'::date + (i % 365)
    );
  END LOOP;
END$$;
