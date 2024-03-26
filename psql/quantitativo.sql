-- Importing data

-- Exploratory Analysis

select * from quantitativo q fetch first 10 row only;

select column_name, data_type
from information_schema.columns
where table_name = 'quantitativo'
order by ordinal_position ;

\d+ quantitativo; -- ON ACTIVE TERMINAL

