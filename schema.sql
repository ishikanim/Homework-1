create table data (
    id serial primary key, 
    nam varchar(255) NOT NULL,
    email varchar(255) NOT NULL, 
    num int, 
    campusFrequency varchar(255), 
    recommend varchar(255), 
    timestampy timestamp without time zone DEFAULT now() 
);


create table bad_way_to_do_users (
    id serial primary key,
    username text,
    password text
);

cur.execute("CREATE TABLE data (name VARCHAR(255), address VARCHAR(255))")


create_script =  ''' CREATE TABLE IF NOT EXISTS data (  id serial primary key, 
    nam varchar(255) NOT NULL,
    email varchar(255) NOT NULL, 
    num int, 
    campusFrequency varchar(255), 
    recommend varchar(255), 
    timestampy timestamp DEFAULT now()); '''

''' CREATE TABLE IF NOT EXISTS results ( id serial primary key, name  text, email email, number number, campusFrequency text, recommend radio, when checkbox, CURRENT_TIMESTAMP() ); '''

cur.execute("SELECT * FROM data")
for table in cur.fetchall():
    print(table)

    

    create table data (
    id serial primary key, 
    nam varchar(255) NOT NULL,
    email varchar(255) NOT NULL, 
    num int, 
    campusFrequency varchar(255), 
    recommend varchar(255), 
    timestampy timestamp without time zone DEFAULT now() 
);
