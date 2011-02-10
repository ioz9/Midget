<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <head>
        <title>kan.gd URL shortner</title>
        <link rel="stylesheet" href="/static/style.css" type="text/css" />
        <script type="text/javascript" src="http://www.google.com/jsapi"></script>
        <script type="text/javascript">
            google.load("jquery", "1.5.0")
            google.setOnLoadCallback(function() {
                $('input[type=text]').focus(function(){ $(this).val(''); });
                $('input[type=submit]').click(function() {
                    var url = $('input[type=text]').val();
                    alert(url);
                });
            });
        </script>
    </head>

    <body>
        <div id="sky">
            <img id="duck" src="/static/duck256.png" />
        </div>

        <div id="container">
            <div>
                <input type="text" name="url" value="Enter URL" />
                <input type="submit" value="Create" />
            </div>
        </div>
    </body>
</html>
