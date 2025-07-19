# RDS MySQL Setup Instructions

1. Launch RDS MySQL instance.
2. Allow EC2 IP in RDS security group.
3. Create database: `quiz_db`.
4. Create table `results`:
   ```sql
   CREATE TABLE results (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       score INT
   );
   ```