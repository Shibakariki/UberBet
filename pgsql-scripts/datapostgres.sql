\c postgres

DROP TABLE IF EXISTS "test";

CREATE TABLE "test"
(
    "id" serial not null,
    "name" text not null,
    "email" text not null,
    "mdp" text not null,
    "username" text not null
);

INSERT INTO "test" ("name","email","mdp","username") VALUES ('admin','admin@admin.fr','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918','admin');
