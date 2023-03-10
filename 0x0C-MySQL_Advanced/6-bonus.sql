-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student
-- Procedure AddBonus is taking 3 inputs (in this order):
-- 1. user_id, a users.id value (you can assume user_id is linked to an existing users)
-- 2. project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- 3. score, the score value for the correction
DELIMITER //
CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;
    
    -- Check if the project already exists in the projects table
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    
    -- If project_id is null, then the project doesn't exist, so we need to create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Insert the correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;
