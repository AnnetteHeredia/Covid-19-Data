var myMap = L.map("map", {
    center: [0,0],
    zoom: 0
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

d3.json('all.geojson').then(function(data) {
    L.geoJson(data).addTo(myMap);
})