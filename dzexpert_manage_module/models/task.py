# -*- coding: utf-8 -*-
from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class Category(models.Model):
    _name = "dzexpert.manage.modules.category"
    _description = "Catégorie de tâche"
    name = fields.Char("Nom")


class Poste(models.Model):
    _name = "dzexpert.manage.modules.poste"
    _description = "Poste"
    name = fields.Char("Nom")


class Task(models.Model):
    _name = "dzexpert.manage.modules.task"
    _inherit = ["mail.thread"]
    _description = "Tâche"
    name = fields.Char("Nom", required=True)
    description = fields.Text("Description", required=True)
    category_ids = fields.Many2many(
        "dzexpert.manage.modules.category",
        relation="dzexpert_manage_modules_task_category_rel",
        string="Catégories",
        required=True,
    )
    poste_ids = fields.Many2many("dzexpert.manage.modules.poste", string="Postes")
    parent_id = fields.Many2one("dzexpert.manage.modules.task", string="Parent")
    security_group_ids = fields.Many2many(
        "dzexpert.manage.modules.security.group",
        relation="dzexpert_manage_modules_task_security_grp_rel",
        string="Groupes de sécurité",
    )
    dependent_tasks_ids = fields.Many2many(
        "dzexpert.manage.modules.task",
        relation="dzexpert_manage_modules_dependent_task_rel",
        column1="task_1",
        column2="task_2",
        string="Tâches dépendantes",
    )
    module_ids = fields.Many2many("dzexpert.manage.modules.module", string="Modules")
