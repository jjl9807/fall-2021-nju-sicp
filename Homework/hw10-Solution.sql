.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE min < height AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d1.name FROM dogs AS d1, parents, dogs AS d2 WHERE d1.name = child AND d2.name = parent ORDER BY d2.height DESC;


CREATE TABLE siblings AS
  SELECT d1.name AS name1, d2.name AS name2, d1.height AS h1, d2.height AS h2 FROM dogs AS d1, dogs AS d2, parents AS p1, parents AS p2 WHERE d1.name = p1.child AND d2.name = p2.child AND p1.parent = p2.parent AND d1.name < d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || name1 || " plus " || name2 ||" have the same size: " || size FROM siblings, sizes WHERE min < h1 AND h1 <= max AND min < h2 AND h2 <= max;
