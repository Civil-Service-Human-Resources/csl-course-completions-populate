import os

def get_env(env_name, default):
    return default if os.environ.get(env_name) == None else os.environ.get(env_name)

vars = {
    "reportingDb": {
        "host": get_env("REPORTING_DB_HOST", "postgres"),
        "username": get_env("REPORTING_DB_USERNAME", "postgres"),
        "password": get_env("REPORTING_DB_PASSWORD", "root-pw"),
        "port": get_env("REPORTING_DB_PORT", "5432"),
        "database": get_env("REPORTING_DB_DATABASE", "reporting")
    },
    "csrsDb": {
        "host": get_env("CSRS_DB_HOST", "mysql"),
        "username": get_env("CSRS_DB_USERNAME", "root"),
        "password": get_env("CSRS_DB_PASSWORD", "example"),
        "database": get_env("CSRS_DB_DATABASE", "csrs")
    }
}
