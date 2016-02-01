/// <reference path="./typings/googlemaps/google.maps.d.ts" />


interface Observer {

	notify (arg:any); 

}

interface Subject {

	private observers: Observer [];
	
	function registerObserver(observer : Observer): void {
		this.observers.push(observer);
	}

	function removeObserver(observer : Observer) : void {
		this.observers.splice(this.observers.indexof(observer), 1);
	}

	function notifyObservers(arg : any): void {
		this.observers.forEach((observer : Observer)=> {
			observer.notify(arg);
		})

	}

	function getState() {
		//get state of subject
		return true;
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

class Filter implements Subject{


	contructor() {
		super();
	}

	//filter by location
		//notifyObservers

	//filter by attributes

}

class Map implements Observer {

	constructor() {}

	notify(arg:any) {
		//notify map and list
	}
	
}

class List implements Observer {

	constructor() {}

	notify(arg:any) {
		//notify map and list
	}
	
}

