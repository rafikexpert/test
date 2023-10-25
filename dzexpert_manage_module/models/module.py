from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)


class SecurityGroup(models.Model):
    _name = "dzexpert.manage.modules.security.group"
    _inherit = ["mail.thread"]
    _description = "Groupe de sécurité"

    name = fields.Char("Nom", required=True)
    technical_name = fields.Char("Nom technique", required=True)
    module_id = fields.Many2one("dzexpert.manage.modules.module", string="module")
    type = fields.Selection(
        [
            ("app", "App"),
            ("technical", "Technique"),
        ],
        string="type",
    )


class Email(models.Model):
    _name = "dzexpert.manage.modules.email"
    _inherit = ["mail.thread"]
    _description = "Email"

    name = fields.Char("Nom", help="Nom du template", required=True)
    module_id = fields.Many2one("dzexpert.manage.modules.module", string="module")


class Menu(models.Model):
    _name = "dzexpert.manage.modules.menu"
    _inherit = ["mail.thread"]
    _description = "Menu"

    name = fields.Char("Nom", required=True)
    parent_id = fields.Many2one("dzexpert.manage.modules.menu", string="Parent")
    sequence = fields.Integer("Sequence", default=10)
    module_id = fields.Many2one("dzexpert.manage.modules.module", string="module")

    _order = "sequence"


class ModuleCategory(models.Model):
    _name = "dzexpert.manage.modules.module.category"
    _inherit = ["mail.thread"]
    _description = "Module category"

    name = fields.Char("Nom", required=True)


class OdooVersion(models.Model):
    _name = "dzexpert.manage.modules.odoo.version"
    _inherit = ["mail.thread"]
    _description = "Odoo version"

    name = fields.Char("Numéro de version", required=True)


class ModuleVersion(models.Model):
    _name = "dzexpert.manage.modules.module.version"
    _inherit = ["mail.thread"]
    _description = "Module version"

    name = fields.Char("Numéro de version", required=True)
    module_id = fields.Many2one("dzexpert.manage.modules.module", string="module")
    current_version = fields.Boolean(
        store=False, string="Version actuelle", compute="_compute_current_version"
    )
    date = fields.Date(string="Date", default=fields.Date.today())

    @api.depends("module_id.version_ids.date", "date")
    def _compute_current_version(self):
        for rec in self:
            most_recent_version = self.env[
                "dzexpert.manage.modules.module.version"
            ].search(
                [("module_id", "=", rec.module_id.id)],
                order="date desc",
                limit=1,
            )
            rec.current_version = most_recent_version.id == rec.id


class Module(models.Model):
    _name = "dzexpert.manage.modules.module"
    _inherit = ["mail.thread"]
    _description = "Module"

    name = fields.Char("Nom", required=True)
    overview = fields.Html("Overview")
    version_ids = fields.One2many(
        "dzexpert.manage.modules.module.version",
        "module_id",
        string="Versions",
    )
    icon = fields.Binary("Icon", attachment=True)
    state = fields.Selection(
        [
            ("draft", "Brouillon"),
            ("specs", "Spécification"),
            ("dev", "Développement"),
            ("testing", "Essai"),
            ("done", "Fait"),
        ],
        string="État",
        default="draft",
    )
    technical_name = fields.Char("Nom technique", required=True)
    type = fields.Selection(
        [
            ("odoo_modules", "Modules odoo"),
            ("dzexpert_modules", "Modules dzexpert"),
            ("third_parties", "Modules tiers"),
        ],
        string="type",
    )
    category_id = fields.Many2one(
        "dzexpert.manage.modules.module.category", string="Catégorie"
    )
    odoo_version_id = fields.Many2one(
        "dzexpert.manage.modules.odoo.version", string="Odoo version", required=True
    )
    security_group_ids = fields.One2many(
        "dzexpert.manage.modules.security.group",
        "module_id",
        string="Groupes de sécurité",
    )
    email_ids = fields.One2many(
        "dzexpert.manage.modules.email",
        "module_id",
        string="Emails",
    )
    menu_ids = fields.One2many(
        "dzexpert.manage.modules.menu",
        "module_id",
        string="Menus",
    )

    def change_state(self):
        if self.state == "draft":
            self.state = "specs"
        elif self.state == "specs":
            self.state = "dev"
        elif self.state == "dev":
            self.state = "testing"
        elif self.state == "testing":
            self.state = "done"

    def cancel_state(self):
        if self.state == "done":
            self.state = "testing"
        elif self.state == "testing":
            self.state = "dev"
        elif self.state == "dev":
            self.state = "specs"
        elif self.state == "specs":
            self.state = "draft"