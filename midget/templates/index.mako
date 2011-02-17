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
                
                $('#form').submit(function(){
                    var url = $('input[type=text]').val();
                    $('#result').css("text-align", "center");

                    $.post('/api', {url: url}, function(data) {
                        $('#result').html('<a href="'+ data +'">'+data+'</a>');
                    })
                    .error(function(data) { $('#result').html(data.responseText); });
                    return false;
                });
            });
        </script>
    </head>

    <body>
        <div id="sky">
            <img id="duck" src="/static/duck256.png" />
        </div>

        <div id="container">
            <div id="result">
                <form id="form">
                    <input type="text" name="url" value="Enter URL" />
                    <input type="submit" value="Create" />
                </form>
            </div>
        </div>
    </body>
</html>
