
window.onload = function(){
	// create a map in the "map" div, set the view to a given place and zoom
	var world = [
		[100,-100],
		[-44,155]
	];
	var allowedCountries = {};
	var map = L.map('map',{minZoom:2})
		.fitBounds(world);
    d3.json('/allgeojson').then(function(json) {
      // For console log to see the geojson
    var test = d3.json('/world_leaf_api')
		L.geoJson(json,{
		    clickable:true,
		    style: function(item){
          // defines the lines on the map
		    	if(item.properties.type == 'stateline'){
		    		return {
					    fill:false,
					    stroke:true,
					    color:'#EAEAEA',
					    weight:2
					}

		    	} if(item.geometry.type == 'Point'){
		    		if(item.properties.importance > 1){
		    			return {
		    				fill:false,
		    				stroke:false
		    			}
		    		}

		    		return {
			        	fill:true,
			        	fillOpacity:1,
			        	stroke:false,
			        	fillColor:"#aaa",
			        	radius: 2 / item.properties.importance
		       		}

		        } else {
		    		return {
					    fillColor:'#fff',
					    fillOpacity:1,
					    fill:true,
					    // color:'#eeeeff',
					    weight:1
					}
		    	}
		    },
		    pointToLayer: function (feature, latlng) {
		        return L.circleMarker(latlng)
		        	.bindLabel(feature.properties.name,{
		        		noHide:true
		        	});
		    },
		    onEachFeature: function (feature, layer) {
          // Get name of the country
		    	var name = feature.properties.name;
          // Get the first cordinate ... Not sure if I need this
          var cord = feature.geometry.coordinates[0][0][0]
		    	function ctxFillColor(){
            // Do not highlight after the click.
		    		return allowedCountries[name] ? '#FFFFFF' : '#FFFFFF';
		    	}
		    	layer.on('click',function(){
			    	allowedCountries[name] = !allowedCountries[name];
			    	console.log(name)
            console.log(cord)
            // var newMarker = new L.marker(cord).addTo(map);
			    	layer.setStyle({
			    		fillColor: ctxFillColor()
			    	});
		    	});

		    	layer.on('mouseover',function(){
		    		layer.setStyle({
		    			fillColor: '#ffaaff'
		    		})
            // console.log(feature.properties.name)
		    	})

		    	layer.on('mouseout',function(){
		    		layer.setStyle({
		    			fillColor: ctxFillColor()
		    		})
		    	})
          // This will add a pop up to the country that you click on.
          // TODO: Display stats
          layer.bindPopup("County: " + feature.properties.name);


		    }
		}).addTo(map);
    console.log(test[0][0])
	});

}
