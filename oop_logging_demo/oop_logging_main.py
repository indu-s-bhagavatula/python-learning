import logging
import logging.config
import yaml
from employee import Employee

log_config_path="logging.yaml"
with open(log_config_path, 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# create logger for application
app_logger = logging.getLogger("oop_logging_app")


def main():
    app_logger.info("Starting the application")
    # Creation of first employee
    firstname='Tony'
    lastname='Stark'
    salary=1000.0
    app_logger.info('Creating a new employee with details - ({},{},{})'.format(firstname,lastname,str(salary)))
    tonyobj = Employee(firstname,lastname,str(salary))

    # Creation of second employee Thor
    thor_details='Thor-1000000'
    app_logger.info('Creating a new employee with details - ({})'.format(thor_details) )
    thorobj = Employee.fromFirstNameAndSalary(thor_details)

    # Creation of third employee - Loki
    app_logger.info('Creating a new employee using only first name - ({})'.format('Loki') )
    lokiobj = Employee.fromFirstName('Loki')

    # Logging total number of employees created
    app_logger.info("Total number of employees created in this run {}".format(Employee.num_employees))

    app_logger.info("Finished the application")

if __name__== "__main__":
    main()
