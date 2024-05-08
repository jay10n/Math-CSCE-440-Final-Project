-- Create the new database
CREATE DATABASE Russo_Ukraine_Loss_DB;

-- Create a new user
CREATE USER jayton WITH ENCRYPTED PASSWORD 'XF-9HGXtN8Ce9';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON DATABASE Russo_Ukraine_Loss_DB TO jayton;
