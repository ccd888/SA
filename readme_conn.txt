###### readme_conn.txt ######

https://stackoverflow.com/questions/38466190/cant-connect-to-postgresql-on-port-5432
listen_addresses = '*'

https://dba.stackexchange.com/questions/83984/connect-to-postgresql-server-fatal-no-pg-hba-conf-entry-for-host
pg_hba.conf

# TYPE DATABASE USER CIDR-ADDRESS  METHOD
host  all  all 0.0.0.0/0 md5
