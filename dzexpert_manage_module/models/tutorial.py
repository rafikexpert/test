from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Topic(models.Model):
    _name = "dzexpert.manage.modules.topic"
    _inherit = ["mail.thread"]
    _description = "Topic"

    name = fields.Char(string="Nom", required=True)
    parent_id = fields.Many2one("dzexpert.manage.modules.topic", string="Parent")
    full_name = fields.Char(string="Name", compute="_compute_full_name", store=True)
    tutorial_ids = fields.Many2many(
        "dzexpert.manage.modules.tutorial",
        relation="dzexpert_manage_modules_tutorial_topic_rel",
        string="Tutoriels",
    )

    @api.depends("name", "parent_id", "parent_id.full_name")
    def _compute_full_name(self):
        for topic in self:
            full_name = topic.name
            parent = topic.parent_id
            while parent:
                full_name = "{}/{}".format(parent.name, full_name)
                parent = parent.parent_id
            topic.full_name = full_name

    def open_tutorials(self):
        return {
            "name": "{} Tutoriels".format(self.name),
            "type": "ir.actions.act_window",
            "res_model": "dzexpert.manage.modules.tutorial",
            "view_mode": "tree,form",
            "domain": [("id", "in", self.tutorial_ids.ids)],
            "flags": {"form": {"action_buttons": False}},
        }


class Link(models.Model):
    _name = "dzexpert.manage.modules.link"
    _inherit = ["mail.thread"]
    _description = "Link"

    url = fields.Char(string="Url", required=True)
    tutorial_id = fields.Many2one("dzexpert.manage.modules.tutorial", string="Tutorial")


class Video(models.Model):
    _name = "dzexpert.manage.modules.video"
    _inherit = ["mail.thread"]
    _description = "Video"

    name = fields.Char(string="Nom", required=True)
    video_url = fields.Char(string="Video URL", required=True)
    description = fields.Html(string="Description")


class Language(models.Model):
    _name = "dzexpert.manage.modules.language"
    _inherit = ["mail.thread"]
    _description = "Language"

    name = fields.Char(string="Nom", required=True)


class Tutorial(models.Model):
    _name = "dzexpert.manage.modules.tutorial"
    _inherit = ["mail.thread"]
    _description = "Tutorial"

    title = fields.Char("Title", required=True)
    tasks_ids = fields.Many2many(
        "dzexpert.manage.modules.task",
        relation="dzexpert_manage_modules_tutorial_task_rel",
        string="Tâches",
    )
    topic_ids = fields.Many2many(
        "dzexpert.manage.modules.topic",
        relation="dzexpert_manage_modules_tutorial_topic_rel",
        string="Topics",
    )
    language_id = fields.Many2one(
        "dzexpert.manage.modules.language", string="Language", required=True
    )
    level = fields.Selection(
        [
            ("easy", "Facile"),
            ("medium", "Moyen"),
            ("difficult", "Difficile"),
        ],
        string="Niveau",
    )
    content = fields.Html("Contenu")
    attachment_number = fields.Integer(
        compute="_compute_attachment_number", string="P.J."
    )
    external_link_ids = fields.One2many(
        "dzexpert.manage.modules.link",
        "tutorial_id",
        string="Liens externes",
    )
    video_ids = fields.Many2many(
        "dzexpert.manage.modules.video",
        relation="dzexpert_manage_modules_tutorial_video_rel",
        string="Videos",
    )
    related_tutorial_ids = fields.Many2many(
        "dzexpert.manage.modules.tutorial",
        relation="dzexpert_manage_modules_related_tutorial_rel",
        column1="related_toturial_1",
        column2="related_toturial_2",
        string="Tutoriels associés",
    )
    translation_ids = fields.Many2many(
        "dzexpert.manage.modules.tutorial",
        relation="dzexpert_manage_modules_translated_tutorial_rel",
        column1="translated_toturial_1",
        column2="translated_toturial_2",
        string="Tutoriels traduits",
    )

    def name_get(self):
        result = []
        for record in self:
            name = "{}, Language: {}".format(record.title, record.language_id.name)
            result.append((record.id, name))
        return result

    def _compute_attachment_number(self):
        for record in self:
            attachment_domain = [
                ("res_model", "=", "dzexpert.manage.modules.tutorial"),
                ("res_id", "=", record.id),
            ]
            record.attachment_number = self.env["ir.attachment"].search_count(
                attachment_domain
            )

    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env.ref("base.action_attachment").sudo().read()[0]
        res["domain"] = [
            ("res_model", "=", "dzexpert.manage.modules.tutorial"),
            ("res_id", "in", self.ids),
        ]
        res["context"] = {
            "create": True,
            "delete": True,
            "default_res_model": "dzexpert.manage.modules.tutorial",
            "default_res_id": self.id,
        }
        return res
