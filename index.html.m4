<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="version" content="1.4">
        <title>Monitor Helper</title>
        <style type="text/css">
            include(reset.css)
        </style>
        <style type="text/css">
            include(monitor.css)
        </style>
        <script type="text/javascript">
            include(monitor_data.js.o)
        </script>
    </head>
<body>
    <form><label for="tube">Tube</label><input type="text" name="tube" id="tube"></form>
    <div id="reference"><label for="compat">Compatible with <span id="compat"></span></label><span id="compat"></span><div id="clearReference">×</div></div>
    <table id="search">
        <thead>
            <tr>
                <th></th>
                <th>Tube</th>
                <th>Heater</th>
                <th>G1</th>
                <th>Neck</th>
            </tr>
        </thead>
        <tbody id="compatRes">
        <tbody id="incompatRes">
    </table>

    <script type="text/javascript">
        include(monitor.js.o)
    </script>
</body>
</html>
