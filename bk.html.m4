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
            include(bk_data.js.o)
        </script>
    </head>
<body>
    <form><label for="tube">Tube</label><input type="text" name="tube" id="tube"><div id="showhelp">?</div></form>
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
        <tbody id="maybeRes">
    </table>

    <div id="help">
        <h1>Finding your tube</h1>
        <p>Type the tube model into the <emph>Tube</emph> field. The search results will update automatically as you type.</p>

        <h1>Finding a compatible tube</h1>
        <p>Clicking or tapping a search result enables compatibility filtering. In this mode, tubes which are compatible with the selected tube are displayed more prominently.</p>
        <ol>
            <li>Search for your source tube, and click or tap it in the results list. Results & <emph>Tube</emph> input will clear.</li>
            <li>Search for your potential donor tube. Compatible tubes will appear normally at the top of the search results; incompatible tubes will be greyed out at the bottom.</li>
        </ol>

        <h1>Legend</h1>
        <table id="legend">
            <tbody>
                <tr>
                    <td class="type color rgb"><span></span><td>
                    <td>Color tube</td>
                </tr>
                <tr>
                    <td class="type color grb"><span></span><td>
                    <td>Color tube, red/green guns swapped</td>
                </tr>
                <tr>
                    <td class="type color bgr"><span></span><td>
                    <td>Color tube, red/blue guns swapped</td>
                </tr>
                <tr>
                    <td class="type mono"><span></span><td>
                    <td>Mono tube, test with red gun</td>
                </tr>
                <tr>
                    <td class="type mono bgr"><span></span><td>
                    <td>Mono tube, test with blue gun</td>
                </tr>
                <tr>
                    <td class="type mono grb"><span></span><td>
                    <td>Mono tube, test with green gun</td>
                </tr>
            </tbody>
        </table>
        <p id="dismiss">Click or tap to dismiss</p>
    </div>

    <script type="text/javascript">
        include(monitor.js.o)
    </script>
</body>
</html>
