from odoo import models, fields


class Paquete(models.Model):
    _name = "paqueteria_paquete"
    _description = "Paquete de transporte"

    tracking_number = fields.Char(
        string="Número de seguimiento",
        required=True,
        help="Código de seguimiento del paquete (Código 128).",
    )

    sender_id = fields.Many2one(
        "res.partner",
        string="Remitente",
        required=True,
    )

    recipient_id = fields.Many2one(
        "res.partner",
        string="Destinatario",
        required=True,
    )

    delivery_country_id = fields.Many2one(
        "res.country",
        string="País de entrega",
    )

    delivery_state_id = fields.Many2one(
        "res.country.state",
        string="Región",
    )

    delivery_city = fields.Char(
        string="Municipio",
    )

    delivery_street = fields.Char(
        string="Calle",
    )

    delivery_number = fields.Char(
        string="Número",
    )

    delivery_extra = fields.Char(
        string="Datos adicionales",
    )

    truck_id = fields.Many2one(
        "paqueteria_camion",
        string="Camión",
    )

    update_ids = fields.One2many(
        "paqueteria_seguimiento",
        "package_id",
        string="Actualizaciones del envío",
    )
