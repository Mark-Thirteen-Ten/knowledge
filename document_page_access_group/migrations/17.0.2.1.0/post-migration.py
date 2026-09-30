# Copyright 2026
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(
        env,
        "document_page_access_group",
        "migrations/17.0.2.1.0/noupdate_changes.xml",
    )