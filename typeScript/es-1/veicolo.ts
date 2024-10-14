class Veicolo{
    marca:string;
    modello:string;
    velocitaMax:number;
    targa:string;
    constructor(Marca:string,Modello:string, velM:number, Targa:string){
       this.marca=Marca;
       this.modello=Modello;
       this.velocitaMax=velM;
       this.targa=Targa;
    }
    descrizione(this:Veicolo):void{
        console.log("la macchina è il modello: "+this.modello+" del marchio "+this.marca+" può raggiungere una velocità di "+this.velocitaMax+"km/h")
        
    }
    oid():void{
        console.log("tttttttttttttttttt")
    }
}
class Auto extends Veicolo{
    numPorte:number
    constructor(Marca:string,Modello:string, velM:number, Targa:string, numPorte:number){
        super(Marca, Modello, velM, Targa)
        this.numPorte=numPorte
    }
    descrizione(this: Auto): void {
        console.log("la macchina è il modello: "+this.modello+" del marchio "+this.marca+" ha un numero di porte di "+this.numPorte+ " e può raggiungere una velocità di "+this.velocitaMax+"km/h")
    }
}
class Moto extends Veicolo{
    manubrio:string
    constructor(Marca:string,Modello:string, velM:number, Targa:string, Manubrio:string){
        super(Marca, Modello, velM, Targa)
        this.manubrio=Manubrio;
    }
    descrizione(this: Moto): void {
        console.log("la moto è il modello: "+this.modello+" del marchio "+this.marca+ " ha un manubrio di tipo "+this.manubrio+ " e può raggiungere una velocità di "+this.velocitaMax+"km/h")
        
    }
}
const bmw= new Veicolo("bmw","ztg",190,"4tgg54")
bmw.descrizione();
bmw.oid();
const panda= new Auto("Fiat","Panda",410,"Destroyer",4)
panda.descrizione();
const vespa= new Moto("Piaggio","Vespa", 300,"35tgf","standard")
vespa.descrizione();