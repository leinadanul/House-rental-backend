-- Database: postgres

-- DROP DATABASE IF EXISTS postgres;

CREATE DATABASE postgres
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Colombia.1252'
    LC_CTYPE = 'Spanish_Colombia.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE postgres
    IS 'default administrative connection database';


--""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""--
--""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""--

--LANDLORDS TABLE

-- Table: public.landlord

-- DROP TABLE IF EXISTS public.landlord;

CREATE TABLE IF NOT EXISTS public.landlord
(
    id bigint NOT NULL,
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    phone_number integer NOT NULL,
    mobile_number integer,
    company_name character varying(255) COLLATE pg_catalog."default",
    picture character varying(255) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.landlord
    OWNER to postgres;

--""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""--
--""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""--

--PROPERTIES TABLE



CREATE TABLE IF NOT EXISTS public.properties
(
    property_id bigint NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    property_type character varying(255) COLLATE pg_catalog."default" NOT NULL,
    location character varying(255) COLLATE pg_catalog."default" NOT NULL,
    capacity integer NOT NULL,
    property character varying(255) COLLATE pg_catalog."default" NOT NULL,
    host_info character varying(255) COLLATE pg_catalog."default" NOT NULL,
    characteristics character varying(255) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    features character varying(255) COLLATE pg_catalog."default" NOT NULL,
    default_available boolean NOT NULL,
    price integer NOT NULL,
    additional_fees character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT properties_pkey PRIMARY KEY (property_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.properties
    OWNER to postgres;

--------------------------------------------------
-- Table: public.characteristics

-- DROP TABLE IF EXISTS public.characteristics;

CREATE TABLE IF NOT EXISTS public.characteristics
(
    id integer NOT NULL DEFAULT nextval('characteristics_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default",
    description character varying COLLATE pg_catalog."default",
    CONSTRAINT characteristics_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.characteristics
    OWNER to postgres;


------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS property_type (
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description VARCHAR(100)
);
ALTER TABLE property_type
ALTER COLUMN description SET NOT NULL




CREATE TABLE IF NOT EXISTS host(
	id SERIAL NOT NULL PRIMARY KEY, 
	name VARCHAR(50) NOT NULL,
	phone_number INTEGER NOT NULL,
	email INTEGER
);




CREATE TABLE IF NOT EXISTS fees(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description VARCHAR(100),
	price NUMERIC NOT NULL
);




CREATE TABLE IF NOT EXISTS features(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100),
	description VARCHAR(100)
);




CREATE TABLE IF NOT EXISTS distributions(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100),
	description VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS properties(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	country VARCHAR(100) NOT NULL,
	state VARCHAR(100) NOT NULL,
	city VARCHAR(100) NOT NULL,
	address VARCHAR(255) NOT NULL,
	capacity INTEGER NOT NULL,
	unavailable_days VARCHAR(50) NOT NULL,
	price FLOAT NOT NULL

	
);

ALTER TABLE properties
ADD COLUMN host_id SERIAL NOT  NULL



ALTER TABLE properties
ADD FOREIGN KEY (host_id) REFERENCES host(id);




ALTER TABLE properties
ADD COLUMN property_type_id SERIAL NOT  NULL



ALTER TABLE properties
ADD FOREIGN KEY (property_type_id) REFERENCES property_type(id);


CREATE TABLE IF NOT EXISTS characteristics(
	id SERIAL NOT NULL PRIMARY KEY,
	description VARCHAR(50),
	properties_id SERIAL NOT NULL,
	FOREIGN KEY (properties_id) REFERENCES properties(id)
)


CREATE TABLE IF NOT EXISTS distributions(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	descriptipn VARCHAR(50) NOT NULL
)

CREATE TABLE IF NOT EXISTS properties_has_property_distribution(
	properties_id SERIAL NOT NULL,
	distributions_id SERIAL NOT NULL,
	FOREIGN KEY (properties_id) REFERENCES properties(id),
	FOREIGN KEY (distributions_id) REFERENCES distributions(id)
);

CREATE TABLE IF NOT EXISTS properties_has_features(
	properties_id SERIAL NOT NULL,
	features_id SERIAL NOT NULL,
	FOREIGN KEY (properties_id) REFERENCES properties(id),
	FOREIGN KEY (features_id) REFERENCES features(id)
);



ALTER TABLE distributions ADD COLUMN quantity INTEGER;
12:03:45
ALTER TABLE distributions ADD COLUMN quantity
12:03:24
ALTER TABLE properties ADD COLUMN description TEXT;
12:02:07
ALTER TABLE properties ADD COLUMN description;
12:01:47
SELECT * FROM public.host ORDER BY id ASC
10:26:18
SELECT * FROM public.properties ORDER BY id ASC
09:59:08
SELECT * FROM public.host ORDER BY id ASC
09:20:32
SELECT * FROM public.host ORDER BY id ASC
09:19:37
SELECT * FROM public.features ORDER BY id ASC
14:33:52
INSERT INTO distributions (name) VALUES ('Bedroom'); INSERT INTO distributions (name) VALUES ('Bed');
14:33:45
INSERT INTO distributions (name) VALUES ('Bedroom'); INSERT INTO distributions (name) VALUES ('Bed');
14:33:15
INSERT INTO features (name, icon) VALUES ('Washer', 'LocalLaundryServiceIcon'); INSERT INTO features (name, icon) VALUES ('Free dryer', 'LocalLaundryServiceIcon '); INSERT INTO features (name, icon) VALUES ('Pets allowed', 'PetsIcon'); INSERT INTO features (name, icon) VALUES ('Free parking', 'LocalParkingIcon'); INSERT INTO features (name, icon) VALUES ('TV', 'TvIcon'); INSERT INTO features (name, icon) VALUES ('Mountaint view', 'PanoramaIcon'); INSERT INTO features (name, icon) VALUES ('Refrigerator', 'KitchenIcon'); INSERT INTO features (name, icon) VALUES ('Microwave', 'MicrowaveIcon'); INSERT INTO features (name, icon) VALUES ('A/C', 'AcUnitIcon'); INSERT INTO features (name, icon) VALUES ('Smoking zone', 'SmokeFreeIcon');
14:33:10
SELECT * FROM public.features ORDER BY id ASC
14:32:44
INSERT INTO distributions (name) VALUES ('Bath');
14:29:46
INSERT INTO features (name, icon) VALUES ('Wifi', 'SignalWifi2BarIcon');
14:29:30
ALTER TABLE properties_has_property_distribution ADD COLUMN quantity INTEGER;
14:27:16
ALTER TABLE properties_has_property_distribution ADD COLUMN quantity;
14:26:04
ALTER TABLE properties_has_property_distribution ADD COLUMN quantity
14:25:56
INSERT ALTER TABLE properties_has_property_distribution ADD COLUMN quantity
14:25:50
INSERT INTO TABLE properties_has_property_distribution ADD COLUMN quantity
14:25:23



---------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS property_type (
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description VARCHAR(100)
);
ALTER TABLE property_type
ALTER COLUMN description SET NOT NULL




CREATE TABLE IF NOT EXISTS host(
	id SERIAL NOT NULL PRIMARY KEY, 
	name VARCHAR(50) NOT NULL,
	phone_number INTEGER NOT NULL,
	email INTEGER
);




CREATE TABLE IF NOT EXISTS fees(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description VARCHAR(100),
	price NUMERIC NOT NULL
);




CREATE TABLE IF NOT EXISTS features(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100),
	description VARCHAR(100)
);




CREATE TABLE IF NOT EXISTS distributions(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100),
	description VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS properties(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	country VARCHAR(100) NOT NULL,
	state VARCHAR(100) NOT NULL,
	city VARCHAR(100) NOT NULL,
	address VARCHAR(255) NOT NULL,
	capacity INTEGER NOT NULL,
	unavailable_days VARCHAR(50) NOT NULL,
	price FLOAT NOT NULL

	
);

ALTER TABLE properties
ADD COLUMN host_id SERIAL NOT  NULL



ALTER TABLE properties
ADD FOREIGN KEY (host_id) REFERENCES host(id);




ALTER TABLE properties
ADD COLUMN property_type_id SERIAL NOT  NULL



ALTER TABLE properties
ADD FOREIGN KEY (property_type_id) REFERENCES property_type(id);


CREATE TABLE IF NOT EXISTS characteristics(
	id SERIAL NOT NULL PRIMARY KEY,
	description VARCHAR(50),
	properties_id SERIAL NOT NULL,
	FOREIGN KEY (properties_id) REFERENCES properties(id)
)


CREATE TABLE IF NOT EXISTS distributions(
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	descriptipn VARCHAR(50) NOT NULL
)

CREATE TABLE IF NOT EXISTS properties_has_property_distribution(
	properties_id SERIAL NOT NULL,
	distributions_id SERIAL NOT NULL,
	FOREIGN KEY (properties_id) REFERENCES properties(id),
	FOREIGN KEY (distributions_id) REFERENCES distributions(id)
);

CREATE TABLE IF NOT EXISTS properties_has_features(
	properties_id SERIAL NOT NULL,
	features_id SERIAL NOT NULL,
	FOREIGN KEY (properties_id) REFERENCES properties(id),
	FOREIGN KEY (features_id) REFERENCES features(id)
);


ALTER TABLE property_distribution
RENAME TO property_distributions

ALTER TABLE fees
ADD COLUMN property_id SERIAL NOT NULL

ALTER TABLE fees
ADD FOREIGN KEY (property_id) REFERENCES properties(id);


ALTER TABLE host
ADD COLUMN landlord_id SERIAL NOT NULL

ALTER TABLE host
ADD FOREIGN KEY (landlord_id) REFERENCES landlord(id);

ALTER TABLE host
DROP COLUMN property_id

INSERT INTO property_type (name, description) VALUES ('House','house');

INSERT INTO features (name, icon) VALUES ('Wifi', 'SignalWifi2BarIcon');
