function getCharts(jsonData){
    //Get the chart values from the JSON string
    dates = jsonData.map(item => item.date);
    totCases = jsonData.map(item => item.total_cases);
    newCases = jsonData.map(item => item.new_cases);
    totDeaths = jsonData.map(item => item.total_deaths);
    newDeaths = jsonData.map(item => item.new_deaths);

    //build a placeholder for final data
    data_list = Array();

    //gather the checkboxes from the control line by element ID
    var total_cases = document.getElementById('total_Cases');
    var new_Cases = document.getElementById('new_Cases');
    var total_Deaths = document.getElementById('total_Deaths');
    var new_Deaths = document.getElementById('new_Deaths');

    //Create the summary chart
    //get the element from the webpage
    summary_table_div = d3.select("#summary_data");
    summary_table_div.html("");
    //create the table
    summary_table_div.append("table").attr("id","sum_table");
    summary_table = d3.select('#sum_table');
    header = summary_table.append("tr");
    header.append("th").text("State: "+jsonData[0].state+"  ");
    header.append("th").text("Start Date: "+dates[0]+"  ");
    header.append("th").text("End Date: "+dates[dates.length - 1]);

    //Populate relevant selected data
    if (total_cases.checked){
        //build the trace for Plotly chart
        total_case_trace = {
            x: dates,
            y: totCases,
            mode: 'lines',
            type: 'scatter',
            name: 'Total Cases'
        };
        data_list.push(total_case_trace);
    };
    if (new_Cases.checked){
        //build the trace for the Plotly chart
        new_cases_trace = {
            x: dates,
            y: newCases,
            mode: 'lines',
            type: 'scatter',
            name: 'New Cases'
        };
        data_list.push(new_cases_trace);
    };
    if (total_Deaths.checked){
        //build the trace for the Plotly chart
        total_deaths_trace = {
            x: dates,
            y: totDeaths,
            mode: 'lines',
            type: 'scatter',
            name: 'Total Deaths'
        };
        data_list.push(total_deaths_trace);
    };
    if (new_Deaths.checked){
        //build the trace for the Plotly chart
        new_deaths_trace = {
            x: dates,
            y: newDeaths,
            mode: 'lines',
            type: 'scatter',
            name: 'New Deaths'
        };
        data_list.push(new_deaths_trace);
    };

    //get the summary chart data
    //total cases
    max_tot_cases = totCases[totCases.length - 1];
    //new cases
    sum_newCases = 0;
    for(k=0;k<newCases.length;k++){
        sum_newCases = sum_newCases+newCases[k];
    }
    average_new_cases = sum_newCases/newCases.length;
    //total deaths
    max_tot_deaths = totDeaths[totDeaths.length - 1];
    //new deaths=
    sum_newDeaths = 0;
    for(l=0;l<newDeaths.length;l++){
        sum_newDeaths = sum_newDeaths+newDeaths[l];
    }
    average_new_Deaths = sum_newDeaths/newDeaths.length;

    //add the summary to the summary table
    tot_case_row = summary_table.append("tr");
    tot_row_data = tot_case_row.append("th").text("Total Cases: "+max_tot_cases);
    new_case_row = summary_table.append("tr");
    new_case_data = new_case_row.append("th").text("Average New Cases: "+average_new_cases.toFixed(2));
    tot_deaths_row = summary_table.append("tr");
    tot_deaths_data = tot_deaths_row.append("th").text("Total Deaths: "+max_tot_deaths);
    new_deaths_row = summary_table.append("tr");
    new_deaths_data = new_deaths_row.append("th").text("Average New Deaths: "+average_new_Deaths.toFixed(2));

    //add labels and title
    layout = {
        xaxis: {title: {text: 'Dates'}},
        yaxis: {title: {text: 'Count'}}
    }

    //display the graph
    Plotly.newPlot('graph', data_list, layout, {responsive:true}); 
    //NOTE: 'graph' is the id of the div tag in US_Charts_Only.html
};

function buildMap(jsonData){
    //Get the chart values from the JSON string
    state = jsonData.map(item => item.state);
    totCases = jsonData.map(item => item.total_cases);
    totDeaths = jsonData.map(item => item.total_deaths);
    country = jsonData.map(item => item.state);

    if (country[0] == 'USA'){

        //Initialize the map
        var myMap = L.map("map", {
            center: [37.09, -95.71],
            zoom: 5
          });
    
        d3.json("../static/js/state_lat_long.geojson").then((data) => {
        var features = data.features;

        for (var i = 0; i < features.length; i++) {
            var feature = features[i];
            state_name = feature.properties.State;
            state_index = state.indexOf(state_name);
            var myCoordinates = [feature.geometry.coordinates[1],feature.geometry.coordinates[0]];
            L.marker(myCoordinates)
                .bindPopup(`<h1>${feature.properties.State}</h1><p style="color:black">Total Cases: ${totCases[state_index]}</p><p style="color:black">Total Deaths: ${totDeaths[state_index]}</p>`)
                .addTo(myMap);
            };
      })}
    else{
        var world = [
            [100, -100],
            [-44, 155],
        ];
        var allowedCountries = {};
        var map = L.map("map", { minZoom: 2 }).fitBounds(world);
    // state_lat_long.geojson
    d3.json("/allgeojson").then(function (json) {
        d3.json("/world_leaf_api").then(function (data) {
        // For console log to see the geojson
        L.geoJson(json, {
            clickable: true,
            style: function (item) {
            // defines the lines on the map
            if (item.properties.type == "stateline") {
                return {
                fill: false,
                stroke: true,
                color: "#EAEAEA",
                weight: 2,
                };
            }
            if (item.geometry.type == "Point") {
                if (item.properties.importance > 1) {
                return {
                    fill: false,
                    stroke: false,
                };
                }

                return {
                fill: true,
                fillOpacity: 1,
                stroke: false,
                fillColor: "#aaa",
                radius: 2 / item.properties.importance,
                };
            } else {
                return {
                fillColor: "#fff",
                fillOpacity: 1,
                fill: true,
                // color:'#eeeeff',
                weight: 1,
                };
            }
            },
            pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng).bindLabel(feature.properties.name, {
                noHide: true,
            });
            },
            onEachFeature: function (feature, layer) {
            // Get name of the country
            var name = feature.properties.name;
            // Get the first cordinate ... Not sure if I need this
            var cord = feature.geometry.coordinates[0][0][0];
            function ctxFillColor() {
                // Do not highlight after the click.
                return allowedCountries[name] ? "#FFFFFF" : "#FFFFFF";
            }
            layer.on("click", function () {
                allowedCountries[name] = !allowedCountries[name];


                function searchMe(name) {
                for (let i = 0; i < data.length; i++) {
                    if (data[i][0] == name) {
                    console.log("Found you! " + name);
                    return i
                    }
                }
                }

                console.log(searchMe(name));
                country = searchMe(name)
                layer.setStyle({
                fillColor: ctxFillColor(),
                });
                layer.bindPopup('<p style="color:black">You are here '+ name + '<p><br>' +
                '<p style="color:black">Total Cases: ' + data[country][1]  + '<p><br>' +
                '<p style="color:black">Total Deaths: ' + data[country][2]+'<p>');
            });

            layer.on("mouseover", function () {

                layer.setStyle({
                fillColor: "#ffaaff",
                });
                // console.log(feature.properties.name)
            });

            layer.on("mouseout", function () {
                layer.setStyle({
                fillColor: ctxFillColor(),
                });
            });
            console.log(typeof data);

            console.log()
            },
        }).addTo(map);
        });
    });
        }

        // Add a tile layer.
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(myMap);
};