FROM postgres

# run *.sql on init
ADD create.sql /docker-entrypoint-initdb.d
ADD init.sql /docker-entrypoint-initdb.d