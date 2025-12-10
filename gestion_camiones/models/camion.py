from odoo import models, fields


class Camion(models.Model):
    _name = "paqueteria_camion"
    _description = "Camión de la flota"

    plate = fields.Char(
        string="Matrícula",
        required=True,
    )

    current_driver_id = fields.Many2one(
        "hr.employee",
        string="Conductor actual",
    )

    previous_driver_ids = fields.Many2many(
        "hr.employee",
        string="Antiguos conductores",
        relation="paqueteria_camion_driver_rel",
        column1="camion_id",
        column2="driver_id",
    )

    last_itv_date = fields.Date(
        string="Fecha última ITV",
    )

    maintenance_notes = fields.Text(
        string="Notas de mantenimiento",
    )

    package_ids = fields.One2many(
        "paqueteria_paquete",
        "truck_id",
        string="Paquetes transportados",
    )
