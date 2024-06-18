echo "COURSE COMPLETIONS POPULATE SCRIPT - SETUP WIZARD"

if [ ! -f ./config.env ]; then
    echo "No config file found."
    echo
    echo "Configure Reporting database"
    echo
    read -p "Host: " REPORTING_DB_HOST
    read -p "Username: " REPORTING_DB_USERNAME
    read -s -p "Password: " REPORTING_DB_PASSWORD
    echo \n
    read -p "Port: " REPORTING_DB_PORT
    read -p "Database: " REPORTING_DB_DATABASE

    echo
    echo "2. Configure CSRS database"

    read -p "Host: " CSRS_DB_HOST
    read -p "Username: " CSRS_DB_USERNAME
    read -s -p "Password: " CSRS_DB_PASSWORD
    echo \n
    read -p "Database: " CSRS_DB_DATABASE

    echo """REPORTING_DB_HOST=$REPORTING_DB_HOST
REPORTING_DB_USERNAME=$REPORTING_DB_USERNAME
REPORTING_DB_PASSWORD=$REPORTING_DB_PASSWORD
REPORTING_DB_PORT=$REPORTING_DB_PORT
REPORTING_DB_DATABASE=$REPORTING_DB_DATABASE

CSRS_DB_HOST=$CSRS_DB_HOST
CSRS_DB_USERNAME=$CSRS_DB_USERNAME
CSRS_DB_PASSWORD=$CSRS_DB_PASSWORD
CSRS_DB_DATABASE=$CSRS_DB_DATABASE""" > config.env
else
    echo "Config file found."
fi

echo
echo "Building script container..."
docker build -t course-completions-populate .

echo
echo "Done. Enter the script container?"
read -p "(Y/n): " RUN_CONTAINER_CONFIRMATION

if [ $RUN_CONTAINER_CONFIRMATION = "Y" ]; then
    docker run -it --rm -v $PWD/app:/app -w /app --env-file config.env course-completions-populate bash
fi