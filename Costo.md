
Objetivo del sistema

Mi sistema genera 1 número por segundo durante un año. Son 31,536,000 números. Elegí 1 número por segundo porque es lo más fácil de explicar y de costear.




Fuente de física de aleatoriedad

El ruido del sensor de una cámara. La cámara queda fija y graba en vivo todo el año.



Arquitectura del sistema

1. Captura: Una cámara fija conectada a una Raspberry Pi graba en vivo todo el tiempo

2. Procesamiento: La Raspberry Pi corre el mismo código de mi prototipo, cada segundo toma un frame y lo resta con el anterior. Se queda con el último bit de cada valor y le aplica el hashing de SHA 256. Cada hash da 32 bytes y el sistema publica 1. El mismo equipo llegaría hasta 32 números por segundo sin gastar más

3. Cada minuto la Raspberry Pi manda 60 números en una sola petición a un Worker de Cloudflare

4. Almacenamiento: El Worker guarda los números en una base de datos D1

5. Entrega: Otra ruta del Worker funciona como API, quien necesite los números los pide ahí

6. Respaldo y monitoreo: Se toma en cuenta la compra de un segundo equipo igual por si falla el primero en algun momento, una batería por si se va la luz y una alerta si pasan unos minutos sin recibir datos




Volumen de datos

1. Números por año: 31,536,000

2. Tamaño por año, con 1 byte por número: 31.5 MB

3. Filas escritas en D1 por día con un equipo: 86,400

4. Filas escritas en D1 por día con dos equipos: 172,800

5. Peticiones al Worker por mes, con 1 por minuto: 43,200

El plan de pago de Cloudflare incluye 10 millones de peticiones al mes. D1 en el plan gratis permite 100,000 filas escritas por día. Un equipo con una fila por número usa 86,400. 2 equipos usan 172,800. El plan de pago incluye 50 millones de filas al mes.



Presupuesto a un año

1. Raspberry Pi 5 de 4 GB (precio de amazon): 110 dólares

2. Cámara Camera Module 3 (precio de amazon): 40 dólares

3. Fuente, caja y microSD (precio de amazon): 40 dólares

4. Batería de respaldo (precio de amazon): 50 dólares

5. Cloudflare Workers y D1, plan de pago a 5 dólares por 12 meses: 60 dólares

7. Electricidad: 14 dólares. Son 8 W todo el año, 70 kWh aproximadamente. La trifa de EEGSA: Q1.51 por kWh.

8. Internet para el proyecto a 30 dólares al mes: 360 dólares

Subtotal: 684 dólares


Fuentes

ttps://developers.cloudflare.com/workers/platform/pricing/

 https://developers.cloudflare.com/d1/platform/pricing/

Raspberry Pi 5 y Pi 4
 https://raspberry.tips/en/raspberrypi-einsteiger/
 raspberry-pi-5-vs-pi-4-comparison-upgrade

Raspberry Pi Camera Module 3
 https://m.reach.dog/shop/vilroscom/products/raspberry-pi-camera-3

 https://cnee.gob.gt/wp-content/uploads/2026/07/Comunicado-CNEE-tarifas-trimestrales-agosto-a-octubre.pdf