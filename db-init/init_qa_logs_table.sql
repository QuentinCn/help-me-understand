\connect appdb

CREATE TABLE IF NOT EXISTS qa_logs (
    id SERIAL PRIMARY KEY,
    pdf_id VARCHAR(10) NOT NULL,
    question VARCHAR(10) NOT NULL,
    answer VARCHAR(10) NOT NULL,
    feedback_score BOOLEAN NOT NULL,
    creation_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);