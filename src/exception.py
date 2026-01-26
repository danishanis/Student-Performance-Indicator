import sys # controlling exceptions with sys library
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    """
    Custom message to be pushed in logs whenever exception occurs.
    Input Parameters:
        1. error: the error message or exception object
        2. error_detail: the sys module which contains info about exception
    
    Output:
    exc_info() returns a tuple of three values that gives information about the exception that is currently being handled.
        exc_tb: execution tab, a traceback object to give information about the error (file name, line number etc)
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] in line number [{1}]. The error message is: \
        [{2}]".format(
     file_name, exc_tb.tb_lineno, str(error))

    return error_message

    
# Custom Exception class to be called whenever exception occurs
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        # since we are inheriting from Exception class, we'd like to invoke constructor in Exception class with error_message parameter
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,
                                                  error_detail = error_detail)
    
    # To get the printable representation of the error message when exception occurs
    def __str__(self):
        return self.error_message
    
# Checking if exception is working fine
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by zero exception occurred", exc_info=True)
#         raise CustomException

        