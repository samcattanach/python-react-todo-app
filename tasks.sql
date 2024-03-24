DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    due_date DATE,
    priority INTEGER NOT NULL,
    status INTEGER NOT NULL
);

INSERT INTO tasks (name, due_date, priority, status) VALUES ('Buy broccoli', '2024-04-18', 1, 0);