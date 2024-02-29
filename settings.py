pip install 'bugsnag[flask]'

import bugsnag

from bugsnag.flask import handle_exceptions

bugsnag.configure(
    api_key="f316eee56196b770fea6d8d8184833a8",
    project_root="/path/to/your/app",
)









app = Flask(__name__)
handle_exceptions(app)
