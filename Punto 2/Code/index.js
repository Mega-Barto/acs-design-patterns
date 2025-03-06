const CuentaAhorros = require("./Models/CuentaAhorros");

console.log(" Iniciando sistema de caja de ahorros...");

let cuenta = new CuentaAhorros(20000);

cuenta.procesarOperacion("deposito", 6000); //  Informa a control de lavado de dinero
cuenta.procesarOperacion("retiro", 5000);   //  Retiro normal
cuenta.procesarOperacion("retiro", 15000);  //  Requiere autorización
cuenta.procesarOperacion("retiro", 2000);   //  Límite de retiros alcanzado

console.log(" Saldo final:", cuenta.saldo());
