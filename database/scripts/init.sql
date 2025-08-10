SET search_path TO public;

DROP EXTENSION IF EXISTS "uuid-ossp";
DROP EXTENSION IF EXISTS "vector";

CREATE EXTENSION "uuid-ossp" SCHEMA public;
CREATE EXTENSION "vector" SCHEMA public;
