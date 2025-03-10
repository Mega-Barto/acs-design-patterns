const VisaStrategy = require('./Strategies/VisaStartegy');
const MasterCardStrategy = require('./Strategies/mastercardStrategy');

class InterestFactory {
    static obtenerEstrategia(marca) {
        if (marca === "Visa") return VisaStrategy;
        if (marca === "MasterCard") return MasterCardStrategy;
        return null;
    }
}

module.exports = InterestFactory;
