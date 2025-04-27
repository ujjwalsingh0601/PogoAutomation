import pytest
import datetime
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Get the absolute project root folder
    project_root = os.path.dirname(os.path.abspath(__file__))

    reports_dir = os.path.join(project_root, 'Reports')

    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
    report_path = os.path.join(reports_dir, f"report_{current_time}.html")

    config.option.htmlpath = report_path
