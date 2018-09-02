import logging
import logging.config
import json
import yaml
import sys

log_config_path="logging.yaml"
with open(log_config_path, 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# create logger for application
employee_logger = logging.getLogger("employee")

class Employee:
    num_employees = 0
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        employee_logger.info('Created new employee with details {}'.format(self.getjsonformat()))
        # Increment number of employees
        Employee.num_employees +=1

    def getjsonformat(self):
        return json.dumps(self.__dict__)
        # return '{firstname:%s}'.format(self.firstname)

    def getFullName(self):
        return self.firstname + ' ' + self.lastname

    def setSalary(self,salary):
        employee_logger.debug('Salary of {} before processing is {}'.format(self.getFullName(), str(self.salary)))
        self.salary = salary
        employee_logger.info('Completed setting salary. New details are {} '.format(self.getjsonformat()))

    def adjustsalary(self, increase_percent):
        employee_logger.debug('Salary of {} before processing is {}'.format(self.getFullName(), str(self.salary)))
        self.salary += (self.salary * increase_percent/100)
        employee_logger.info('Completed adjusting salary {}'.format(self.getjsonformat()))

    @classmethod
    def fromFirstName(cls, firstname):
        return cls(firstname,'',0.0)

    @classmethod
    def fromFirstNameAndSalary(cls, emp_details):
        firstname, salary_str = emp_details.split("-")
        try:
            salary = float(salary_str)
            return cls(firstname, '', salary )
        except:
            employee_logger.warning('Cannot create object with emp_details passed as {}.StackTrace is\n{}'.format(emp_details,sys.exc_info() ))
            return
