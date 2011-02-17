<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
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
        <section id="sky">
            <img id="duck" src="/static/duck256.png" />
        </section>

        <section id="container">
            <section id="result">
                <form id="form">
                    <input type="text" name="url" value="Enter URL" />
                    <input type="submit" value="Create" />
                </form>
            </section>
        </section>
    </body>
</html>
