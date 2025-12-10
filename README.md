# Tarea-11-Odoo
1. Descripción del módulo

Este módulo permite gestionar paquetes, camiones y actualizaciones de envíos dentro de una empresa de transportes.
Incluye tres modelos: paquetes, camiones y seguimientos.

2. Estructura del módulo
gestion_camiones/
  __init__.py
  __manifest__.py
  models/
    paquete.py
    seguimiento.py
    camion.py
    __init__.py
  security/
    ir.model.access.csv
  views/
    paquete_views.xml
    camion_views.xml
    menu.xml

3. Modelos
Paquete (paqueteria_paquete)
Campos principales:
tracking_number
sender_id
recipient_id
datos de dirección
truck_id
update_ids (One2many hacia Seguimiento)
Seguimiento (paqueteria_seguimiento)
package_id (Many2one a Paquete)
date
state
note
Camión (paqueteria_camion)
plate
current_driver_id
previous_driver_ids
last_itv_date
maintenance_notes
package_ids (One2many a Paquetes)

5. Funcionamiento básico

Un paquete tiene varias actualizaciones.(one to many)
Un paquete va en un camión.(one to one)
Un camión puede transportar varios paquetes.(one to many)
Las actualizaciones se muestran como una lista dentro del formulario del paquete.
Las listas se muestran con <list> en Odoo 18 ya que con tree genera errores.

5. Vistas
El módulo incluye:
Vistas lista y formulario para Paquetes
Vistas lista y formulario para Camiones
Menú principal con dos opciones: Paquetes y Camiones

6. Seguridad
El archivo ir.model.access.csv permite que los usuarios internos puedan crear, leer, modificar y borrar paquetes, seguimientos y camiones.

7. Instalación
Copiar el módulo en la carpeta de addons.
Reiniciar Odoo.
Activar modo desarrollador.
Actualizar lista de aplicaciones.
Instalar "Gestión de Camiones".

8. Uso

En “Paquetes” se crean los paquetes y sus actualizaciones.

En “Camiones” se registran los camiones y los paquetes que transportan.
