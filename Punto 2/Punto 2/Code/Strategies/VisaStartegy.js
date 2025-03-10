class VisaStrategy {
    static calcularInteres(banco, cuotas) {
        if (banco === "Banco A") return 0.02 * cuotas;
        if (banco === "Banco B") return 0.015 * cuotas;
        return 0.018 * cuotas;
    }
}

module.exports = VisaStrategy;
