const Handler = require("./Handler");

class ControlLavadoHandler extends Handler {
    handle(request) {
        if (request.tipo === "deposito" && request.monto > 5000) {
            console.log("⚠️ Depósito alto, informando a control de lavado de dinero.");
        }
        return super.handle(request);
    }
}

module.exports = ControlLavadoHandler;
