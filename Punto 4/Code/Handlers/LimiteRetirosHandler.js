const Handler = require("./Handler");

class LimiteRetirosHandler extends Handler {
    constructor(cuenta) {
        super();
        this.cuenta = cuenta;
    }

    handle(request) {
        if (request.tipo === "retiro" && this.cuenta.retirosSemana >= 2) {
            console.log("❌ Límite de retiros alcanzado.");
            return false;
        }
        return super.handle(request);
    }
}

module.exports = LimiteRetirosHandler;
