# -*- coding: utf-8 -*-
{
    "name": "Gestion de camiones",
    "version": "1.0",
    "summary": "Gestión de paquetes, camiones y seguimiento de envíos",
    "author": "Sonia",
    "category": "Operations",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/paquete_views.xml",
        "views/camion_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
