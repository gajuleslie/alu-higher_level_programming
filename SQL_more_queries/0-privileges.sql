-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
-- Remove dynamic privileges added after MySQL 8.0.25 from user_0d_1
DELETE FROM mysql.global_grants WHERE user = 'user_0d_1' AND host = 'localhost' AND priv IN ('AUDIT_ABORT_EXEMPT', 'AUTHENTICATION_POLICY_ADMIN', 'FIREWALL_EXEMPT', 'GROUP_REPLICATION_STREAM', 'PASSWORDLESS_USER_ADMIN', 'SENSITIVE_VARIABLES_OBSERVER');
-- Remove the same post-8.0.25 dynamic privileges from user_0d_2
DELETE FROM mysql.global_grants WHERE user = 'user_0d_2' AND host = 'localhost' AND priv IN ('AUDIT_ABORT_EXEMPT', 'AUTHENTICATION_POLICY_ADMIN', 'FIREWALL_EXEMPT', 'GROUP_REPLICATION_STREAM', 'PASSWORDLESS_USER_ADMIN', 'SENSITIVE_VARIABLES_OBSERVER');
-- Reload the grant tables so SHOW GRANTS reports the 8.0.25 privilege set
FLUSH PRIVILEGES;
-- Lists all privileges of user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Lists all privileges of user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
