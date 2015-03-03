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
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="5000;url=http://plugincompat.herokuapp.com">
        <script type="text/javascript">
            window.location.href = "http://plugincompat.herokuapp.com"
        </script>
        <title>Page Redirection</title>
    </head>
    <body>
        <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
        If you are not redirected automatically, follow the <a href='http://plugincompat.herokuapp.com'>link to plugincompat page</a>.
    </body>
</html>
    """

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
