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
            include(__TYPE__`'_data.js.o)
        </script>
    </head>
<body>
    <form><label for="tube">Tube</label><input type="text" name="tube" id="tube"><div id="showhelp">?</div></form>
    <div id="reference"><label for="compat">Compatible with <span id="compat"></span></label><span id="compat"></span><div id="clearReference">×</div></div>
    <table id="search">
        <thead>
            <tr>
                <th></th>
                include(__TYPE__`'_headers.html.m4)
            </tr>
        </thead>
        <tbody id="compatRes">
        <tbody id="incompatRes">
    </table>

    <div id="help">
        <h1>Monitor Helper</h1>
        <p>This is a tool to assist CRT repair and swapping. With it, you can find the adapter and settings for rejuvenating a tube, as well as determine if tubes are compatible with each other, and thus may be substituted.</p>

        <h1>Tube model numbers</h1>
        <p>The model number is usually located on a sticker on the back side of the tube. It is almost never located on the metal frame or circuit boards (chassis). Tube models come in a number of forms, but these are the most common:</p>
        <ul>
            <li><strong>19</strong>VLUP22 — <strong>19”</strong> tube</li>
            <li><strong>15</strong>ST4730R — <strong>15”</strong> tube</li>
            <li>A<strong>48</strong>LRH93X — <strong>48 cm</strong> (19”) tube</li>
            <li>A<strong>63</strong>ADT10X05 — <strong>63 cm</strong> (25”) tube</li>
        </ul>

        <h1>Searching for your tube</h1>
        <p>Type the tube model into the <emph>Tube</emph> field. The search results will update automatically as you type.</p>

        <h1>Finding a compatible tube</h1>
        <p>Clicking or tapping a search result enables compatibility filtering. In this mode, tubes which are compatible with the selected tube are displayed more prominently.</p>
        <ol>
            <li>Search for your source tube, and click or tap it in the results list. Results & <emph>Tube</emph> input will clear.</li>
            <li>Search for your potential donor tube. Compatible tubes will appear normally at the top of the search results; incompatible tubes will be greyed out at the bottom.</li>
        </ol>

        <p><strong>Tube compatibility is not a guarantee that you can swap!</strong> You must also measure the yoke resistance and possibly swap the yoke.</p>

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
