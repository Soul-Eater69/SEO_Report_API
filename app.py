from deepawali_seo_report import app
from deepawali_seo_report.views import *
from flask_restful import Api



api = Api(app)

api.add_resource(OnPageSEO, "/getOnPageSEOReport")
api.add_resource(Usability, "/getUsabilityReport")
api.add_resource(Performance, "/getPerformanceReport")
api.add_resource(Setup, "/setup")

if __name__ == "__main__":
    app.run(debug=True)