# Course Completions Database Populate Script

## About

This script populates the new columns in the `course_completion_events` table in the reporting database:

* `profession_name`
* `organisation_abbreviation`
* `grade_code`

## Initial setup


### Using the Wizard

The easiest way to setup the script is to run the set up Wizard:

```sh
./setupWizard.sh
```

The wizard will guide you through the creation of a config file (`config.env`), if it's not present, which will contain the connection details for your reporting and CSRS databases. Once this is completed, it will build a Docker container which you can run your scripts in.

### Manual setup

If you'd rather set this up manually, here are the steps:

#### 1. Create a config file

Create a new file `config.env` in the project root. In the file, add the connection details for the reporting and CSRS databases, like so:

```props
REPORTING_DB_HOST=host
REPORTING_DB_USERNAME=user
REPORTING_DB_PASSWORD=password
REPORTING_DB_PORT=0000
REPORTING_DB_DATABASE=db

CSRS_DB_HOST=host
CSRS_DB_USERNAME=user
CSRS_DB_PASSWORD=password
CSRS_DB_DATABASE=db
```

#### 2. Build the script Docker container

Build the Docker container:

```sh
docker build -t course-completions-populate .
```

Optionally, you can run the scripts without a Docker container.

## Scripts

To start and enter the Script container, run this command:

```sh
docker run -it --rm -v $PWD/app:/app -w /app --env-file config.env course-completions-populate bash
```

Either within the Docker container or standalone, the prefix to run all the scripts is:

```sh
python app.py <script>
```

### Plan

```sh
python app.py plan
```

The `plan` script checks which rows have empty values for `profession_name`, `organisation_abbreviation` and `grade_code`. It then uses the values from `profession_id`, `organisation_id` and `grade_id` to retrieve the data from the CSRS database. It will create a file `plan.json` which looks like this:

```json
[
    {
        "eventId": 1,
        "updates": [
            {
                "row": "organisation_abbreviation",
                "value": "CO"
            },
            {
                "row": "profession_name",
                "value": "Analysis"
            },
            {
                "row": "grade_code",
                "value": "SEO"
            }
        ]
    },
    ...
```

This file will later be used to populate the reporting database during the `apply` stage.

### Apply

```sh
python app.py apply
```

The `apply` script takes the updates described in the `plan.json` file created during the `plan` stage and applies them to the reporting database.

### Revert

```sh
python app.py revert
```

In case of any issues, you can use the `revert` script to clear all values for the new columns using the plan.

## Logs

To check the logs, check the `app.log` file or run this command:

```sh
tail -f app.log
```

## Test locally

You can test and run the scripts locally by setting up by using Docker Compose:

```sh
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up -d
docker-compose -f docker-compose.dev.yml exec script bash
```

This will create setup a local environment, including a local MySQL and Postgres setup.
