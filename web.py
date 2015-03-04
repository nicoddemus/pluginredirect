import os
import itertools
import flask



app = flask.Flask('pluginredirect')

@app.route('/', methods=['GET', 'POST'])
def index():
    return """
<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <title>Page Redirection</title>
    </head>
    <body>
        <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
        This page has moved, please follow the link to <a href='http://plugincompat.herokuapp.com'>plugincompat</a> page.
    </body>
</html>
    """

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
