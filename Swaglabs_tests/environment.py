from selenium import webdriver
"""
@before_scenario:
Executes opening of Chrome browser and maximizing the window for precise element detection.

@after_scenario:
Closes Chrome browser in preparation of next scenario.
"""
def before_scenario(context, scenario):
    print("Starting before_scenario")
    try:
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        print("before_scenario completed successfully")
    except Exception as e:
        print(f"Error in before_scenario: {e}")

def after_scenario(context, scenario):
    print("Starting after_scenario")
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
        print("after_scenario completed successfully")
    except Exception as e:
        print(f"Error in after_scenario: {e}")