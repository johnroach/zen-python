from zen import app

def before_feature(context, feature):
    app.testing = True
    context.client = app.test_client()
