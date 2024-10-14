"use strict";
class Veicolo {
    constructor(Marca, Modello, velM, Targa) {
        this.marca = Marca;
        this.modello = Modello;
        this.velocitaMax = velM;
        this.targa = Targa;
    }
    descrizione() {
        console.log("la macchina è il modello: " + this.modello + " del marchio " + this.marca + " può raggiungere una velocità di " + this.velocitaMax + "km/h");
    }
   
}
class Auto extends Veicolo {
    constructor(Marca, Modello, velM, Targa, numPorte) {
        super(Marca, Modello, velM, Targa);
        this.numPorte = numPorte;
    }
    descrizione() {
        console.log("la macchina è il modello: " + this.modello + " del marchio " + this.marca + " ha un numero di porte di " + this.numPorte + " e può raggiungere una velocità di " + this.velocitaMax + "km/h");
    }
}
class Moto extends Veicolo {
    constructor(Marca, Modello, velM, Targa, Manubrio) {
        super(Marca, Modello, velM, Targa);
        this.manubrio = Manubrio;
    }
    descrizione() {
        console.log("la moto è il modello: " + this.modello + " del marchio " + this.marca + " ha un manubrio di tipo " + this.manubrio + " e può raggiungere una velocità di " + this.velocitaMax + "km/h");
    }
}
const bmw = new Veicolo("bmw", "ztg", 190, "4tgg54");
bmw.descrizione();
console.log("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
const panda = new Auto("Fiat", "Panda", 410, "Destroyer", 4);
panda.descrizione();
console.log("tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")
const vespa = new Moto("Piaggio", "Vespa", 300, "35tgf", "standard");
vespa.descrizione();
