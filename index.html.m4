<html>
    <head>
        <title>Monitor Helper</title>
        <style type="text/css">
            include(reset.css)
        </style>
        <style type="text/css">
            include(monitor.css)
        </style>
        <script type="text/javascript">
            include(monitor_data.js)
        </script>
    </head>
<body>
    <form><label for="tube">Tube</label><input type="text" name="tube" id="tube"></form>
    <table>
        <thead>
            <tr>
                <th>Tube</th>
                <th>Heater</th>
                <th>Neck</th>
                <th>Type</th>
            </tr>
        </thead>
        <tbody id="tbody"/>
    </table>

    <script type="text/javascript">
        include(monitor.js)
    </script>
</body>
</html>
