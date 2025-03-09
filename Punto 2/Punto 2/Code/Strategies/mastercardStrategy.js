class MasterCardStrategy {
    static calcularInteres(banco, cuotas) {
        return 0.018 * cuotas;
    }
}

module.exports = MasterCardStrategy;
