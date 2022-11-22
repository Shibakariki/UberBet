CREATE TABLE "test" (
  "Id" serial NOT NULL,
  PRIMARY KEY ("Id"),
  "name" text NOT NULL,
  "email" text NOT NULL,
  "mdp" text NOT NULL,
  "username" text NOT NULL
);

INSERT INTO "test" ("name", "email", "mdp", "username")
VALUES ('admin', 'admin@admin.fr', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin');