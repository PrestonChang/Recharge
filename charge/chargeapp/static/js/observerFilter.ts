/// <reference path="./typings/googlemaps/google.maps.d.ts" />

declare var stationIDs:any[]; 
declare var latitudes:any[];
declare var longitudes:any[];
declare var addresses:any[];
declare var operators:any[];

interface Observer {

	notify (arg:any); 

}

interface Subject {

	private observers: Observer [];
	
	registerObserver(observer : Observer) {
		this.observers.push(observer);
	}

	removeObserver(observer : Observer) {
		this.observers.splice(this.observers.indexof(observer), 1);
	}

	notifyObservers(arg : any) {
		this.observers.forEach((observer : Observer)=> {
			observer.notify(arg);
		})

	}

	getState() {
		//get state of subject
		return true; //change this later
	}
}


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

class Filter implements Subject {
	
	contructor() {
		super();
	}

	getDistanceFromLatLon(lat1: number, lon1: number, lat2: number, lon2: number) {
		var Radius = 6371; //Radius of Earth in Km
		var dLat = deg2rad(lat2-lat1);
		var dLon = deg2rad(lon2-lon1);

		var a = 
			Math.sin(dLat/2) * Math.sin(dLat/2) +
			Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
			Math.sin(dLon/2) * Math.sin(dLon/2);
		var c = 2 * Math.atan2(Math.sqrt(a)), Math.sqrt(1-a));
		var d = R * c; //Distance in Km
		return d

	}

	deg2rad(deg) {
		return deg * (Math.PI/180);
	}

	//TODO test filtering
	filterByLocation(userLatitude: number, userLongitude: number, range: string) {

		var filteredStations = []

		for(var n = 0; n < stationIDs.length; n++) { 
			var distance = getDistanceFromLatLon(userLatitude, userLongitude, latitudes[n], longitudes[n]);
			if(distance <= range) {
				var station = new ChargingStation(latitudes[n], longitudes[n], addresses[n], operators[n]);
				allStations.push(station);
			}

		}

		return filterStations;

	}

	


}

function getAllChargingStations() {
	var allStations = [];
	for(var n = 0; n < stationIDs.length; n++) { 
		var station = new ChargingStation(latitudes[n], longitudes[n], addresses[n], operators[n]);
		allStations.push(station);
	}
	return allStations;
}


module Mapping {

	export class GoogleMap implements Observer {

		public name: string;
		private map: any;
		private options: any;

		contructor(mapDiv: Element) {

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

		notify(arg:any) {
		//notify subject
		}

	}
}

class List implements Observer {

	constructor() {}

	notify(arg:any) {
		//notify subject
	}
	
}



/*
function printStations() {
	var station = new ChargingStation(latitudes[0], longitudes[0], addresses[0], operators[0]);
	var chargeStations = [];
	chargeStations = getAllChargingStations();
    //return "Here is a list of stations in typescript: " + stations[0];
    //return "Here is a list of stations in typescript: " + latitudes[0];
    //return "Here is a list of stations in typescript: " + station.getAddress();
    return "Here is a list of stations in typescript: " + chargeStations[0].getAddress();
}
 
document.body.innerHTML = printStations();
*/

