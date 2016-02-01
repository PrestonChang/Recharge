/// <reference path="./typings/googlemaps/google.maps.d.ts" />

declare var stationIDs: any[]; 
declare var latitudes: any[];
declare var longitudes: any[];
declare var addresses: any[];
declare var operators: any[];


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



function printStations() {
	//var station = new ChargingStation(latitudes[0], longitudes[0], addresses[0], operators[0]);
	//var chargeStations = [];
	//chargeStations = getAllChargingStations();
    //return "Here is a list of stations in typescript: " + stations[0];
    return "Here is a list of stations in typescript: " + latitudes[0];
    //return "Here is a list of stations in typescript: " + station.getAddress();
    //return "Here is a list of stations in typescript: " + chargeStations[0].getAddress();
}
 
document.body.innerHTML = printStations();


