-- Creates the MySQL user user_0d_1 if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges on the server to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Remove dynamic privileges added after MySQL 8.0.25 from user_0d_1
DELETE FROM mysql.global_grants WHERE user = 'user_0d_1' AND host = 'localhost' AND priv IN ('AUDIT_ABORT_EXEMPT', 'AUTHENTICATION_POLICY_ADMIN', 'FIREWALL_EXEMPT', 'GROUP_REPLICATION_STREAM', 'PASSWORDLESS_USER_ADMIN', 'SENSITIVE_VARIABLES_OBSERVER', 'TELEMETRY_LOG_ADMIN');
-- Reload the grant tables so SHOW GRANTS reports the 8.0.25 privilege set
FLUSH PRIVILEGES;
