-- Table: book_user

-- DROP TABLE book_user;

CREATE TABLE book_user
(
    user_id character varying(255) NOT NULL,
    passwd character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    user_shi character varying(255),
    user_mei character varying(255),
    del boolean,
    CONSTRAINT book_user_pkey PRIMARY KEY (user_id)
);