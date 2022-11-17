FROM postgres:latest

ENV PGDATA /var/lib/postgresql/data
# this 777 will be replaced by 700 at runtime (allows semi-arbitrary "--user" values)
RUN chown -R postgres:postgres "$PGDATA" && chmod 777 "$PGDATA"