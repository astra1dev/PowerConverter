from colorama import Fore, Style  # , Back


# @error_handler is the shorthand way of saying: some_function = handle_errors(some_function)
# when some_function is called, it is actually calling the "wrapper" function returned by error_handler
# the wrapper allows you to modify or extend the behavior of the original function, without modifying its code
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print(Fore.GREEN + "[SUCCESS] File(s) successfully converted!" + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR] File(s) not found! Make sure you put in the path correctly." +
                  Style.RESET_ALL)
        except FileExistsError:
            print(Fore.RED + "[INFO] The file is already in the desired format!" + Style.RESET_ALL)
        except OSError:
            print(Fore.RED + "[ERROR] The file(s) could not be converted!" + Style.RESET_ALL)

    return wrapper
