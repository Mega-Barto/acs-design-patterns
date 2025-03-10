const InterestFactory = require('./InteresFactory');

class Calculator {
    static calcularPrecioCuotas(precio, cuotas, marca, banco) {
        const Estrategia = InterestFactory.obtenerEstrategia(marca);
        if (!Estrategia) {
            console.log("Marca de tarjeta no válida");
            return null;
        }
        
        const intereses = Estrategia.calcularInteres(banco, cuotas);
        const precioCuotas = precio * (1 + intereses);
        const montoCuota = precioCuotas / cuotas;
        
        return { precioCuotas, montoCuota };
    }
}

module.exports = Calculator;
