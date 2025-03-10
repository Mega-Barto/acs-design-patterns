const readline = require('readline');
const Calculator = require('./calculator');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Ingrese el precio del producto: ", (precio) => {
    rl.question("Ingrese la cantidad de cuotas: ", (cuotas) => {
        rl.question("Ingrese la marca de la tarjeta (Visa/MasterCard): ", (marca) => {
            rl.question("Ingrese el banco emisor: ", (banco) => {
                const resultado = Calculator.calcularPrecioCuotas(parseFloat(precio), parseInt(cuotas), marca, banco);
                if (resultado) {
                    console.log("Precio total en cuotas:", resultado.precioCuotas.toFixed(2));
                    console.log("Monto por cuota:", resultado.montoCuota.toFixed(2));
                }
                rl.close();
            });
        });
    });
});
