class CuentaAhorros {
    constructor(saldoInicial) {
        this.saldo = saldoInicial;
        this.retirosSemana = 0;
    }

    depositar(monto) {
        this.saldo += monto;
        if (monto > 5 * 1000) {
            console.log("Depósito alto, informando a control de lavado de dinero De la DIAN.");
        }
    }

    retirar(monto) {
        if (this.retirosSemana >= 2) {
            console.log("Límite de retiros alcanzado.");
            return false;
        }

        if (monto > 10 * 1000) {
            if (!Autorizador.solicitarAutorizacion()) {
                console.log("Retiro no autorizado.");
                return false;
            }
        }

        if (this.saldo >= monto) {
            this.saldo -= monto;
            this.retirosSemana++;
            console.log("Retiro exitoso.");
        } else {
            console.log("Saldo insuficiente.");
        }
    }

    saldo() {
        return this.saldo;
    }
}

class Autorizador {
    static solicitarAutorizacion() {
        console.log("Solicitud de autorización en proceso...");
        return true; // Simulación de aprobación automática
    }
}

// Ejemplo de uso
let cuenta = new CuentaAhorros(20000);
cuenta.depositar(6000); // Debería informar sobre el depósito alto
cuenta.retirar(5000);   // Retiro normal
cuenta.retirar(15000);  // Requiere autorización
cuenta.retirar(2000);   // Límite de retiros alcanzado
