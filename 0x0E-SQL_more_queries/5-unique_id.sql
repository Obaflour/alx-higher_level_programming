-- This script creates tables unique ids

CREATE TABLE IF NOT EXIXTS `unique_id` (
	`id`	INT	DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
	);
