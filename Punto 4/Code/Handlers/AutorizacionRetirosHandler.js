const Handler = require("./Handler");
const Autorizador = require("../models/Autorizador");

class AutorizacionRetirosHandler extends Handler {
    handle(request) {
        if (request.tipo === "retiro" && request.monto > 10000) {
            console.log("⚠️ Se requiere autorización para el retiro.");
            if (!Autorizador.solicitarAutorizacion()) {
                console.log("❌ Retiro no autorizado.");
                return false;
            }
        }
        return super.handle(request);
    }
}

module.exports = AutorizacionRetirosHandler;
