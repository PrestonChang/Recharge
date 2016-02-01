/// <reference path="./typings/googlemaps/google.maps.d.ts" />
var ChargingStation = (function () {
    function ChargingStation(lat, lon, address, operator) {
        this.lat = lat;
        this.lon = lon;
        this.address = address;
        this.operator = operator;
    }
    ChargingStation.prototype.getLatitude = function () {
        return this.lat;
    };
    ChargingStation.prototype.getLongitude = function () {
        return this.lon;
    };
    ChargingStation.prototype.getAddress = function () {
        return this.address;
    };
    ChargingStation.prototype.getOperator = function () {
        return this.operator;
    };
    return ChargingStation;
})();
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
