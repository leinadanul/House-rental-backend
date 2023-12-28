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

