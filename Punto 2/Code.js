// Calculadora de Precios de Productos con Cuotas

// Clase de Emisor de Tarjeta de Crédito
class EmisorTarjetaCredito {
    constructor(nombre) {
        this.nombre = nombre;
    }

    // Método para calcular tasas de interés
    calcularInteres(numeroCuotas, precioProdcuto) {
        // Cálculo de interés simple por defecto
        const tasaInteresBase = this.obtenerTasaInteresBase(numeroCuotas);
        return precioProdcuto * tasaInteresBase * numeroCuotas;
    }

    // Obtener tasa de interés base según número de cuotas
    obtenerTasaInteresBase(numeroCuotas) {
        // Lógica de tasas de interés de ejemplo
        if (numeroCuotas <= 3) return 0.02; // 2% para 3 o menos cuotas
        if (numeroCuotas <= 6) return 0.03; // 3% para 4-6 cuotas
        return 0.04; // 4% para más de 6 cuotas
    }
}

// Clase de Marca de Tarjeta de Crédito
class MarcaTarjetaCredito {
    constructor(nombre) {
        this.nombre = nombre;
    }

    // Método para aplicar descuentos específicos de la marca
    aplicarDescuentoMarca(precioBase, numeroCuotas) {
        // Lógica de descuentos específica de la marca
        switch(this.nombre.toLowerCase()) {
            case 'visa':
                return numeroCuotas > 6 ? precioBase * 0.95 : precioBase;
            case 'mastercard':
                return numeroCuotas <= 3 ? precioBase * 0.98 : precioBase;
            default:
                return precioBase;
        }
    }
}

// Calculadora de Precios de Productos
class CalculadoraPreciosProductos {
    constructor() {
        this.productos = {
            'laptop': 1000,
            'smartphone': 500,
            'tablet': 300
        };
    }

    // Calcular precio en cuotas
    calcularPrecioCuotas(nombreProducto, numeroCuotas, marcaTarjeta, emisorTarjeta) {
        // Validar entradas
        if (!this.productos[nombreProducto]) {
            throw new Error('Producto no encontrado');
        }

        if (numeroCuotas <= 0) {
            throw new Error('El número de cuotas debe ser mayor que cero');
        }

        const precioContado = this.productos[nombreProducto];
        
        // Crear instancias de marca y emisor de tarjeta
        const marca = new MarcaTarjetaCredito(marcaTarjeta);
        const emisor = new EmisorTarjetaCredito(emisorTarjeta);

        // Aplicar descuentos específicos de la marca
        const precioConDescuento = marca.aplicarDescuentoMarca(precioContado, numeroCuotas);

        // Calcular interés
        const montoInteres = emisor.calcularInteres(numeroCuotas, precioConDescuento);
        
        // Precio total incluyendo interés
        const precioTotal = precioConDescuento + montoInteres;
        
        // Calcular monto de cada cuota
        const montoCuota = precioTotal / numeroCuotas;

        return {
            precioContado: precioContado.toFixed(2),
            precioTotal: precioTotal.toFixed(2),
            montoInteres: montoInteres.toFixed(2),
            montoCuota: montoCuota.toFixed(2),
            numeroCuotas: numeroCuotas
        };
    }

    // Listar productos disponibles
    obtenerProductosDisponibles() {
        return Object.keys(this.productos);
    }
}

// Ejemplo de uso
const calculadora = new CalculadoraPreciosProductos();

// Función para simular interacción con el usuario
function calcularCuotasProducto(nombreProducto, numeroCuotas, marcaTarjeta, emisorTarjeta) {
    try {
        const resultado = calculadora.calcularPrecioCuotas(nombreProducto, numeroCuotas, marcaTarjeta, emisorTarjeta);
        
        console.log(`Producto: ${nombreProducto}`);
        console.log(`Precio al contado: $${resultado.precioContado}`);
        console.log(`Precio total (Cuotas): $${resultado.precioTotal}`);
        console.log(`Monto de interés: $${resultado.montoInteres}`);
        console.log(`Número de cuotas: ${resultado.numeroCuotas}`);
        console.log(`Monto de cada cuota: $${resultado.montoCuota}`);
        
        return resultado;
    } catch (error) {
        console.error('Error al calcular cuotas:', error.message);
    }
}

// Demostración
calcularCuotasProducto('laptop', 6, 'Visa', 'Banco A');
calcularCuotasProducto('smartphone', 3, 'Mastercard', 'Banco B');