


d3.json('state_lat_long.geojson').then((data) => {
  // console.log(data);
  var features = data.features
  console.log(features)
  // var latitude = data.features[0]
  //creating a path to get to coordinates. we use forEach() funciton to do this and call it location
  // features.forEach((feature) => {
  //     state = feature.properties.State
  //     location
  //     console.log(state)
  // })

  for (var i = 0; i < features.length; i++) {
    var feature = features[i];
    var myCoordinates = [feature.geometry.coordinates[1],feature.geometry.coordinates[0]]
    console.log(myCoordinates)
    L.marker(myCoordinates)
      .bindPopup(`<h1>${feature.properties.State}</h1>`) //<hr> <h3>Population ${city.population.toLocaleString()}</h3>`)
      .addTo(myMap);
  }
  // fetch('United_States_COVID-19_Cases_and_Deaths_by_State_over_Time (1).csv').then(function(response){
  //   //console.log(response) //just a promise
  //     return response.text();
  // }).then(function(text){
  //     //console.log(text)
  //     var lines = text.split("\n");
  //     for (var a = 1; a < lines.length; a++) {
  //     var line = lines[a];
  //     var parts = line.split(",");
  //       for (var l = 0; l < parts.length; l++) {
  //        var part =parts[l]
  //         console.log(part)
  //       }
  //     }
  //     // Handling of the text contents goes here
  // }).catch(function(err){
  //     // Error handling goes here (e.g. the network request failed, etc)
  // })
  
  //testfunction(data)
}) 



// function testfunction(testdata) {
//   console.log("I am in test function")

//   console.log(testdata)
// }


// getLong = d3.json('state_lat_long.geojson').then((data) => {
//   // console.log(data);
//   var features = data.features
//   console.log(features)
//   // var latitude = data.features[0]
//   //creating a path to get to coordinates. we use forEach() funciton to do this and call it location
//   features.forEach((location) => {
//       longitude = location.geometry.coordinates[0]
//       // console.log(longitude)
//   })
// })
// console.log(getLong)



// getLat = d3.json('state_lat_long.geojson').then((data) => {
//   // console.log(data);
//   var features = data.features
//   console.log(features)
//   // var latitude = data.features[0]
//   //creating a path to get to coordinates. we use forEach() funciton to do this and call it location
//   features.forEach((location) => {
//       longitude = location.geometry.coordinates[1]
//       // console.log(longitude)
//   })
// })
// console.log(getLat)

// Create a map object.
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});


// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);
