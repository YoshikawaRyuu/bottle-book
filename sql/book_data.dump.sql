--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Homebrew)
-- Dumped by pg_dump version 15.4

-- Started on 2023-11-07 10:33:07 JST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16391)
-- Name: book_user; Type: TABLE; Schema: public; Owner: book_userY
--

CREATE TABLE public.book_user (
    user_id character varying(255) NOT NULL,
    passwd character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    user_shi character varying(255),
    user_mei character varying(255),
    del boolean
);


ALTER TABLE public.book_user OWNER TO "book_userY";

--
-- TOC entry 216 (class 1259 OID 24583)
-- Name: books; Type: TABLE; Schema: public; Owner: book_userY
--

CREATE TABLE public.books (
    id integer NOT NULL,
    name character varying(255),
    volume character varying(255),
    author character varying(255),
    publisher character varying(255),
    memo text,
    create_date timestamp with time zone NOT NULL,
    del boolean
);


ALTER TABLE public.books OWNER TO "book_userY";

--
-- TOC entry 215 (class 1259 OID 24582)
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: book_userY
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_seq OWNER TO "book_userY";

--
-- TOC entry 3620 (class 0 OID 0)
-- Dependencies: 215
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: book_userY
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- TOC entry 3465 (class 2604 OID 24586)
-- Name: books id; Type: DEFAULT; Schema: public; Owner: book_userY
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- TOC entry 3612 (class 0 OID 16391)
-- Dependencies: 214
-- Data for Name: book_user; Type: TABLE DATA; Schema: public; Owner: book_userY
--

COPY public.book_user (user_id, passwd, email, user_shi, user_mei, del) FROM stdin;
001	yyyyy	aaaaa	ヨシ	カワ	f
002	wzwzw	bbbbb	ヨシカ	ヨシカワ	f
003	yoshikawa	ccccc	おい	お前	f
004	wzwzw	ddddd	ミャッミン	パイン	f
\.


--
-- TOC entry 3614 (class 0 OID 24583)
-- Dependencies: 216
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: book_userY
--

COPY public.books (id, name, volume, author, publisher, memo, create_date, del) FROM stdin;
1	君たちはどう生きるか	単体(なし)	吉野源三郎	ポプラ社	映画化されてた	2023-10-25 04:01:51.445179+09	f
2	制作実習	上巻	岡田直己先生	神戸電子	それなりに面白い	2023-10-25 14:03:19.124026+09	f
\.


--
-- TOC entry 3621 (class 0 OID 0)
-- Dependencies: 215
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: book_userY
--

SELECT pg_catalog.setval('public.books_id_seq', 9, true);


--
-- TOC entry 3467 (class 2606 OID 16397)
-- Name: book_user book_user_pkey; Type: CONSTRAINT; Schema: public; Owner: book_userY
--

ALTER TABLE ONLY public.book_user
    ADD CONSTRAINT book_user_pkey PRIMARY KEY (user_id);


--
-- TOC entry 3469 (class 2606 OID 24590)
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: book_userY
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


-- Completed on 2023-11-07 10:33:07 JST

--
-- PostgreSQL database dump complete
--

