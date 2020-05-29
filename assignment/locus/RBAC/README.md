## RBAC (Role Based Access Control)
### Mani Bhushan Kumar (manibhushan05) | May 29th, 2020

#### Introduction
This is a RBAC solution developed in python3.
It is developed to authenticate if a user has permission to perform a ACTION-TYPE (read/write/delete) in some given resources

The following features of an application are considered as resources
* DEVICE-MANAGEMENT - This will allow user to work on device management (E.g.: AWS portal where EC2 can be a device)
* DASHBOARD - The AWS portal UI can be considered as DASHBOARD
* ADMINISTRATION - Admnistrating the AWS account can be considered.

#### Code walkthrough
* AuthenticationSytem\
    * handlers\
        * entity\__init__.py - EntityHandler : Abstract entity handler class which needs to be implemented by child entity classes. Contains abstract method populate() and get()
        * entity\role.py - RoleEntiryHandler : Class to handles roles activity like populating default roles and exposing the roles. It is interited from EntityHandler class
        * entity\user.py - UserEntiryHandler : Class to handle user activity like creating a collection of users and exposing those. If you want to try with more users, you can add those in the populate_default() method
        * exception.py - AuthenticationSystemExceptionHandler : Base exception handling class. Other exception class inherits from this. The exception logger is created here and re-used in child classes. This file contains a total of 6 exception handling classes.<br>
        It contains these classes
            * MissingEntityException - Exception is raised if any entity is missing. It accepts 2 paramters and it acts as parent class for the following
                * MissingUserException
                * MissingResourcesException
                * MissingActionTypeException
            * NoneValueException - Exception is raised if any value is of None type
        * log.py - Class for handling logs and logging. It contains a static method 'get_logger' which accepts the logger name and returns an instance of logging to the calling method.
        * validation.py - Validation class for data validation before processing
    * models\
        * action_type.py - Contains an enumerator with all available ACTION TYPES
        * resources.py - Contains an enumerator with all avilable RESOURCES
        * role.py - Contains the models of a role. It will have a name, resource and action-type
        * user.py - Contains the models of a user. It will have a name and a list of roles
    * service\
        *authentication.py - AuthenticationService class contains a single method authenticate() which takes user, resource and action-type as per the problem description. It validates the input, does the role comparision and returns the authentication status. It also logs the result to file.
* driver.py - Driver class uses the AuthenticationSytem. It first lists all available users with thier permission. Next it prompts you to select user, resources and action-type. It authenticates your choices using AuthenticationSytem and displays the result

