# -*- coding: utf-8 -*-
from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class Category(models.Model):
    _name = "dzexpert_manage_modules.category"
    _description = "Catégorie de tâche"
    name = fields.Char("Nom")


class Poste(models.Model):
    _name = "dzexpert_manage_modules.poste"
    _description = "Poste"
    name = fields.Char("Nom")



class Task(models.Model):
    _name = "dzexpert_manage_modules.task"
    _description = "Poste"
    name = fields.Char("Nom", required=True)
    description = fields.Text("Description", required=True)
    category_id = fields.Many2one(
        "dzexpert_manage_modules.category", string="Categorie"
    )
    poste_id = fields.Many2one("dzexpert_manage_modules.poste", string="Poste")
    parent_id = fields.Many2one("dzexpert_manage_modules.task", string="Parent")
    dependent_tasks_ids = fields.One2many(
        "dzexpert_manage_modules.task",
        "parent_id",
        string="Tâches dépendantes",
    )
