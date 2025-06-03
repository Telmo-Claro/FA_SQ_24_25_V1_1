import logger
import ui

if __name__ == "__main__":
    log = logger.Logger() # initializes the logger
    try:
        main_ui = ui.Ui(log) # initializes the main UI with logger
        main_ui.Landing() # start the application with the landing page
    except Exception as e:
        log.log_error(e, "MAIN")
        print("An error occurred. Please check the logs for details.")
