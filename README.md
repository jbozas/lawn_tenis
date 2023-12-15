#Como usuario quiero setear un horario y dia y que el bot se encargue de reservarlo a penas sea posible:
* Usuario y contraseña
* Fecha: Cualquier dia posterior a hoy, cualquier fecha.
* Single/Doble
    - En caso de que no este logeado, logearlo.
    - En caso de que no este disponible, sacar el horario mas proximo y notificar.
    - Sacar la cancha con numero de cancha menor posible.

#Requerimientos tecnicos
* Parametros del Script:
    - Usuario y contraseña
    - Jugadores
    - Fecha(dia y hora/minutos)
* Request para solicitar token
* Request para consultar disponibilidad
* Request para obtener IDs de jugadores
* Request para reservar
* Notificar al usuario - LOW Priority - Lawn notifica de por si


#@TODO:
- Crearlo como comando y hacerlo ejecutable desde consola.
- En caso de que haya un error en la reserva, notificar al usuario.
