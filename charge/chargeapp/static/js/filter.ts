/// <reference path="./typings/googlemaps/google.maps.d.ts" />

declare var stationIDs:any[]; 
declare var latitudes:any[];
declare var longitudes:any[];
declare var addresses:any[];
declare var operators:any[];


class ChargingStation {

	private lat: number;
	private lon: number;
	private address: string;
	private operator: string;

	constructor(lat: number, lon: number, address: string, operator: string) {
		this.lat = lat;
		this.lon = lon;
		this.address = address;
		this.operator = operator;
	}

	getLatitude() {
		return this.lat;
	}

	getLongitude() {
		return this.lon;
	}

	getAddress() {
		return this.address;
	}

	getOperator() {
		return this.operator;
	}

}

/* Not compiling for some reason
class Filter {

	constructor() {

	}

	degToRad(deg) {
		return deg * (Math.PI/180);
	}

	function getDistanceFromLatLon(lat1, lon1, lat2, lon2) {
		var Radius = 6371; //Radius of Earth in Km
		var dLat = degToRad(lat2-lat1);
		var dLon = degToRad(lon2-lon1);

		var a = 
			Math.sin(dLat/2) * Math.sin(dLat/2) +
			Math.cos(degToRad(lat1)) * Math.cos(degToRad(lat2)) *
			Math.sin(dLon/2) * Math.sin(dLon/2);
		var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
		var d = Radius * c; //Distance in Km
		return d;

	}

	//TODO test filtering
	function filterByLocation(userLatitude, userLongitude, range) {

		var filteredStations = [];

		for(var n = 0; n < stationIDs.length; n++) { 
			var distance = getDistanceFromLatLon(userLatitude, userLongitude, latitudes[n], longitudes[n]);
			if(distance <= range) {
				var station = new ChargingStation(latitudes[n], longitudes[n], addresses[n], operators[n]);
				filteredStations.push(station);
			}

		}

		return filteredStations;

	}
}
*/

/*
function getAllChargingStations() {
	var allStations = [];
	for(var n = 0; n < stationIDs.length; n++) { 
		var station = new ChargingStation(latitudes[n], longitudes[n], addresses[n], operators[n]);
		allStations.push(station);
	}
	return allStations;
}
*/

/* Used for testing
function printStations() {

	//var station = new ChargingStation(latitudes[0], longitudes[0], addresses[0], operators[0]);
	//var chargeStations = [];
	//chargeStations = getAllChargingStations();
    return "Here is a list of stations in typescript: " + stationIDs[0];
    //return "Here is a list of stations in typescript: " + latitudes[0];
    //return "Here is a list of stations in typescript: " + station.getAddress();
    //return "Here is a list of stations in typescript: " + chargeStations[0].getAddress();
}

 document.body.innerHTML = printStations();

*/

/*
module Mapping {

	export class GoogleMap {

		public name: string;
		private map: any;
		private options: any;

		constructor(mapDiv: Element) {

			this.name = "GoogleMap";

			this.options = {
			    center:new google.maps.LatLng(49.2827,-123.1207),
			    zoom:12,
			    mapTypeId:google.maps.MapTypeId.ROADMAP
			 };

  			this.map = new google.maps.Map(mapDiv, this.options);
  			//google.maps.event.addDomListener(window, 'load', initialize);

  			//addMarkers(map);
		}
	}
}
*/


