from odoo import models, fields


class Seguimiento(models.Model):
    _name = "paqueteria_seguimiento"
    _description = "Actualización del envío"

    package_id = fields.Many2one(
        "paqueteria_paquete",
        string="Paquete",
        required=True,
        ondelete="cascade",
    )

    date = fields.Datetime(
        string="Fecha",
        required=True,
        default=fields.Datetime.now,
    )

    state = fields.Selection(
        [
            ("preparacion", "En preparación"),
            ("transito", "En tránsito"),
            ("reparto", "En reparto"),
            ("entregado", "Entregado"),
            ("incidencia", "Con incidencia"),
        ],
        string="Estado",
        required=True,
        default="preparacion",
    )

    note = fields.Text(
        string="Notas adicionales",
    )
