const LimiteRetirosHandler = require("../Handlers/LimiteRetirosHandler");
const AutorizacionRetirosHandler = require("../Handlers/AutorizacionRetirosHandler");
const ControlLavadoHandler = require("../Handlers/ControlLAvadoHandler");

class CuentaAhorros {
    constructor(saldoInicial) {
        this.saldo = saldoInicial;
        this.retirosSemana = 0;
    }

    procesarOperacion(tipo, monto) {
        let handlerChain = new LimiteRetirosHandler(this);
        handlerChain
            .setNext(new AutorizacionRetirosHandler())
            .setNext(new ControlLavadoHandler());

        let request = { tipo, monto };
        if (!handlerChain.handle(request)) {
            return;
        }

        if (tipo === "retiro") {
            if (this.saldo >= monto) {
                this.saldo -= monto;
                this.retirosSemana++;
                console.log("Retiro exitoso.");
            } else {
                console.log("Saldo insuficiente.");
            }
        } else if (tipo === "deposito") {
            this.saldo += monto;
        }
    }

    saldo() {
        return this.saldo;
    }
}

module.exports = CuentaAhorros;
